---
Status: Pending
---

***

> [!query]
> ```query-text
> What brand name medications would my doctor likely prescribe if I have tumor-induced osteomalacia (TIO)?
> ```

***

> [!answer]
> ```answer-text
> If you have **tumor-induced osteomalacia (TIO)**, your doctor may consider the following **brand name medications**:
> 
> ### 1. **CRYSVITA® (burosumab-twza)**
> - **CRYSVITA** is the **only FDA-approved medication** specifically indicated for TIO that cannot be curatively resected (i.e., when the tumor cannot be found or removed surgically).
> - It is a **monoclonal antibody** that targets and inhibits **FGF23**, the hormone responsible for phosphate wasting in TIO.
> 
> ### 2. **Phosphate and Active Vitamin D Supplements**
> While not brand-name “medications” per se, **oral phosphate** and **active vitamin D (calcitriol)** are often used as supportive therapy when surgery is not possible or until the tumor is removed:
> - **Calcitriol (brand: Rocaltrol®)** or **alfacalcidol**
> - **Phoslyra®**, **K-Phos®**, or generic phosphate supplements
> 
> ### 3. **Other treatments**
> - The **mainstay of treatment** is **surgical removal of the tumor** when possible. Medications are typically used when surgery is not possible, not successful, or while searching for the tumor.
> 
> ---
> 
> **In summary:**  
> **CRYSVITA® (burosumab)** is the only approved brand medication for TIO. Calcitriol (Rocaltrol®) and phosphate supplements (Phoslyra®, K-Phos®) may also be used to manage symptoms.
> 
> **References:**
> - [FDA label for CRYSVITA](https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/761068s006lbl.pdf)
> - [UpToDate: Tumor-induced osteomalacia](https://www.uptodate.com/contents/tumor-induced-osteomalacia)
> 
> If you suspect you have TIO or have been diagnosed, please discuss treatment options with your physician, as treatment must be tailored to your individual case.
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
> CRYSVITA,Rocaltrol,Phoslyra,K-Phos
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
> N/A
> ```