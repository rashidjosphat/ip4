# YOLO ECOMMERCE APPLICATION
this application is an e-commerce application. which assist ussers in selling and buying product, 
user can sell there product by loging in and then add product 
 ![the add product image](addProduct.png)
, after the product details are 
added the product will be deplayed to customers who can order your product from the application like this .
![viewing product](product.png)


# RUNNING THE APPLICATION IN K8S
the application is configure in a way it can run on k8s so after creting a cluster in your clowd provider we start by creating a persistent volume so that our database can keep parsist the product details.

## Preriquesites
first of all things we need to have our clone application in you machine so
after creating a derectory where you want to store the application provision files run.
```bash
    git clone https://github.com/rashidjosphat/ip4.git
```
this will clone this repo. 
the other tools you must have before proceeding is kubectl for communicating with your cluster. You can find
detail explanation on how to install it in the [kube install](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/).

### creating a PV
in the mongodb-k8s folder there is a file called mongo-pv.yml that is what we gona use to provision our PV.
so afte cd into the directory with our yolo files run 
```bash
    kubectl apply -f ./mongodb-k8s/mongo-pv.yml
```
this command will create a PV resorce in your cluster. to comfirm that it is indeed running run command.

```bash
    kubctl get pv
```
this will output something like this 
!(pv)[pv.png]

now lets start our persistent volume claim which is ment to connect our database to the pv run the command.
```bash
    kubectl apply -f ./mongodb-k8s/PVC.yml 
```
to confirm that our pvc is running seccesfully run command.
```bash
    kubectl get pvc
    kubctl get pv
```
this will autput somethis like .
(pvc)[pvc.png]

afte we have confirmed that our pvc is running and connected with the pv lets now run our stateful mongo application and its related service.
```bash 
    kubectl apply -f ./mongodb-k8s/stateful.yml
    kubectl apply -f ./mongodb-k8s/service.yml

```
this could take a while depending on the size of the image size because it must pull the mongo:latest image as stated in our stateful.yml file.
To confirm that there are no error you can run .
```bash 
    kubectl describe pod mongodb-0
```
i know what you are thinking 'pods have unic name ' thats true but in our mongo db resource we created it using stateful resource that mean when the control plane is sheduling the creation of the pod it gona start with 0 and then autoincrement the pods but keep in mind that only happens in stateful deployment now that .
so the describe command above will output something like this .
!(mongodb describe output)[./images/describe_mongodb.png]


this verify that our mongodb is being brought up without any error you should be happy by now because we are out of the hard part now come the fun stuffs 🙄🥹.


