<%*
// CONFIGURATION
const GENERALIZED_QUERIES_PATH = "audit/Queries/Products/Generalized";
const MED_CONFIGS_PATH = "audit/Queries/Products/Config";
const OUTPUT_BASE_PATH = "audit/Queries/Products";

// HELPER FUNCTIONS
function getPlaceholders(str) { const regex = /{{\s*(\w+?)\s*}}/g; const matches = str.match(regex) || []; return [...new Set(matches.map(p => p.replace(/{{\s*|\s*}}/g, '')))]; }
const cartesian = (head, ...tail) => { if (!head) return [[]]; const tailProduct = cartesian(...tail); return head.flatMap(h => tailProduct.map(t => [h, ...t])); };

function parseMeasuresFromMarkdown(mdText) {
    if (!mdText) return [];
    const measures = [];
    const measureBlocks = mdText.split('* ---').slice(1);
    for (const block of measureBlocks) {
        const measureObj = { params: {} };
        const lines = block.trim().split('\n');
        for (const line of lines) {
            const match = line.match(/^\s*\*\s*([\w\.]+):\s*(.*)/);
            if (match) {
                const key = match[1].trim();
                const value = match[2].trim();
                if (key.startsWith('params.')) {
                    measureObj.params[key.split('.')[1]] = value;
                } else {
                    measureObj[key] = value;
                }
            }
        }
        if (measureObj.id) {
            measures.push(measureObj);
        }
    }
    return measures;
}

function stringifyMeasuresToMarkdown(measuresArray) {
    return measuresArray.map(measure => {
        let block = '* ---\n';
        for (const key in measure) {
            if (key === 'params') {
                for (const pKey in measure.params) {
                    block += `  * params.${pKey}: ${measure.params[pKey]}\n`;
                }
            } else {
                block += `  * ${key}: ${measure[key]}\n`;
            }
        }
        return block.trim();
    }).join('\n');
}

// MAIN BATCH SCRIPT LOGIC
const allConfigFiles = app.vault.getMarkdownFiles().filter(f => f.path.startsWith(MED_CONFIGS_PATH));
if (allConfigFiles.length === 0) return new Notice("❌ No config files found.", 5000);

const queryTemplateFiles = app.vault.getMarkdownFiles().filter(f => f.path.startsWith(GENERALIZED_QUERIES_PATH));
if (queryTemplateFiles.length === 0) return new Notice(`❌ No generalized query files found.`, 5000);

let totalFilesCreated = 0;
new Notice(`🚀 Starting BATCH query generation...`);

for (const configFile of allConfigFiles) {
    const configCache = app.metadataCache.getFileCache(configFile);
    const config = configCache?.frontmatter;
    if (!config || !config.medication_name || !config.placeholders) continue;
    
    const { medication_name, placeholders } = config;
    new Notice(`Processing: ${medication_name}...`);
    const medicationOutputPath = `${OUTPUT_BASE_PATH}/${medication_name}`;

    for (const templateFile of queryTemplateFiles) {
        const templateContent = await app.vault.cachedRead(templateFile);
        const contentParts = templateContent.split('# Measures');
        if (contentParts.length < 2) continue;
        
        const queryTemplatePart = contentParts[0];
        const measuresTemplatePart = contentParts[1];
        
        const allPlaceholders = getPlaceholders(templateContent);
        const valueArrays = [];
        const placeholderMap = {};
        for (const [i, p] of allPlaceholders.entries()) { valueArrays.push(placeholders[p] || [`[${p}_UNDEFINED]`]); placeholderMap[p] = i; }
        
        const combinations = cartesian(...valueArrays);
        const queryGroups = new Map();

        for (const combo of combinations) {
            let renderedQuery = queryTemplatePart;
            let renderedMeasuresText = measuresTemplatePart;
            for (const placeholderName of allPlaceholders) {
                const valueIndex = placeholderMap[placeholderName];
                const value = combo[valueIndex];
                const regex = new RegExp(`{{\\s*${placeholderName}\\s*}}`, 'g');
                renderedQuery = renderedQuery.replace(regex, value);
                renderedMeasuresText = renderedMeasuresText.replace(regex, value);
            }
            const queryKey = renderedQuery.trim();
            if (!queryGroups.has(queryKey)) { queryGroups.set(queryKey, { query: renderedQuery, measures: [] }); }
            const measuresForThisCombo = parseMeasuresFromMarkdown(renderedMeasuresText);
            queryGroups.get(queryKey).measures.push(...measuresForThisCombo);
        }

        let fileCounter = 1;
        for (const { query, measures } of queryGroups.values()) {
            const uniqueMeasures = [];
            const seenDescriptions = new Set();
            const idCounters = {};
            for (const measure of measures) {
                if (!seenDescriptions.has(measure.description)) {
                    const originalId = measure.id;
                    if (!idCounters[originalId]) { idCounters[originalId] = 0; }
                    idCounters[originalId]++;
                    if (idCounters[originalId] > 1) { measure.id = `${originalId}_${idCounters[originalId]}`; }
                    uniqueMeasures.push(measure);
                    seenDescriptions.add(measure.description);
                }
            }

            const prefixForCallout = (text) => text.split('\n').map(line => `> ${line}`).join('\n');
            const cleanQueryText = query.replace('# Query', '').trim();
            const queryBlock = prefixForCallout(`\`\`\`query-text\n${cleanQueryText}\n\`\`\``);
            const answerBlock = prefixForCallout(`\`\`\`answer-text\n\n\`\`\``);
            const measuresAsMarkdown = stringifyMeasuresToMarkdown(uniqueMeasures);
            const measuresBlock = prefixForCallout(`\`\`\`measures-md\n${measuresAsMarkdown}\n\`\`\``);

            const allEvaluationBlocks = uniqueMeasures.map(measure => {
                const singleMeasureDisplay = `- measure: ${measure.description}\n  type: ${measure.type}`;
                const evaluationBlock = prefixForCallout(`\`\`\`evaluation-yaml\n${singleMeasureDisplay}\n\`\`\``);
                const evalResultBlock = prefixForCallout(`\`\`\`evaluation-result-text\n\n\`\`\``);
                return `> [!evaluation]\n${evaluationBlock}\n\n> [!evaluation-result]\n${evalResultBlock}`;
            }).join('\n\n***\n\n');

            // --- FIX IS HERE ---
            const contentBlocks = [
                `---
Status: Pending
---`,
                `> [!query]\n${queryBlock}`,
                `> [!answer]\n${answerBlock}`,
                `> [!measures]-\n${measuresBlock}`,
                allEvaluationBlocks
            ];
            
            const newContent = contentBlocks.join('\n\n***\n\n');
            // --- END FIX ---
            
            const querySpecificDir = `${medicationOutputPath}/${templateFile.basename}/query-${fileCounter}`;
            const newFilePath = `${querySpecificDir}/blank`;

            if (!await app.vault.adapter.exists(newFilePath + ".md")) {
                if (!await app.vault.adapter.exists(querySpecificDir)) {
                    await app.vault.createFolder(querySpecificDir);
                }
                await tp.file.create_new(newContent, newFilePath, false);
                totalFilesCreated++;
            }
            fileCounter++;
        }
    }
}
new Notice(`✅ Batch Complete! Created ${totalFilesCreated} new query file(s).`, 7000);
%>