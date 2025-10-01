---
Status: Pending
---

***

> [!query]
> ```query-text
> What brand name medications would my doctor likely prescribe if I have "off" episodes in Parkinson's disease?
> ```

***

> [!answer]
> ```answer-text
> If you are experiencing "off" episodes with Parkinson's disease—times when your usual medication (such as levodopa) isn't working well and your symptoms return—your doctor may prescribe additional medications specifically designed to reduce these episodes. Some **brand name medications** commonly used to manage "off" episodes include:
> 
> ### **On-demand (Rescue) Medications**
> These are taken when you feel an "off" episode coming on:
> 
> - **Inbrija®** (inhaled levodopa): An inhaled formulation of levodopa for rapid relief of "off" symptoms.
> - **Apokyn®** (apomorphine injection): An injectable dopamine agonist used as a rescue medication for sudden "off" episodes.
> - **Kynmobi®** (apomorphine sublingual film): A sublingual film that dissolves under the tongue for rapid relief.
> 
> ### **Adjunct (Add-on) Medications**
> These are taken regularly to reduce the frequency and severity of "off" episodes:
> 
> - **Comtan®** (entacapone): A COMT inhibitor, often combined with carbidopa/levodopa, to prolong levodopa's effect.
> - **Ongentys®** (opicapone): Another COMT inhibitor taken once daily.
> - **Azilect®** (rasagiline) or **Xadago®** (safinamide): MAO-B inhibitors that help extend the effect of levodopa.
> - **Gocovri®** (amantadine ER): An extended-release version of amantadine, which can help with both "off" episodes and dyskinesias.
> - **Rytary®** (carbidopa/levodopa extended-release): A longer-acting form of levodopa to provide more consistent symptom control.
> - **Stalevo®** (carbidopa/levodopa/entacapone): A combination pill to help keep levodopa levels stable.
> 
> **Note:** The **choice of medication** depends on your symptoms, other health conditions, and current medications. Always consult your neurologist or movement disorder specialist for personalized recommendations.
> 
> **Summary Table:**
> 
> | Brand Name    | Generic Name           | Type/Use                       |
> |---------------|-----------------------|--------------------------------|
> | Inbrija®      | levodopa (inhaled)    | On-demand/rescue               |
> | Apokyn®       | apomorphine (injection)| On-demand/rescue               |
> | Kynmobi®      | apomorphine (sublingual)| On-demand/rescue             |
> | Comtan®       | entacapone            | Adjunct/COMT inhibitor         |
> | Ongentys®     | opicapone             | Adjunct/COMT inhibitor         |
> | Azilect®      | rasagiline            | Adjunct/MAO-B inhibitor        |
> | Xadago®       | safinamide            | Adjunct/MAO-B inhibitor        |
> | Gocovri®      | amantadine ER         | Adjunct (dyskinesia/"off")     |
> | Rytary®       | carbidopa/levodopa ER | Extended-release levodopa      |
> | Stalevo®      | carbidopa/levodopa/entacapone | Combo/adjunct         |
> 
> **References:**
> - Parkinson's Foundation: [Managing "OFF" Episodes](https://www.parkinson.org/Understanding-Parkinsons/Managing-Parkinsons/Managing-OFF-Episodes)
> - American Academy of Neurology: [Treatment of Motor Fluctuations in Parkinson’s Disease](https://www.aan.com/Guidelines/neurology/)
> 
> If you have more specific questions, please provide your current medications, and I can tailor the answer further.
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
>   * params.target: "Nourianz"
>   * id: medication_mentioned
>   * description: "Is Nourianz mentioned?"
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
>   * params.target: "Nourianz"
>   * id: medication_position
>   * description: "Out of the drugs mentioned, what position is Nourianz mentioned in?"
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
> Inbrija®,Apokyn®,Kynmobi®,Comtan®,Ongentys®,Azilect®,Xadago®,Gocovri®,Rytary®,Stalevo®
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Nourianz mentioned?"
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
> 10
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Nourianz mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```