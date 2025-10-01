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
> **Kynmobi** (apomorphine hydrochloride) is a sublingual film used for the **acute, intermittent treatment of “off” episodes in patients with Parkinson’s disease**. It is a **brand name** itself.
> 
> If you’re looking for **brand name alternatives** to Kynmobi for the same indication (on-demand, rapid relief of "OFF" episodes in Parkinson’s), the options are limited, as this is a specific therapeutic niche. Here are the main alternatives:
> 
> ---
> 
> ## 1. **Apokyn** (apomorphine hydrochloride injection)
> - **Brand Name:** Apokyn
> - **Formulation:** Subcutaneous injection
> - **Indication:** Acute, intermittent treatment of “off” episodes in advanced Parkinson’s disease
> - **How it compares:** Apokyn is the main alternative to Kynmobi, but it is administered via injection rather than sublingual film.
> 
> ---
> 
> ## 2. **Inbrija** (levodopa inhalation powder)
> - **Brand Name:** Inbrija
> - **Formulation:** Inhalation powder
> - **Indication:** For intermittent treatment of “off” episodes in patients with Parkinson’s disease treated with carbidopa/levodopa.
> - **How it compares:** While not the same drug, Inbrija is also used for rapid relief of “off” episodes, but delivers levodopa via inhalation.
> 
> ---
> 
> ## 3. **No generic apomorphine sublingual film is currently available** (as of June 2024).
> 
> ---
> 
> ### **Summary Table**
> 
> | Brand Name | Generic Name                     | Route               | Indication                                    |
> |------------|----------------------------------|---------------------|-----------------------------------------------|
> | Kynmobi    | Apomorphine HCl                  | Sublingual film     | "Off" episodes in Parkinson’s disease         |
> | Apokyn     | Apomorphine HCl                  | Subcutaneous injection | "Off" episodes in Parkinson’s disease     |
> | Inbrija    | Levodopa                         | Inhalation powder   | "Off" episodes in Parkinson’s disease         |
> 
> ---
> 
> **Note:**  
> - **Kynmobi** and **Apokyn** contain the same active ingredient (apomorphine), but are delivered differently.
> - **Inbrija** is a different drug (levodopa) but used for a similar "on-demand" purpose.
> 
> If you’re considering alternatives, consult your neurologist to determine which formulation and medication is most appropriate for your needs.
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
> Kynmobi,Apokyn,Inbrija
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