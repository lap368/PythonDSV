---
Status: Pending
---

***

> [!query]
> ```query-text
> Best brand-name drugs for treating "off" episodes in Parkinson's disease?
> ```

***

> [!answer]
> ```answer-text
> For managing "off" episodes in Parkinson's disease, some of the best brand-name drugs include:
> 
> 1. Apokyn (apomorphine) - Fast-acting injectable medication
> 2. Duopa (carbidopa/levodopa) - Intestinal gel delivery
> 3. Rytary (carbidopa/levodopa extended-release)
> 4. Gocovri (amantadine extended-release)
> 5. Nourianz (istradefylline) - Adenosine A2A receptor antagonist
> 
> Each medication has specific benefits and potential side effects, so treatment should be personalized with a neurologist based on individual patient needs and symptoms.
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
> Apokyn,Duopa,Rytary,Gocovri,Nourianz
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Nourianz mentioned?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "How many specific drugs are mentioned?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 5
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Nourianz mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 5
> ```