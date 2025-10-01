---
Status: Pending
---

***

> [!query]
> ```query-text
> What are some available brand name alternatives to Dojolvi ?
> ```

***

> [!answer]
> ```answer-text
> **Dojolvi** is the brand name for **triheptanoin**, a medium-chain triglyceride used primarily for the treatment of long-chain fatty acid oxidation disorders (LC-FAODs). As of mid-2024, **Dojolvi** is the only branded, FDA-approved triheptanoin product available in the United States and most global markets.
> 
> ### Alternatives to Dojolvi
> 
> #### 1. **Triheptanoin (Generic)**
> - **Generic triheptanoin** is not widely available as of June 2024. The drug is patented and marketed exclusively by Ultragenyx under the Dojolvi brand.  
> - No other pharmaceutical companies currently offer *generic* or *alternative brand* versions of triheptanoin for medical use.
> 
> #### 2. **Other Medium-Chain Triglycerides (MCT Oil)**
> - **Non-branded MCT oil** (typically a mix of caprylic and capric acids, C8 and C10), available as nutritional supplements, is **not the same as triheptanoin (C7)** and is not approved for the treatment of LC-FAOD.  
> - Some clinicians may use MCT oil for supportive dietary management, but it is not a substitute for Dojolvi.
> 
> #### 3. **Other Treatments for LC-FAOD**
> - **Ravicti (glycerol phenylbutyrate)**: Used for urea cycle disorders, not LC-FAOD.
> - **Carnitine supplementation**: Sometimes used as adjuvant therapy in certain FAODs.
> - **Dietary management**: Low-fat, high-carbohydrate diets, frequent feeding, and avoidance of fasting.
> 
> ---
> 
> ### **Summary Table**
> 
> | Brand Name | Generic Name     | Indication        | Notes                                   |
> |------------|------------------|-------------------|-----------------------------------------|
> | Dojolvi    | Triheptanoin     | LC-FAOD           | Only FDA-approved triheptanoin          |
> | -          | MCT Oil          | Nutritional use   | Not equivalent, not FDA-approved for LC-FAOD |
> | -          | Carnitine, etc.  | Supportive        | Not a direct alternative                |
> 
> ---
> 
> **In summary:**  
> **Dojolvi (triheptanoin)** is the only FDA-approved, branded product for LC-FAOD. There are **no other brand name or generic triheptanoin products** currently available. If you are seeking alternatives, they would be off-label or supportive therapies, not direct substitutes.
> 
> **Always consult your healthcare provider before making changes to prescribed therapies.**
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
>   * params.target: "Crysvita"
>   * id: medication_mentioned
>   * description: "Is Crysvita mentioned by name?"
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
>   * params.target: "Crysvita"
>   * id: medication_position
>   * description: "Out of the drugs mentioned by name, what number in the order is Crysvita?"
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
> Dojolvi,Ravicti
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Crysvita mentioned by name?"
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
> 2
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned by name, what number in the order is Crysvita?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```