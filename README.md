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
