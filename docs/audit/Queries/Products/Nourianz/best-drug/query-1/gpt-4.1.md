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
> For **Parkinson's disease**, "**off**" episodes refer to periods when the effectiveness of **levodopa** wears off and symptoms (such as tremor, rigidity, and slowness) return. Several **brand-name drugs** are FDA-approved to manage or reduce "off" episodes by working as **add-on therapies** to levodopa/carbidopa. Here are the main options:
> 
> ---
> 
> ## 1. **Inbrija®** (inhaled levodopa)
> - **Form:** Inhaled powder
> - **Use:** Rapid relief of "off" symptoms
> - **How it works:** Provides a quick boost of levodopa via inhalation
> 
> ---
> 
> ## 2. **Apokyn®** (apomorphine injection)
> - **Form:** Subcutaneous injection
> - **Use:** Rapid, temporary relief from "off" episodes
> - **How it works:** Dopamine agonist; fast-acting, typically used as a rescue medication
> 
> ---
> 
> ## 3. **Kynmobi™** (apomorphine sublingual film)
> - **Form:** Sublingual (under the tongue) film
> - **Use:** Rapid relief of "off" episodes
> - **How it works:** Same active ingredient as Apokyn, but non-injectable
> 
> ---
> 
> ## 4. **Ongentys®** (opicapone)
> - **Form:** Oral capsule
> - **Use:** Reduces "off" time by prolonging levodopa effect
> - **How it works:** COMT inhibitor; taken once daily
> 
> ---
> 
> ## 5. **Xadago®** (safinamide)
> - **Form:** Oral tablet
> - **Use:** Reduces "off" time as an add-on to levodopa
> - **How it works:** MAO-B inhibitor with additional mechanisms
> 
> ---
> 
> ## 6. **Gocovri®** (amantadine ER)
> - **Form:** Extended-release capsule
> - **Use:** Also indicated to treat dyskinesia, may help with "off" episodes
> - **How it works:** NMDA receptor antagonist
> 
> ---
> 
> ### Other Options
> - **COMT inhibitors:** Entacapone (**Comtan®**) and tolcapone (**Tasmar®**) are older options.
> - **MAO-B inhibitors:** Rasagiline (**Azilect®**), selegiline (**Eldepryl®**, **Zelapar®**).
> 
> ---
> 
> ### **Summary Table**
> 
> | Brand Name   | Generic Name     | Route         | Main Role                         |
> |--------------|------------------|---------------|-----------------------------------|
> | Inbrija      | Levodopa         | Inhaled       | Rapid relief during "off"         |
> | Apokyn       | Apomorphine      | Injection     | Rapid rescue for "off"            |
> | Kynmobi      | Apomorphine      | Sublingual    | Rapid rescue for "off"            |
> | Ongentys     | Opicapone        | Oral          | Reduces "off" time                |
> | Xadago       | Safinamide       | Oral          | Reduces "off" time                |
> | Gocovri      | Amantadine ER    | Oral          | "Off" episodes & dyskinesia       |
> | Comtan       | Entacapone       | Oral          | Reduces "off" time                |
> | Azilect      | Rasagiline       | Oral          | Reduces "off" time                |
> 
> ---
> 
> **Selection depends on:**  
> - Type/severity of "off" episodes  
> - Patient preferences (oral, inhaled, injection)  
> - Side effect profile  
> - Insurance coverage
> 
> **Always consult a movement disorder specialist for optimal management.**
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
> Inbrija,Apokyn,Kynmobi,Ongentys,Xadago,Gocovri,Comtan,Azilect
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
> 8
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