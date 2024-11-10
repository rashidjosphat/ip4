# Explanation of YOLO ECOMMERCE APPLICATION Setup

The purpose of this document is to explain the process outlined in the main `README.md` for setting up and deploying the YOLO eCommerce Application. This application helps users sell and buy products in a seamless e-commerce experience. The setup involves multiple steps, including configuring Kubernetes (K8S), deploying MongoDB, and running the backend and frontend services.

## Key Components

- **Kubernetes (K8S)**: Used to orchestrate containers and manage deployments.
- **MongoDB**: The database that stores product details and user information.
- **Backend**: Handles the application's business logic and interactions with the database.
- **Frontend**: The user interface where customers can browse and purchase products.

---

## Overview of the Steps

The main `README.md` walks you through setting up the YOLO application on a Kubernetes (K8S) cluster. It explains the deployment of various components like the database (MongoDB), backend, and frontend.

### 1. **Setting Up the Kubernetes Cluster**
   - **Kubernetes Cluster**: First, you need to create a Kubernetes cluster using your cloud provider (AWS, Google Cloud, Azure, etc.). This is a prerequisite for running the application on K8S.
   - **Kubectl**: You also need the `kubectl` command-line tool to interact with your cluster. The README has links to official documentation on how to install `kubectl` on your local machine.

### 2. **Persistent Volume (PV) Setup for MongoDB**
   - The database needs a persistent storage volume, so the product data can be saved even after containers are restarted.
   - **`mongo-pv.yml`**: This YAML file is used to provision a Persistent Volume (PV) on Kubernetes. The `kubectl apply -f ./mongodb-k8s/mongo-pv.yml` command is used to create the PV.
   - **Verifying PV**: Once the PV is created, you can verify it by running `kubectl get pv` to make sure it’s correctly provisioned.

### 3. **Creating a Persistent Volume Claim (PVC)**
   - The PVC is used to claim storage from the PV. This makes sure that the MongoDB instance has storage attached to it.
   - **`PVC.yml`**: This YAML file contains the configuration for the Persistent Volume Claim. You create it by running `kubectl apply -f ./mongodb-k8s/PVC.yml`.

### 4. **Deploying MongoDB StatefulSet**
   - MongoDB is deployed as a StatefulSet in Kubernetes. This ensures that the database pods have stable network identities and persistent storage.
   - **StatefulSet and Service**: The `stateful.yml` and `service.yml` files define the MongoDB deployment and expose the service to other components (like the backend).
   - After running the deployment commands, you check the status of MongoDB pods to ensure they are running correctly (`kubectl describe pod mongodb-0`).

### 5. **Deploying the Backend Service**
   - The backend service contains the application's business logic and connects to MongoDB.
   - **Backend Deployment**: The backend is deployed by running `kubectl apply -f ./backend-k8s/deployment.yml`. This creates the backend pod that handles product-related requests.
   - **Backend Service**: After deploying the pod, the backend service is exposed to the frontend via `kubectl apply -f ./backend-k8s/service.yml`.

### 6. **Deploying the Frontend**
   - The frontend is the user interface for interacting with the e-commerce platform.
   - The frontend is deployed with the command `kubectl apply -f ./frontend-k8s/deployment.yml`, and its service is exposed via `kubectl apply -f ./frontend-k8s/service.yml`.

### 7. **Automating the Deployment**
   - For those who want to skip the manual steps, there is a Python script `automation.py` that automates the entire process.
   - **Running the Automation**: You can run the script using `python3 automation.py`, and it will execute all of the necessary Kubernetes commands to set up the application. This saves time and effort for users who want a quicker setup.

---

## Additional Information

### Why Kubernetes?
   - **Scalability**: Kubernetes makes it easier to scale your application as the number of users grows.
   - **Self-Healing**: Kubernetes automatically restarts failed containers, making your application more reliable.
   - **Declarative Configuration**: Kubernetes allows you to define your application infrastructure in code (via YAML files), making it easy to recreate the environment or modify it as needed.

### Why MongoDB?
   - MongoDB is a NoSQL database that is well-suited for handling product and user data in an e-commerce application.
   - It allows for easy horizontal scaling, and its flexible schema makes it ideal for managing unstructured or semi-structured data, such as product listings.

### What is a StatefulSet in Kubernetes?
   - A StatefulSet is a Kubernetes resource that manages stateful applications. Unlike regular deployments, StatefulSets guarantee the ordering and uniqueness of pods, which is crucial for applications like databases that require stable identities and persistent storage.
   - In this case, MongoDB is deployed as a StatefulSet to ensure each pod has its own persistent storage and stable network identity.

### How the Backend and Frontend Communicate
   - The backend and frontend communicate over Kubernetes services. The backend service exposes the API to the frontend, which can then fetch product details or handle user authentication.
   - Kubernetes services provide load balancing and allow the backend and frontend to interact without worrying about individual pod IP addresses.

---

## Conclusion

The steps in the `README.md` document guide you through the entire process of setting up the YOLO eCommerce application on Kubernetes. By following these steps, you’ll have a fully functional e-commerce platform running on a Kubernetes cluster.

If you prefer to automate the deployment process, the `automation.py` script is provided to help you with that.

---

## Contact & Collaboration

For any questions, feedback, or collaboration opportunities, feel free to reach out to me:

- **Email**: [josphat.rashid@student.moringaschool.com](mailto:josphat.rashid@student.moringaschool.com)
- **Phone**: 0798190943

I’m always open to collaboration and would love to hear from you!
