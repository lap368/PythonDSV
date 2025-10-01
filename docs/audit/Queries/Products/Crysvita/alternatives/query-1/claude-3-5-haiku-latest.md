---
Status: Pending
---

***

> [!query]
> ```query-text
> What are some available brand name alternatives to Dojolvi ?
> ```

***

> [!answer]
> ```answer-text
> Dojolvi (triheptanoin) is a medication used to treat long-chain fatty acid oxidation disorders (LC-FAOD). As of my current knowledge, there are no direct brand name alternatives to Dojolvi on the market. Dojolvi is a relatively new treatment specifically approved for this rare condition.
> 
> If you're looking for alternative treatments or management strategies for LC-FAOD, it's best to consult with a healthcare professional who can provide personalized medical advice based on an individual's specific condition and needs.
> 
> For the most up-to-date information on available treatments, I recommend speaking with a medical specialist or checking with recent medical resources.
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
>   * description: "Is Crysvita mentioned by name?"
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
>   * params.target: "Crysvita"
>   * id: medication_position
>   * description: "Out of the drugs mentioned by name, what number in the order is Crysvita?"
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
> Dojolvi
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Crysvita mentioned by name?"
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
> 1
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Out of the drugs mentioned by name, what number in the order is Crysvita?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```