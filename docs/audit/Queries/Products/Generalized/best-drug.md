# Query
Best brand-name drugs for treating {{effect}}?

# Measures
* ---
  * id: mentioned_drugs
  * description: "AI Task: Extract all mentioned drug names"
  * type: ai
  * prompt: "Based ONLY on the provided context, list all specific prescription medication BRAND NAMES mentioned, in the order they appear. Exclude generic names (e.g., include 'Tylenol', but exclude 'acetaminophen'). Your response MUST be a valid JSON array of strings. If no medications are mentioned, return an empty array []."
* ---
  * id: medication_mentioned
  * description: "Is {{medication}} mentioned?"
  * type: programmatic
  * input: mentioned_drugs
  * params.target: "{{medication}}"
  * logic: "return input.includes(params.target);"
* ---
  * id: total_drug_count
  * description: "How many specific drugs are mentioned?"
  * type: programmatic
  * input: mentioned_drugs
  * logic: "return input.length;"
* ---
  * id: medication_position
  * description: "Out of the drugs mentioned, what position is {{medication}} mentioned in?"
  * type: programmatic
  * input: mentioned_drugs
  * params.target: "{{medication}}"
  * logic: "const index = input.indexOf(params.target); return index === -1 ? 'N/A' : index + 1;"
