---
Status: Pending
---

***

> [!query]
> ```query-text
> What is Nourianz?
> ```

***

> [!answer]
> ```answer-text
> Nourianz (istradefylline) is a prescription medication used to treat Parkinson's disease. It is an oral medication that helps reduce "off" episodes in patients who are already taking levodopa/carbidopa. An "off" episode is when Parkinson's medication stops working effectively, and motor symptoms like tremors, stiffness, and slowness of movement return. Nourianz works by targeting a different mechanism in the brain compared to other Parkinson's medications, specifically by blocking adenosine A2A receptors. It was approved by the FDA in 2019 and is manufactured by Kyowa Kirin.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: is_drug_class
>   * description: "Does the answer represent Nourianz as a adenosine receptor antagonist?"
>   * type: ai
>   * prompt: "Based on the text, does the response identify Nourianz as a adenosine receptor antagonist? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_technical_name
>   * description: "Is the non-branded name for Nourianz, istradefylline mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the name istradefylline mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_effect
>   * description: "Is it accurately presented that Nourianz is taken to treat "off" episodes in Parkinson's disease?"
>   * type: ai
>   * prompt: "Based on the text, is it stated that Nourianz treats "off" episodes in Parkinson's disease? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: language_approachable
>   * description: "Rate how approachable the language is for a non-medical professional."
>   * type: ai
>   * prompt: "In the description of "off" episodes in Parkinson's disease, rate how approachable the language is for a non-medical professional from 1 (very technical) to 10 (very approachable). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable, you may use null as your response, providing a comment clarifying why"
> * ---
>   * id: has_company
>   * description: "Is the company Kyowa mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the company 'Kyowa' mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Does the answer represent Nourianz as a adenosine receptor antagonist?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is the non-branded name for Nourianz, istradefylline mentioned?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is it accurately presented that Nourianz is taken to treat "off" episodes in Parkinson's disease?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Rate how approachable the language is for a non-medical professional."
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 8
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is the company Kyowa mentioned?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> false
> ```