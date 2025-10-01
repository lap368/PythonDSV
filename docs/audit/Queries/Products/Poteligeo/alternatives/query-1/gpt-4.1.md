---
Status: Pending
---

***

> [!query]
> ```query-text
> What are some available brand name alternatives to Adcetris ?
> ```

***

> [!answer]
> ```answer-text
> **Adcetris** is the brand name for **brentuximab vedotin**, an antibody-drug conjugate used to treat certain lymphomas (such as Hodgkin lymphoma and systemic anaplastic large cell lymphoma).
> 
> ### Brand Name Alternatives to Adcetris
> 
> As of **mid-2024**, **Adcetris** is the **original brand** of brentuximab vedotin, developed by Seattle Genetics (now Seagen) in partnership with Takeda. There are currently **no other brand name brentuximab vedotin products** approved in the US, Europe, or most major markets. **No biosimilar versions are currently approved** as of this date.
> 
> #### Summary:
> - **Adcetris** is the **only brand name** for brentuximab vedotin available.
> - **No biosimilars or brand alternatives** are approved yet (as of June 2024).
> 
> #### Related Information:
> - Other drugs for similar indications (but with **different mechanisms** and **not interchangeable**): **Keytruda** (pembrolizumab), **Opdivo** (nivolumab), **Rituxan** (rituximab), etc. However, **these are not alternatives** to Adcetris in terms of composition.
> 
> **If you are seeking alternatives for clinical or insurance reasons, please consult your oncologist, as treatment regimens are highly individualized.**
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
> Adcetris,Keytruda,Opdivo,Rituxan
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
> 4
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