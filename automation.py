import subprocess
import time
import os

def run_command(command, check=True):
    """Run a shell command and return the output."""
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, text=True, check=check, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result

def apply_k8s_manifest(manifest_path):
    """Apply a Kubernetes manifest."""
    run_command(f"kubectl apply -f {manifest_path}")

def check_pod_status(pod_name):
    """Check if the pod is running and ready."""
    print(f"Checking status of pod: {pod_name}")
    while True:
        result = subprocess.run(f"kubectl get pod {pod_name}", shell=True, text=True, capture_output=True)
        if "Running" in result.stdout:
            print(f"Pod {pod_name} is running!")
            break
        print(f"Waiting for pod {pod_name} to be ready...")
        time.sleep(10)

def check_service_status(service_name):
    """Check if the service is running."""
    print(f"Checking status of service: {service_name}")
    while True:
        result = subprocess.run(f"kubectl get svc {service_name}", shell=True, text=True, capture_output=True)
        if service_name in result.stdout:
            print(f"Service {service_name} is running!")
            break
        print(f"Waiting for service {service_name} to be ready...")
        time.sleep(10)

def check_node_ready(node_name):
    """Check if the node is ready."""
    print(f"Checking status of node: {node_name}")
    while True:
        result = subprocess.run(f"kubectl get node {node_name}", shell=True, text=True, capture_output=True)
        if "Ready" in result.stdout:
            print(f"Node {node_name} is ready!")
            break
        print(f"Waiting for node {node_name} to be ready...")
        time.sleep(10)

def get_node_ip(node_name):
    """Get the IP address of the node."""
    print(f"Getting IP address of node: {node_name}")
    result = subprocess.run(f"kubectl get node {node_name} -o wide", shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        # Parse the IP address from the output
        for line in result.stdout.splitlines():
            if node_name in line:
                parts = line.split()
                node_ip = parts[5]  # IP address is in the 5th column (INTERNAL-IP)
                print(f"Node IP address is: {node_ip}")
                return node_ip
    print(f"Could not find IP address for node: {node_name}")
    return None

def check_path_exists(path, node_ip):
    """Check if the path exists on the node."""
    result = subprocess.run(f"ssh {node_ip} 'test -d {path}'", shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Path {path} does not exist, creating it...")
        subprocess.run(f"ssh {node_ip} 'sudo mkdir -p {path}'", shell=True)
        subprocess.run(f"ssh {node_ip} 'sudo chown -R <k8s_user>:<k8s_group> {path}'", shell=True)
    else:
        print(f"Path {path} exists.")

def main():
    print("Starting the deployment process...")

    # Step 1: Check if the node is ready and get the node IP
    node_name = "kind-control-plane"  # Replace with your actual node name
    check_node_ready(node_name)

    # Fetch node IP (should be 172.18.0.2 based on your kubectl output)
    node_ip = get_node_ip(node_name)
    if not node_ip:
        print(f"Failed to retrieve IP for node {node_name}. Exiting...")
        return

    # Step 2: Ensure the MongoDB path exists on the node
    check_path_exists("/mnt/data/mongodb", node_ip)

    # Step 3: Apply Persistent Volume (PV)
    apply_k8s_manifest("./mongodb-k8s/mongo-pv.yml")
    
    # Step 4: Apply Persistent Volume Claim (PVC)
    apply_k8s_manifest("./mongodb-k8s/PVC.yml")
    
    # Step 5: Deploy MongoDB StatefulSet and Service
    apply_k8s_manifest("./mongodb-k8s/stateful.yml")
    apply_k8s_manifest("./mongodb-k8s/service.yml")
    
    # Check MongoDB pod
    check_pod_status("mongodb-0")

    # Step 6: Deploy the Backend
    apply_k8s_manifest("./backend-k8s/deployment.yml")
    check_pod_status("backend-yolo")

    # Step 7: Apply Backend Service
    apply_k8s_manifest("./backend-k8s/service.yml")
    check_service_status("backend-yolo-service")

    # Step 8: Deploy the Frontend
    apply_k8s_manifest("./frontend-k8s/deployment.yml")
    check_pod_status("frontend-yolo")

    # Step 9: Apply Frontend Service
    apply_k8s_manifest("./frontend-k8s/service.yml")
    check_service_status("frontend-yolo-service")

    print("Deployment completed successfully! 🎉")

if __name__ == "__main__":
    main()
