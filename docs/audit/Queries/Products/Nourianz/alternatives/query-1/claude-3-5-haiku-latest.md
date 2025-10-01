---
Status: Pending
---

***

> [!query]
> ```query-text
> What are some available brand name alternatives to Ongentys ?
> ```

***

> [!answer]
> ```answer-text
> Ongentys (opicapone) is a medication used to treat Parkinson's disease. Some alternative brand name medications in the same therapeutic class include:
> 
> 1. Comtan (entacapone)
> 2. Stalevo (carbidopa/levodopa/entacapone combination)
> 3. Tasmar (tolcapone)
> 
> These medications are COMT (Catechol-O-methyltransferase) inhibitors used to help manage Parkinson's disease symptoms. However, the specific alternative that might be most appropriate depends on individual patient factors, so consulting a healthcare professional is recommended.
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
> Ongentys,Comtan,Stalevo,Tasmar
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