---
Status: Pending
---

***

> [!query]
> ```query-text
> What is Crysvita?
> ```

***

> [!answer]
> ```answer-text
> 
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: is_drug_class
>   * description: "Does the answer represent Crysvita as a monoclonal antibody?"
>   * type: ai
>   * prompt: "Based on the text, does the response identify Crysvita as a monoclonal antibody? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_technical_name
>   * description: "Is the non-branded name for Crysvita, burosumab (or burosumab-twza) mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the name burosumab (or burosumab-twza) mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_effect
>   * description: "Is it accurately presented that Crysvita is taken to treat X-linked hypophosphatemia (XLH)?"
>   * type: ai
>   * prompt: "Based on the text, is it stated that Crysvita treats X-linked hypophosphatemia (XLH)? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: language_approachable
>   * description: "Rate how approachable the language is for a non-medical professional."
>   * type: ai
>   * prompt: "In the description of X-linked hypophosphatemia (XLH), rate how approachable the language is for a non-medical professional from 1 (very technical) to 10 (very approachable). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable, you may use null as your response, providing a comment clarifying why"
> * ---
>   * id: has_company
>   * description: "Is the company Kyowa mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the company 'Kyowa' mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_effect_2
>   * description: "Is it accurately presented that Crysvita is taken to treat tumor-induced osteomalacia (TIO)?"
>   * type: ai
>   * prompt: "Based on the text, is it stated that Crysvita treats tumor-induced osteomalacia (TIO)? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Does the answer represent Crysvita as a monoclonal antibody?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is the non-branded name for Crysvita, burosumab (or burosumab-twza) mentioned?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is it accurately presented that Crysvita is taken to treat X-linked hypophosphatemia (XLH)?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Rate how approachable the language is for a non-medical professional."
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is the company Kyowa mentioned?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is it accurately presented that Crysvita is taken to treat tumor-induced osteomalacia (TIO)?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```