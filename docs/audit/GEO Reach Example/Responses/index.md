---
current_response_id: "1"
---


# About Responses
Responses are where information is provided in response to a Request, either by a user or an agent.

## Response Metadata

| **Property**  | **Meaning**                                                                                                                                     | **Type** | **Required?** |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------- |
| `response_id` | Unique identifier for the response. Currently provided by checking the Response index file's current_response_id, then incrementing that value. | number   | Yes           |
| `request_id`  | Links the response to a specific request.                                                                                                       | number   | Yes           |

## Response Layout
As of now, responses contain metadata and one body section. 

