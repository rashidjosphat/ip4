import sys
import subprocess

pvc_process = subprocess.run(["kubectl apply -f ./mongodb-k8s/mongo-pv.yml"], shell=True, stdout=True)

