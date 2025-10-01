<%*
// This script finds all generated answer files and compiles their contents into a single report.

// --- CONFIGURATION ---
const AUDIT_ROOT_PATH = "audit/Queries/Products";
const REPORT_OUTPUT_PATH = "audit/Reports";

// --- UTILITY FUNCTIONS (SELF-CONTAINED) ---

// Gets the content of the FIRST matching block.
function getBlock(content, blockName) {
    if (!content) return null;
    const regex = new RegExp('^>\\s*`{3}' + blockName + '\\n([\\s\\S]*?)^>\\s*`{3}', 'gm');
    const matches = [...content.matchAll(regex)];
    if (matches.length > 0) {
        const rawContent = matches[0][1];
        return rawContent.split('\n').map(line => line.replace(/^>\s*/, '')).join('\n').trim();
    }
    return null;
}

// Gets the content of ALL matching blocks.
function getAllBlocks(content, blockName) {
    if (!content) return [];
    const regex = new RegExp('^>\\s*`{3}' + blockName + '\\n([\\s\\S]*?)^>\\s*`{3}', 'gm');
    const matches = [...content.matchAll(regex)];
    return matches.map(match => {
        const rawContent = match[1];
        return rawContent.split('\n').map(line => line.replace(/^>\s*/, '')).join('\n').trim();
    });
}

// --- MAIN SCRIPT LOGIC ---
new Notice("🚀 Compiling audit report...");

// 1. Find all relevant answer files
const allFiles = app.vault.getMarkdownFiles();
const answerFiles = allFiles.filter(f => f.path.startsWith(AUDIT_ROOT_PATH) && f.name !== 'blank.md' && f.path.includes('/query-'));

if (answerFiles.length === 0) {
    return new Notice("❌ No answer files found to compile.", 5000);
}

const reportData = {};

// 2. Loop through each file and extract its data
for (const file of answerFiles) {
    const content = await app.vault.read(file);
    
    const pathParts = file.path.split('/');
    const medicationName = pathParts[3];
    const queryType = pathParts[4];
    
    if (!reportData[medicationName]) {
        reportData[medicationName] = {};
    }
    if (!reportData[medicationName][queryType]) {
        reportData[medicationName][queryType] = [];
    }
    
    const query = getBlock(content, "query-text");
    const answer = getBlock(content, "answer-text");
    const evalMeasuresRaw = getAllBlocks(content, "evaluation-yaml");
    const evalResults = getAllBlocks(content, "evaluation-result-text");
    
    const evalMeasures = evalMeasuresRaw.map(yamlText => {
        const match = yamlText.match(/- measure: (.*)/);
        return match ? match[1].trim().replace(/"/g, '') : "N/A";
    });

    reportData[medicationName][queryType].push({
        fileLink: `[[${file.path}|${file.name}]]`,
        query,
        answer,
        evaluations: evalMeasures.map((measure, i) => ({
            measure,
            result: evalResults[i] || "N/A"
        }))
    });
}

// 3. Build the final Markdown report string
let reportContent = `# AI Medication Audit Report\n\nGenerated on: ${new Date().toLocaleString()}\n\n`;

for (const medicationName in reportData) {
    reportContent += `***\n# ${medicationName}\n\n`;
    for (const queryType in reportData[medicationName]) {
        reportContent += `## ${queryType}\n\n`;
        for (const result of reportData[medicationName][queryType]) {
            reportContent += `### Response from ${result.fileLink}\n\n`;
            reportContent += `**Query:**\n> ${result.query}\n\n`;
            
            // Sanitize the answer for blockquote formatting
            const formattedAnswer = result.answer ? result.answer.replace(/\n/g, '\n> ') : "N/A";
            reportContent += `**Answer:**\n> ${formattedAnswer}\n\n`;
            
            reportContent += `**Evaluation Results:**\n\n`;
            reportContent += `| Measure | Result |\n`;
            reportContent += `| --- | --- |\n`;
            
            // --- FIX IS HERE ---
            result.evaluations.forEach(ev => {
                // Sanitize content for table compatibility: remove newlines and escape pipe characters
                const measureCell = (ev.measure || "").replace(/\|/g, '\\|').replace(/\n/g, '<br>');
                const resultCell = (String(ev.result) || "").replace(/\|/g, '\\|').replace(/\n/g, '<br>');
                reportContent += `| ${measureCell} | ${resultCell} |\n`;
            });
            reportContent += `\n`;
        }
    }
}

// 4. Create the new report file
const dateString = new Date().toISOString().split('T')[0];
const reportFileName = `AuditReport${dateString}.md`;

if (!await app.vault.adapter.exists(REPORT_OUTPUT_PATH)) {
    await app.vault.createFolder(REPORT_OUTPUT_PATH);
}

// Check if a report for today already exists
const reportFile = app.vault.getAbstractFileByPath(`${REPORT_OUTPUT_PATH}/${reportFileName}`);
if (reportFile) {
    // If it exists, overwrite it
    await app.vault.modify(reportFile, reportContent);
    new Notice(`✅ Report updated: ${reportFileName}`, 7000);
} else {
    // Otherwise, create a new one and open it
    const newFile = await tp.file.create_new(reportContent, `${REPORT_OUTPUT_PATH}/${reportFileName}`, true);
    new Notice(`✅ Report created: ${reportFileName}`, 7000);
}
%>