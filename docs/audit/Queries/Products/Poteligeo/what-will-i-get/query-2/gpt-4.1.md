---
Status: Pending
---

***

> [!query]
> ```query-text
> What brand name medications would my doctor likely prescribe if I have Sezary Syndrome?
> ```

***

> [!answer]
> ```answer-text
> If you have **Sézary syndrome** (a rare and aggressive form of cutaneous T-cell lymphoma), your doctor may consider several treatment options, many of which have well-known **brand names**. The specific medication(s) prescribed will depend on your individual case, previous treatments, and overall health. Here are some **common brand name medications** and therapies used for Sézary syndrome:
> 
> ---
> 
> ### **Systemic Therapies**
> 
> #### **Immunomodulatory and Biologic Agents**
> - **Zolinza®** (vorinostat): a histone deacetylase (HDAC) inhibitor.
> - **Istodax®** (romidepsin): another HDAC inhibitor.
> - **Poteligeo®** (mogamulizumab): a monoclonal antibody targeting CCR4, FDA-approved specifically for Sézary syndrome and mycosis fungoides.
> - **Adcetris®** (brentuximab vedotin): an antibody-drug conjugate used in some cases.
> - **Ontak®** (denileukin diftitox): a fusion protein, though less commonly used due to availability issues.
> 
> #### **Retinoids**
> - **Targretin®** (bexarotene): an oral retinoid specifically approved for cutaneous T-cell lymphoma.
> 
> #### **Interferons**
> - **Intron A®** (interferon alfa-2b): an immunomodulator, sometimes used off-label.
> 
> ---
> 
> ### **Chemotherapy**
> - **Treanda®** (bendamustine): sometimes used in refractory cases.
> - **Gemzar®** (gemcitabine): another option used in some patients.
> - **Pralatrexate** (Folotyn®): approved for peripheral T-cell lymphoma, sometimes used off-label.
> 
> ---
> 
> ### **Other Therapies**
> - **Photopheresis** (also called **extracorporeal photopheresis**): a procedure, not a drug, but sometimes called **UVADEX®** (methoxsalen) when used with this treatment.
> 
> - **Topical corticosteroids** and **topical nitrogen mustard** (Valchlor®) may be used, though these are more commonly for skin-limited disease (Sézary syndrome is a leukemic, systemic disease).
> 
> ---
> 
> **Note:**  
> - **Sézary syndrome** treatment is **highly individualized** and often **multimodal** (using several approaches).
> - **Clinical trials** may also be recommended, as this is a rare and challenging disease.
> 
> **Always** consult your **oncologist** or **hematologist** for the most appropriate, up-to-date, and personalized treatment plan.
> 
> **References**:  
> - [National Comprehensive Cancer Network (NCCN) Guidelines: Primary Cutaneous Lymphomas](https://www.nccn.org/professionals/physician_gls/pdf/primary_cutaneous.pdf)  
> - [Cutaneous Lymphoma Foundation – Sézary Syndrome Treatments](https://www.clfoundation.org/)
> 
> Let me know if you want **more detailed information** about **any of these medications** or **treatment strategies**!
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
> Zolinza,Istodax,Poteligeo,Adcetris,Ontak,Targretin,Intron A,Treanda,Gemzar,Folotyn,UVADEX,Valchlor
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Poteligeo mentioned?"
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
> 12
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Poteligeo mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 3
> ```