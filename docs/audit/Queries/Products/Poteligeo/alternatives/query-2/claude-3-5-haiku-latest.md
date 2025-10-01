---
Status: Pending
---

***

> [!query]
> ```query-text
> What are some available brand name alternatives to Zolinza ?
> ```

***

> [!answer]
> ```answer-text
> Zolinza (generic name: vorinostat) is a medication used to treat cutaneous T-cell lymphoma. Some alternative brand names or generic equivalents include:
> 
> 1. Vorinostat (generic name)
> 2. ISTODAX (romidepsin) - another histone deacetylase inhibitor used for similar conditions
> 3. Panobinostat (Farydak) - another HDAC inhibitor
> 
> It's important to note that while these medications have similar mechanisms of action, they are not exact substitutes and should only be used under medical supervision. Always consult with a healthcare professional to determine the most appropriate treatment for your specific condition.
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
>   * params.target: "Poteligeo"
>   * id: medication_mentioned
>   * description: "Is Poteligeo mentioned by name?"
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
>   * params.target: "Poteligeo"
>   * id: medication_position
>   * description: "Out of the drugs mentioned by name, what number in the order is Poteligeo?"
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
> Zolinza,ISTODAX,Farydak
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Poteligeo mentioned by name?"
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
> 3
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned by name, what number in the order is Poteligeo?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```