<%*
// ---------------------------------------------------------------------
//                          CONFIGURATION
// ---------------------------------------------------------------------
const GENERALIZED_QUERIES_PATH = "audit/Queries/Products/Generalized";
const MED_CONFIGS_PATH = "audit/Queries/Products/Config";
const OUTPUT_BASE_PATH = "audit/Queries/Products";

// ---------------------------------------------------------------------
//                          HELPER FUNCTIONS
// ---------------------------------------------------------------------
function getPlaceholders(str) { const regex = /{{\s*(\w+?)\s*}}/g; const matches = str.match(regex) || []; return [...new Set(matches.map(p => p.replace(/{{\s*|\s*}}/g, '')))]; }
const cartesian = (head, ...tail) => { if (!head) return [[]]; const tailProduct = cartesian(...tail); return head.flatMap(h => tailProduct.map(t => [h, ...t])); };

// ---------------------------------------------------------------------
//                          MAIN SCRIPT LOGIC
// ---------------------------------------------------------------------
// ... (Initial setup fetching config and query template files is the same) ...

const configFiles = app.vault.getMarkdownFiles().filter(f => f.path.startsWith(MED_CONFIGS_PATH));
if (configFiles.length === 0) return new Notice("❌ Error: No medication config files found.", 5000);

const selectedConfigFile = await tp.system.suggester(configFiles.map(f => f.basename), configFiles);
if (!selectedConfigFile) return new Notice("⚠️ Process cancelled.", 3000);

const configCache = app.metadataCache.getFileCache(selectedConfigFile);
const config = configCache?.frontmatter;
if (!config || !config.medication_name || !config.placeholders) return new Notice(`❌ Error: Invalid configuration in "${selectedConfigFile.basename}".`, 5000);

const { medication_name, placeholders } = config;
const medicationOutputPath = `${OUTPUT_BASE_PATH}/${medication_name}`;
const queryTemplateFiles = app.vault.getMarkdownFiles().filter(f => f.path.startsWith(GENERALIZED_QUERIES_PATH));

let filesCreatedCount = 0;
new Notice(`🚀 Starting query generation for ${medication_name}...`);

for (const templateFile of queryTemplateFiles) {
    const templateContent = await app.vault.cachedRead(templateFile);
    
    const queryTemplatePart = templateContent.split('# Measures')[0];
    const measuresMatch = templateContent.match(/# Measures\n```yaml([\s\S]*?)```/);
    const measuresTemplatePart = measuresMatch ? measuresMatch[1].trim() : '';

    if (!measuresTemplatePart) continue;

    const allPlaceholders = getPlaceholders(templateContent);
    const valueArrays = [];
    const placeholderMap = {};
    for (const [i, p] of allPlaceholders.entries()) {
        valueArrays.push(placeholders[p] || [`[${p}_UNDEFINED]`]);
        placeholderMap[p] = i;
    }

    const combinations = cartesian(...valueArrays);
    const queryGroups = new Map();

    for (const combo of combinations) {
        let renderedQuery = queryTemplatePart;
        let renderedMeasuresYAML = measuresTemplatePart;
        
        for (const placeholderName of allPlaceholders) {
            const valueIndex = placeholderMap[placeholderName];
            const value = combo[valueIndex];
            const regex = new RegExp(`{{\\s*${placeholderName}\\s*}}`, 'g');
            renderedQuery = renderedQuery.replace(regex, value);
            renderedMeasuresYAML = renderedMeasuresYAML.replace(regex, value);
        }

        const queryKey = renderedQuery.trim();
        if (!queryGroups.has(queryKey)) {
            queryGroups.set(queryKey, { query: renderedQuery, measures: [] });
        }
        
        const measuresForThisCombo = tp.user.parseYaml(renderedMeasuresYAML);
        queryGroups.get(queryKey).measures.push(...measuresForThisCombo);
    }

    let fileCounter = 1;
    for (const { query, measures } of queryGroups.values()) {
        
        const uniqueMeasures = [];
        const seenDescriptions = new Set();
        const idCounters = {}; // To track usage of each original ID

        for (const measure of measures) {
            if (!seenDescriptions.has(measure.description)) {
                
                // --- NEW ID UNIQUENESS LOGIC ---
                const originalId = measure.id;
                // Initialize counter for this id if it's the first time we've seen it
                if (!idCounters[originalId]) {
                    idCounters[originalId] = 0;
                }
                idCounters[originalId]++; // Increment the counter

                // If this is the second or later time we've seen this original ID, make the new ID unique
                if (idCounters[originalId] > 1) {
                    measure.id = `${originalId}_${idCounters[originalId]}`;
                }
                // --- END NEW LOGIC ---

                uniqueMeasures.push(measure);
                seenDescriptions.add(measure.description);
            }
        }

        const prefixForCallout = (text) => text.split('\n').map(line => `> ${line}`).join('\n');
        
        const cleanQueryText = query.replace('# Query', '').trim();
        const queryBlock = prefixForCallout(`\`\`\`query-text\n${cleanQueryText}\n\`\`\``);
        const answerBlock = prefixForCallout(`\`\`\`answer-text\n\n\`\`\``);
        
        const measuresAsYaml = tp.user.stringifyYaml(uniqueMeasures);
        const measuresBlock = prefixForCallout(`\`\`\`measures-yaml\n${measuresAsYaml}\n\`\`\``);

        const allEvaluationBlocks = uniqueMeasures.map(measure => {
            const singleMeasureYaml = `- measure: ${measure.description}\n  type: ${measure.type}`;
            const evaluationBlock = prefixForCallout(`\`\`\`evaluation-yaml\n${singleMeasureYaml}\n\`\`\``);
            const evalResultBlock = prefixForCallout(`\`\`\`evaluation-result-text\n\n\`\`\``);
            return `> [!evaluation]\n${evaluationBlock}\n\n> [!evaluation-result]\n${evalResultBlock}`;
        }).join('\n\n***\n\n');

        const newContent = `---
Status: Pending
---

> [!query]
${queryBlock}

***

> [!answer]
${answerBlock}

***

> [!measures]-
${measuresBlock}

***

${allEvaluationBlocks}
`;
        
        const querySpecificDir = `${medicationOutputPath}/${templateFile.basename}/query-${fileCounter}`;
        const newFilePath = `${querySpecificDir}/blank`;

        if (!await app.vault.adapter.exists(querySpecificDir)) {
            await app.vault.createFolder(querySpecificDir);
        }
        await tp.file.create_new(newContent, newFilePath, false);
        filesCreatedCount++;
        fileCounter++;
    }
}
new Notice(`✅ Success! Created ${filesCreatedCount} unique query file(s) for ${medication_name}.`, 5000);
%>