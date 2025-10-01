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
> For tumor-induced osteomalacia (TIO), treatment typically involves addressing the underlying cause and managing phosphate and vitamin D metabolism. While I can't definitively state specific brand name medications, common treatments may include:
> 
> 1. Phosphate supplements
> - Possible brand names: Phospha 250 Neutral, Neutra-Phos
> 
> 2. Calcitriol (active vitamin D)
> - Brand names: Rocaltrol, Calcijex
> 
> 3. Surgical removal of the causative tumor when possible
> 
> 4. In cases where surgical removal is not feasible, targeted medical therapies might include:
> - Burosumab (Crysvita) - a monoclonal antibody specifically approved for X-linked hypophosphatemia, which has similar metabolic characteristics to TIO
> 
> The exact prescription would depend on:
> - Individual patient characteristics
> - Specific tumor location
> - Severity of phosphate wasting
> - Patient's overall health status
> 
> A medical professional would determine the most appropriate treatment plan based on comprehensive evaluation and diagnostic results. Always consult with an endocrinologist or specialist familiar with rare metabolic disorders for personalized medical advice.
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
> Phospha 250 Neutral,Neutra-Phos,Rocaltrol,Calcijex,Crysvita
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
> 5
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned, what position is Crysvita mentioned in?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 5
> ```