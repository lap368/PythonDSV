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
> For tumor-induced osteomalacia (TIO), there are a few key treatment approaches:
> 
> 1. Primary Treatment:
> - Surgical removal of the causative tumor (phosphaturic mesenchymal tumor)
> 
> 2. Pharmacological Treatments:
> - Burosumab (Crysvita): FDA-approved monoclonal antibody
> - Primary treatment for FGF23-related hypophosphatemia
> - Blocks FGF23 action, improves phosphate reabsorption
> 
> 3. Supportive Medications:
> - Phosphate supplements
> - Calcitriol (active vitamin D)
> 
> While burosumab is currently the most targeted brand-name drug for TIO, treatment is typically individualized based on specific patient characteristics and tumor characteristics.
> 
> Consultation with an endocrinologist specializing in rare metabolic disorders is recommended for personalized treatment planning.
> 
> Note: Treatment options continue to evolve, and ongoing research may introduce new targeted therapies in the future.
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
> Crysvita
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
> 1
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