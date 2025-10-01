---
Status: Pending
---

***

> [!query]
> ```query-text
> What brand name medications would my doctor likely prescribe if I have X-linked hypophosphatemia (XLH)?
> ```

***

> [!answer]
> ```answer-text
> If you have **X-linked hypophosphatemia (XLH)**, the main brand name medication your doctor may prescribe is:
> 
> ### 1. **Crysvita®** (burosumab-twza)
> - **Crysvita** is a monoclonal antibody that targets FGF23, the protein overactive in XLH.
> - It is the **first and only FDA-approved treatment specifically for XLH** in both children and adults.
> - It is given as a subcutaneous injection, usually every 2 or 4 weeks.
> 
> ---
> 
> ### Other Treatments (not specific to XLH, but sometimes used):
> 
> **Before Crysvita, treatment options were limited to:**
> - **Phosphate supplements** (various brands, usually as over-the-counter or compounded preparations, not a specific brand for XLH)
> - **Active vitamin D analogs** (such as **calcitriol** (brand: **Rocaltrol®**), or **alfacalcidol** (brand: **One-Alpha®** in some countries))
> 
> These are **not brand name medications for XLH** specifically, but are sometimes used as supportive therapy, especially in settings where Crysvita may not be available or appropriate.
> 
> ---
> 
> ## **Summary Table**
> 
> | Medication Name | Brand Name  | Purpose in XLH                           |
> |-----------------|-------------|------------------------------------------|
> | Burosumab       | Crysvita®   | XLH-specific, targets FGF23              |
> | Calcitriol      | Rocaltrol®  | Active vitamin D analog, supportive      |
> | Alfacalcidol    | One-Alpha®  | Active vitamin D analog, supportive      |
> | Phosphate tabs  | (various)   | Phosphate replacement, supportive        |
> 
> **Crysvita** is the primary, XLH-specific, brand name medication your doctor is likely to prescribe.
> 
> **Always consult your doctor for the treatment best suited to your case.**
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
>   * params.target: "Crysvita"
>   * id: medication_mentioned
>   * description: "Is Crysvita mentioned?"
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
>   * params.target: "Crysvita"
>   * id: medication_position
>   * description: "Out of the drugs mentioned, what position is Crysvita mentioned in?"
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
> Crysvita®,Rocaltrol®,One-Alpha®
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Crysvita mentioned?"
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
> 3
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Crysvita mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```