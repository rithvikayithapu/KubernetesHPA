# Run the application 

## Step-1: Installation
- Docker must exist on the host machine
- Python installation guide could be found here: [Install Python](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/)
- Locust could be installed using: ```pip3 install locust ```

## Step-2: Minikube:
- Install Kubernetes using the following commands:
  ```
  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  chmod +x ./kubectl
  sudo mv ./kubectl /usr/local/bin/kubectl
  ```
- Install minikube using the following commands: 
  ```
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  minikube start --force
  ```
- Enable metrics monitoring using:
  ```
  minikube addons enable metrics-server
  ```

- Deploy the app and hpa using:
  ```
  kubectl apply -f server-deployment.yaml
  kubectl apply -f server-hpa.yaml
  ```
- To view the deployments, hpa and performance:
   ```
  kubectl get deployments
   kubectl get pods
   kubectl top nodes
   kubectl top pods
   ```

## Step-3: Locust Load Generation
- Type ```minikube ip```
- Type ```kubectl get services```
- To run ```locust -f locustfile.py --host=http://<minikube ip>:<Nodeport>```
