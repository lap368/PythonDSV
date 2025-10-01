---
current_request_id: "2"
---
# About Requests
Requests are how the audit pipeline indicates information that needs to be added in order for the process to continue. They may be requests that need to be filled out by the user or by AI agents. Metadata will indicate various important pieces of information about the request.

## Request Metadata

| **Property**        | **Meaning**                                                                                                                                                                                                                         | **Type** | **Required?** |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------- |
| `request_id`        | Unique identifier for the request for information. Allows responses to refer back to what request they are responding to. Currently provided by checking the Request index file's current_request_id, then incrementing that value. | number   | Yes           |
| `requires_citation` | Indicates whether some form of citation is required in order to fully answer the question. Defaults to false.                                                                                                                       | boolean  | No            |

## Request Layout
As of now, requests contain metadata and one body section. The body should clearly ask for the required piece of information.

