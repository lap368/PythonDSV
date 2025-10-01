---
Status: Pending
---

***

> [!query]
> ```query-text
> What brand name medications would my doctor likely prescribe if I have Mycosis Fungoides?
> ```

***

> [!answer]
> ```answer-text
> If you have **Mycosis Fungoides**, a type of cutaneous T-cell lymphoma, your doctor may consider a variety of treatment options, some of which involve brand name medications. The choice depends on the stage and severity of the disease. Here are some commonly prescribed brand name medications and therapies for Mycosis Fungoides:
> 
> ### Topical Therapies
> - **Valchlor®** (mechlorethamine gel): A topical chemotherapy agent.
> - **Targretin®** (bexarotene gel): A topical retinoid.
> 
> ### Systemic Therapies
> - **Targretin®** (bexarotene capsules): Oral retinoid for more advanced disease.
> - **Zolinza®** (vorinostat): An oral histone deacetylase (HDAC) inhibitor.
> - **Istodax®** (romidepsin): An intravenous HDAC inhibitor.
> - **Poteligeo®** (mogamulizumab): An intravenous monoclonal antibody.
> - **Adcetris®** (brentuximab vedotin): An antibody-drug conjugate for certain cases.
> - **Methotrexate** (no common brand name for lymphoma): Sometimes used orally or by injection.
> 
> ### Other Treatments
> - **Phototherapy** (PUVA, UVB): Not a medication, but often used as a first-line treatment.
> - **Interferon alfa** (brand names include Intron A®, Roferon-A®): Sometimes used for more advanced disease.
> 
> ### Notes:
> - **Corticosteroids** (topical and oral, e.g., Clobex® for clobetasol): Often used for skin inflammation but not disease-specific.
> - **Chemotherapy agents** (e.g., gemcitabine, liposomal doxorubicin): Used in advanced or refractory cases, but often not brand-specific.
> 
> **Please remember:** The specific medication and brand your doctor prescribes will depend on your individual disease characteristics, overall health, and prior treatments. Always discuss options with your oncologist or dermatologist specializing in cutaneous lymphomas.
> 
> **References:**
> - National Comprehensive Cancer Network (NCCN) Guidelines
> - Leukemia & Lymphoma Society
> - Mycosis Fungoides Foundation
> 
> If you have a particular stage or prior treatments, I can provide more tailored options.
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
> Valchlor,Targretin,Targretin,Zolinza,Istodax,Poteligeo,Adcetris,Intron A,Roferon-A,Clobex
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
> 10
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Poteligeo mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 6
> ```