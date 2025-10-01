---
Status: Pending
---

***

> [!query]
> ```query-text
> Best brand-name drugs for treating Mycosis Fungoides?
> ```

***

> [!answer]
> ```answer-text
> **Mycosis Fungoides** is the most common type of cutaneous T-cell lymphoma (CTCL). Treatment is individualized based on the stage, but there are several brand-name drugs commonly used, either alone or in combination.
> 
> ### **Topical Treatments**
> - **Valchlor® (mechlorethamine gel):** A topical chemotherapy for early-stage disease.
> - **Elidel® (pimecrolimus) and Protopic® (tacrolimus):** Topical immunomodulators, sometimes used off-label.
> - **Steroid creams** (various brands like **Clobex®**, **Temovate®** for clobetasol): Potent topical corticosteroids.
> 
> ### **Phototherapy**
> - **No specific brand**; Narrowband UVB or PUVA (psoralen + UVA) are standard.
> 
> ### **Oral/Systemic Therapies**
> - **Targretin® (bexarotene):** An oral retinoid specifically approved for CTCL.
> - **Zolinza® (vorinostat):** An oral histone deacetylase (HDAC) inhibitor.
> - **Istodax® (romidepsin):** An intravenous HDAC inhibitor.
> - **Poteligeo® (mogamulizumab):** A monoclonal antibody for relapsed/refractory CTCL.
> - **Adcetris® (brentuximab vedotin):** Antibody-drug conjugate for CD30-positive cases.
> - **Methotrexate** (various brands such as **Trexall®**): Used off-label for some patients.
> - **Pralatrexate (Folotyn®):** An antifolate chemotherapy approved for peripheral T-cell lymphoma, occasionally used in CTCL.
> 
> ### **Other Modalities**
> - **Interferon alfa-2b** (brand: **Intron® A**, **Roferon®-A**): Used in some cases.
> - **Total skin electron beam therapy (TSEB):** Not a drug, but important in advanced skin involvement.
> 
> ---
> 
> ## **Summary Table: Common Brand-Name Drugs for Mycosis Fungoides**
> 
> | Drug Name (Brand)         | Drug Class                   | Route     | Indication Stage         |
> |-------------------------- |-----------------------------|-----------|-------------------------|
> | **Valchlor®**             | Topical alkylator            | Topical   | Early                   |
> | **Targretin®**            | Retinoid (rexinoid)          | Oral      | Advanced/refractory     |
> | **Zolinza®**              | HDAC inhibitor               | Oral      | Advanced/refractory     |
> | **Istodax®**              | HDAC inhibitor               | IV        | Advanced/refractory     |
> | **Poteligeo®**            | Monoclonal antibody (CCR4)   | IV        | Advanced/refractory     |
> | **Adcetris®**             | CD30 antibody-drug conjugate | IV        | CD30+ cases             |
> | **Folotyn®**              | Antifolate chemotherapy      | IV        | Advanced/refractory     |
> | **Elidel®/Protopic®**     | Topical immunomodulator      | Topical   | Early (off-label)       |
> | **Intron® A**             | Interferon                   | IV/SC     | Advanced/refractory     |
> 
> ---
> 
> **Note:**  
> - **Treatment is highly individualized** and often requires specialist (dermatologist or oncologist) guidance.
> - **Some drugs are used off-label** for Mycosis Fungoides.
> - **Other supportive/adjunct therapies** (e.g., phototherapy, radiation) are also important.
> 
> **Always consult with a healthcare provider specializing in CTCL for the most appropriate and up-to-date therapy for your specific case.**
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
>   * description: "Is Poteligeo mentioned?"
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
>   * params.target: "Poteligeo"
>   * id: medication_position
>   * description: "Out of the drugs mentioned, what position is Poteligeo mentioned in?"
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
> Valchlor®,Elidel®,Protopic®,Clobex®,Temovate®,Targretin®,Zolinza®,Istodax®,Poteligeo®,Adcetris®,Trexall®,Folotyn®,Intron® A,Roferon®-A
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Poteligeo mentioned?"
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
> 14
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Poteligeo mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```