<%*
const { getMeta, setMeta, updateMeta, parseFrontmatter } = tp.user.metaUtils;
const workspace = tp.app.workspace;
const activeFile = workspace.getActiveFile();
const auditRoot = activeFile.parent.parent;

// Identify Responses directory and index
const responsesDirPath = auditRoot.path + "/Responses";
const responsesIndexPath = responsesDirPath + "/index";

let addOneToString = function(value) {
	return "" + (parseInt(value) + 1) + ""
}

const { oldValue } = await updateMeta(tp, responsesIndexPath, "current_response_id", addOneToString, "0");
let currentId = oldValue;

// Get metadata from the current request file
const requestId = await getMeta(tp, activeFile.path, "request_id", "unknown");
const requiresCitation = await getMeta(tp, activeFile.path, "requires_citation", "false");

// Get the question from the body of the request file
const requestContent = await tp.file.content;
const { body } = parseFrontmatter(requestContent);
const question = body.trim();

// Build the content for the new response file
const requestLink = `[[${activeFile.basename}]]`;
const responseFileContent = `---
response_id: "${currentId}"
request_id: "${requestId}"
---
## Request
${requestLink}

## Question
${question}

## Response
`;

// Create the new response file
const responseFileName = `Response_${currentId}.md`;
const responseFilePath = responsesDirPath + "/" + responseFileName;

const newFile = await app.vault.create(responseFilePath, responseFileContent);

// Open the newly created file 
await app.workspace.getLeaf(false).openFile(newFile);

%>