---
Status: Pending
---

***

> [!query]
> ```query-text
> Best brand-name drugs for treating tumor-induced osteomalacia (TIO)?
> ```

***

> [!answer]
> ```answer-text
> **Tumor-induced osteomalacia (TIO)** is a rare disorder usually caused by small, often benign, mesenchymal tumors that secrete **fibroblast growth factor 23 (FGF23)**. This leads to **phosphate wasting**, low levels of active vitamin D, and impaired bone mineralization (osteomalacia).
> 
> ### Mainstay of Treatment
> **Definitive treatment:**  
> - **Surgical removal of the tumor** (if found and resectable) is curative in most cases.
> 
> **When surgery is not possible or the tumor cannot be found:**
> 
> ### Best Brand-Name Drugs for Medical Management
> 
> #### 1. **Burosumab (Brand: Crysvita)**
> - **Mechanism:** Burosumab is a fully human monoclonal antibody that binds to and inhibits FGF23, thus correcting phosphate wasting.
> - **Indication:** Approved for **TIO** in adults and children aged 2 years and older in several regions (check local regulatory status).
> - **Efficacy:** Shown to increase serum phosphate, improve bone mineralization, and reduce symptoms.
> - **Brand Name:** **Crysvita**
> 
> #### 2. **Phosphate and Active Vitamin D Analogues**
> Traditionally, before burosumab, TIO was managed with:
> - **Oral phosphate supplements** (no single brand, various formulations)
> - **Active vitamin D analogs:**
>   - **Calcitriol** (Brand: **Rocaltrol**)
>   - **Alfacalcidol** (Brand: **One-Alpha**, in some countries)
> 
> **Note:** These are supportive and not disease-modifying; they do not address the underlying FGF23 excess.
> 
> ---
> 
> ## **Summary Table**
> 
> | Drug         | Brand Name  | Mechanism          | Notes                                            |
> |--------------|-------------|--------------------|--------------------------------------------------|
> | Burosumab    | Crysvita    | Anti-FGF23 antibody| First-line for unresectable/not found tumors     |
> | Calcitriol   | Rocaltrol   | Active vitamin D   | Supportive, used with phosphate supplements      |
> | Alfacalcidol | One-Alpha   | Vitamin D analog   | Supportive, used with phosphate supplements      |
> 
> ---
> 
> ## **Key Points**
> - **Crysvita (burosumab)** is the first and only targeted, FDA- and EMA-approved drug for TIO.
> - **Surgical removal** of the tumor, if possible, is curative.
> - **Phosphate and vitamin D analogs** are supportive, not curative, and require careful monitoring.
> 
> **Always consult a metabolic bone disease specialist or endocrinologist for diagnosis and management.**
> 
> **References:**  
> - Chong WH, et al. Tumor-induced osteomalacia. Endocr Relat Cancer. 2011.
> - Jan de Beur SM, et al. Burosumab for TIO. NEJM. 2022.
> - Crysvita (burosumab) Prescribing Information, Ultragenyx/ Kyowa Kirin.
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
> Crysvita,Rocaltrol,One-Alpha
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
> 1
> ```