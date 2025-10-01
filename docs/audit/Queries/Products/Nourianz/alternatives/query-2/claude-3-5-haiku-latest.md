---
Status: Pending
---

***

> [!query]
> ```query-text
> What are some available brand name alternatives to Kynmobi ?
> ```

***

> [!answer]
> ```answer-text
> Kynmobi (apomorphine) is a medication used to treat "off" episodes in Parkinson's disease. As of my current knowledge, there aren't many direct brand-name alternatives specifically for this medication. However, some related medications for Parkinson's disease include:
> 
> 1. Apokyn (also apomorphine, similar to Kynmobi)
> 2. Inbrija (inhaled levodopa)
> 3. Duopa (carbidopa/levodopa intestinal gel)
> 
> It's important to note that the availability of specific alternatives can vary, and the best alternative would depend on an individual patient's specific symptoms and medical history. A neurologist or movement disorder specialist would be the best resource for determining the most appropriate alternative treatment.
> 
> Always consult with a healthcare professional before changing or substituting any medication.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: mentioned_drugs
>   * description: "AI Task: Extract all mentioned drug names"
>   * type: ai
>   * prompt: "Based ONLY on the provided context, list all specific prescription medication BRAND NAMES mentioned, in the order they appear. Exclude generic names (e.g., include 'Tylenol', but exclude 'acetaminophen'). Your response MUST be a valid JSON array of strings. If no medications are mentioned, return an empty array []."
> * ---
>   * params.target: "Nourianz"
>   * id: medication_mentioned
>   * description: "Is Nourianz mentioned by name?"
>   * type: programmatic
>   * input: mentioned_drugs
>   * logic: "return input.includes(params.target);"
> * ---
>   * id: total_drug_count
>   * description: "How many specific drugs are mentioned by name?"
>   * type: programmatic
>   * input: mentioned_drugs
>   * logic: "return input.length;"
> * ---
>   * params.target: "Nourianz"
>   * id: medication_position
>   * description: "Out of the drugs mentioned by name, what number in the order is Nourianz?"
>   * type: programmatic
>   * input: mentioned_drugs
>   * logic: "const index = input.indexOf(params.target); return index === -1 ? 'N/A' : index + 1;"
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "AI Task: Extract all mentioned drug names"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> Kynmobi,Apokyn,Inbrija,Duopa
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Nourianz mentioned by name?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> false
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "How many specific drugs are mentioned by name?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 4
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned by name, what number in the order is Nourianz?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```