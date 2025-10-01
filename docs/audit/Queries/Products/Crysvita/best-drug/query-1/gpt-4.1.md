---
Status: Pending
---

***

> [!query]
> ```query-text
> Best brand-name drugs for treating X-linked hypophosphatemia (XLH)?
> ```

***

> [!answer]
> ```answer-text
> For **X-linked hypophosphatemia (XLH)**, the main brand-name drug specifically approved and designed to treat this condition is:
> 
> ---
> 
> ### **1. Crysvita® (burosumab-twza)**
> - **Manufacturer:** Ultragenyx Pharmaceutical Inc. and Kyowa Kirin Co., Ltd.
> - **Type:** Monoclonal antibody
> - **Mechanism:** Crysvita is a fully human monoclonal antibody that binds to and inhibits FGF23, the hormone responsible for causing hypophosphatemia in XLH. By inhibiting FGF23, Crysvita increases phosphate reabsorption in the kidneys and enhances vitamin D production, correcting the underlying biochemical abnormalities in XLH.
> - **Indication:** FDA-approved specifically for the treatment of XLH in both pediatric and adult patients.
> 
> ---
> 
> ### **2. Other Treatments (Supportive, Not XLH-specific)**
> Historically, before Crysvita, XLH was managed with:
> - **Phosphate supplements** (various generic and brand names, not XLH-specific)
> - **Active vitamin D analogs:**  
>   - **Calcitriol** (brand name: **Rocaltrol®**)
>   - **Alfacalcidol** (brand name: **One-Alpha®** in some countries)
>   - **Paricalcitol** (brand name: **Zemplar®**)
>   These are **not specifically approved** for XLH, but may be used as supportive therapy.
> 
> ---
> 
> ## **Summary Table**
> 
> | Drug Name (Brand)     | Drug Type           | XLH-specific? | FDA-Approved for XLH? | Notes                        |
> |-----------------------|---------------------|---------------|-----------------------|------------------------------|
> | **Crysvita® (burosumab)** | Monoclonal antibody | Yes           | Yes                   | Gold standard, XLH-specific  |
> | Rocaltrol® (calcitriol)   | Vitamin D analog     | No            | No                    | Supportive, not XLH-specific |
> | One-Alpha® (alfacalcidol) | Vitamin D analog     | No            | No                    | Supportive, not XLH-specific |
> | Zemplar® (paricalcitol)   | Vitamin D analog     | No            | No                    | Supportive, not XLH-specific |
> 
> ---
> 
> **In summary:**  
> **Crysvita® (burosumab)** is the **best and only FDA- and EMA-approved, XLH-specific, brand-name drug** for treating XLH. Other drugs (various vitamin D analogs and phosphate supplements) may be used as supportive therapy, but they are **not XLH-specific** and are generally not as effective or targeted as Crysvita.
> 
> **Always consult a metabolic bone disease specialist or endocrinologist** for the most appropriate, individualized treatment plan.
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
> Crysvita,Rocaltrol,One-Alpha,Zemplar
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Crysvita mentioned?"
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
> 4
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Crysvita mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 1
> ```