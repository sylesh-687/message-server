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
