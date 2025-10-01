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
> **Ongentys** is the brand name for **opicapone**, a medication used as an adjunctive treatment to levodopa/carbidopa in patients with Parkinson’s disease experiencing "off" episodes.
> 
> ### Brand Name Alternatives to Ongentys (Opicapone)
> 
> As of June 2024, **Ongentys** is the primary and only widely available **brand name** for opicapone globally. There are **no other brand name alternatives** for opicapone currently marketed in the United States, Europe, or most other regions. Generic versions of opicapone may become available in the future, but as of now, only Ongentys is on the market.
> 
> ### Alternatives in the Same Drug Class (COMT Inhibitors)
> 
> If you are seeking **other brand name medications** in the same class (**COMT inhibitors**) used for Parkinson’s disease, here are some options:
> 
> 1. **Comtan** (entacapone)
> 2. **Tasmar** (tolcapone)
> 
> #### Summary Table
> 
> | Brand Name | Generic Name | Drug Class         |
> |------------|--------------|--------------------|
> | Ongentys    | Opicapone    | COMT inhibitor     |
> | Comtan      | Entacapone   | COMT inhibitor     |
> | Tasmar      | Tolcapone    | COMT inhibitor     |
> 
> **Note:** Only Ongentys contains opicapone; Comtan and Tasmar are different medications within the same class.
> 
> ---
> 
> **References:**
> - FDA and EMA drug approvals databases (as of 2024)
> - Ongentys (opicapone) Prescribing Information
> 
> **If you are looking for opicapone specifically, Ongentys is currently the only brand name product available.** If you are looking for other COMT inhibitors, Comtan and Tasmar are the main brand name options.
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
> Ongentys,Comtan,Tasmar
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
> 3
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