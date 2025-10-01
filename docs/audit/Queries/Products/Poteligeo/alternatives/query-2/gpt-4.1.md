---
Status: Pending
---

***

> [!query]
> ```query-text
> What are some available brand name alternatives to Zolinza ?
> ```

***

> [!answer]
> ```answer-text
> **Zolinza** is the brand name for **vorinostat**, a histone deacetylase inhibitor used mainly for the treatment of **cutaneous T-cell lymphoma (CTCL)**. If you are seeking **brand name alternatives** to Zolinza (vorinostat), there are some important points to consider:
> 
> ### 1. **Vorinostat (Zolinza)**
> - **Zolinza** is the only widely available brand name for vorinostat itself.
> - Generic versions of vorinostat may be available in some markets, but typically under the generic name "vorinostat".
> 
> ### 2. **Other HDAC Inhibitors (Brand Name Alternatives)**
> If you are looking for other **brand name drugs** with a similar mechanism of action (HDAC inhibitors) used for similar indications, here are some alternatives:
> 
> #### **Romidepsin**
> - **Brand name:** Istodax®
> 
> #### **Belinostat**
> - **Brand name:** Beleodaq®
> 
> #### **Panobinostat**
> - **Brand name:** Farydak®
> 
> #### **Chidamide** (not available in all countries)
> - **Brand name:** Epidaza (mainly in China and some other regions)
> 
> ### 3. **Summary Table**
> 
> | Drug Name (Generic) | Brand Name   | Indication(s)                      | Class                |
> |---------------------|--------------|-------------------------------------|----------------------|
> | Vorinostat          | Zolinza      | CTCL, off-label in other cancers    | HDAC inhibitor       |
> | Romidepsin          | Istodax      | CTCL, PTCL                          | HDAC inhibitor       |
> | Belinostat          | Beleodaq     | PTCL                                | HDAC inhibitor       |
> | Panobinostat        | Farydak      | Multiple myeloma                    | HDAC inhibitor       |
> | Chidamide           | Epidaza      | PTCL, other (mainly China)          | HDAC inhibitor       |
> 
> ### **Note**
> - **Zolinza** is the only brand name for vorinostat approved in most regions.
> - If you specifically need an alternative with the **same active ingredient** (vorinostat), only generic versions (labeled as "vorinostat") may be available.
> - If you are looking for **brand name drugs with a similar mechanism** for similar indications, consider **Istodax, Beleodaq,** or **Farydak**.
> 
> **Always consult your healthcare provider** before switching medications, as different drugs—even in the same class—may have different efficacy, side effect profiles, and approved uses.
> 
> **References:**
> - FDA drug labels
> - National Comprehensive Cancer Network (NCCN) Guidelines
> - [Drugs.com - Zolinza alternatives](https://www.drugs.com/mtm/zolinza.html)
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
> Zolinza,Istodax,Beleodaq,Farydak,Epidaza
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
> 5
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