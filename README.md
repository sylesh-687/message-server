# Message Application
This API service provides endpoints for managing messages, including creating, retrieving, updating, and deleting messages. It implements the following message data structure:

```
{
    "account_id": "<id>",
    "message_id": "<random-uuid>",
    "sender_number": "<PHONE_NUMBER>",
    "receiver_number": "<PHONE_NUMBER>"
}
```

## How to deploy This application?
### Pre-reqs
- PostgresDB
- Kubernetes Cluster
- Git
- Kubectl

### Steps
In this example i have used multipass for ubuntu containers (https://multipass.run/) and have installed k3s (https://k3s.io/)

#### Step1 

Create Ubuntu Container 

```
multipass launch --name demo-server --disk 10G
```
Enter into the Container
```
multipass shell demo-server
```
Clone the repo
```
git clone https://github.com/sylesh-687/message-server.git
```
#### Step2
Update the Manifest with pg_endpoint

```
vim message-server/apiserver/kubernetes-manifests/message_server.yml
```

<img width="1469" alt="image" src="https://github.com/sylesh-687/message-server/assets/101313682/342858e2-4790-418a-9e06-d7a3eeac5726">

Apply the manifest

```
kubectl apply -f message-server/apiserver/kubernetes-manifests/message_server.yml
```

Update the Egress in network policy for the webserver to postgres
```
vim message-server/apiserver/kubernetes-manifests/message_server.yml
```
<img width="902" alt="image" src="https://github.com/sylesh-687/message-server/assets/101313682/25b83d74-b2e2-4f8f-aeca-996d88b6378c">

Access the application at http://<node>:30007
<img width="1239" alt="image" src="https://github.com/sylesh-687/message-server/assets/101313682/6662758f-8c33-4e0a-9a10-b571d49076fe">

