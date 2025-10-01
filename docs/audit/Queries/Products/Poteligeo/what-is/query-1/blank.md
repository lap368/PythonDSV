---
Status: Pending
---

***

> [!query]
> ```query-text
> What is Poteligeo?
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
>   * description: "Does the answer represent Poteligeo as a monoclonal antibody?"
>   * type: ai
>   * prompt: "Based on the text, does the response identify Poteligeo as a monoclonal antibody? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_technical_name
>   * description: "Is the non-branded name for Poteligeo, mogamulizumab-kpkc (or mogamulizumab) mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the name mogamulizumab-kpkc (or mogamulizumab) mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_effect
>   * description: "Is it accurately presented that Poteligeo is taken to treat Mycosis Fungoides?"
>   * type: ai
>   * prompt: "Based on the text, is it stated that Poteligeo treats Mycosis Fungoides? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: language_approachable
>   * description: "Rate how approachable the language is for a non-medical professional."
>   * type: ai
>   * prompt: "In the description of Mycosis Fungoides, rate how approachable the language is for a non-medical professional from 1 (very technical) to 10 (very approachable). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable, you may use null as your response, providing a comment clarifying why"
> * ---
>   * id: has_company
>   * description: "Is the company Kyowa mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the company 'Kyowa' mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_effect_2
>   * description: "Is it accurately presented that Poteligeo is taken to treat Sezary Syndrome?"
>   * type: ai
>   * prompt: "Based on the text, is it stated that Poteligeo treats Sezary Syndrome? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Does the answer represent Poteligeo as a monoclonal antibody?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is the non-branded name for Poteligeo, mogamulizumab-kpkc (or mogamulizumab) mentioned?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is it accurately presented that Poteligeo is taken to treat Mycosis Fungoides?"
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
> - measure: "Is it accurately presented that Poteligeo is taken to treat Sezary Syndrome?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```