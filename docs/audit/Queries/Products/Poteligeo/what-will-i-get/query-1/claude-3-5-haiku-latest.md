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
> For Mycosis Fungoides, a type of cutaneous T-cell lymphoma, doctors might prescribe several medications depending on the stage and severity of the condition:
> 
> 1. Topical Treatments:
> - Corticosteroid creams (e.g., Lidex, Diprolene)
> - Nitrogen mustard cream (Mustargen)
> 
> 2. Skin-Directed Therapies:
> - Mechlorethamine gel (Valchlor)
> - Bexarotene gel (Targretin)
> 
> 3. Systemic Treatments:
> - Interferon alfa (Intron A, Roferon-A)
> - Bexarotene oral capsules (Targretin)
> - Methotrexate
> - Vorinostat (Zolinza)
> 
> 4. Advanced Stage Treatments:
> - Romidepsin (Istodax)
> - Mogamulizumab (Poteligeo)
> 
> 5. Chemotherapy Options:
> - Gemcitabine
> - Liposomal doxorubicin (Doxil)
> 
> The specific medication will depend on individual patient factors, disease stage, and potential side effects. Your oncologist or dermatologist will determine the most appropriate treatment plan for your specific case.
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
> Lidex,Diprolene,Mustargen,Valchlor,Targretin,Intron A,Roferon-A,Targretin,Zolinza,Istodax,Poteligeo,Doxil
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
> 11
> ```