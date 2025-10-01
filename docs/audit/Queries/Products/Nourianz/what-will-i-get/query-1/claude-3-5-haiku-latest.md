---
Status: Pending
---

***

> [!query]
> ```query-text
> What brand name medications would my doctor likely prescribe if I have "off" episodes in Parkinson's disease?
> ```

***

> [!answer]
> ```answer-text
> For managing "off" episodes in Parkinson's disease, doctors might prescribe:
> 
> 1. Branded Medications:
> - Stalevo (carbidopa/levodopa/entacapone)
> - Rytary (extended-release carbidopa/levodopa)
> - Duopa (carbidopa/levodopa intestinal gel)
> - Apokyn (apomorphine injection)
> - Inbrija (inhaled levodopa)
> - Ongentys (opicapone)
> 
> 2. Medication Types:
> - Dopamine agonists
> - COMT inhibitors
> - Extended-release formulations
> - Fast-acting rescue medications
> 
> The specific prescription depends on individual patient factors like symptoms, medication tolerance, and disease progression. Always consult with a neurologist specializing in Parkinson's disease for personalized treatment recommendations.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: mentioned_drugs
>   * description: "AI Task: Extract all mentioned drug names"
>   * type: ai
>   * prompt: "Based ONLY on the provided context, list all specific prescription medication BRAND NAMES mentioned, in the order they appear. Exclude generic names (e.g., include 'Tylenol', but exclude 'acetaminophen'). In cases where both a brand name and a generic name have been provided and it is unclear which is the brand name and which is the common name, it is fine to include both. Your response MUST be a valid JSON array of strings. If no medications are mentioned, return an empty array []."
> * ---
>   * params.target: "Nourianz"
>   * id: medication_mentioned
>   * description: "Is Nourianz mentioned?"
>   * type: programmatic
>   * input: mentioned_drugs
>   * logic: "return input.includes(params.target);"
> * ---
>   * id: total_drug_count
>   * description: "How many specific drugs are mentioned?"
>   * type: programmatic
>   * input: mentioned_drugs
>   * logic: "return input.length;"
> * ---
>   * params.target: "Nourianz"
>   * id: medication_position
>   * description: "Out of the drugs mentioned, what position is Nourianz mentioned in?"
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
> Stalevo,Rytary,Duopa,Apokyn,Inbrija,Ongentys
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Nourianz mentioned?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> false
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "How many specific drugs are mentioned?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 6
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Nourianz mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```