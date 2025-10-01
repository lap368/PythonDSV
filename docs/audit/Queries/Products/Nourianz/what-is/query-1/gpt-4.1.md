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
> **Nourianz** is the brand name for **istradefylline**, a prescription medication used in the treatment of Parkinson’s disease. Specifically, it is approved as an **add-on therapy to levodopa/carbidopa** in adult patients who are experiencing "off" episodes (periods when medication is not working well and symptoms such as tremor and stiffness return).
> 
> **Key points about Nourianz (istradefylline):**
> 
> - **Mechanism of Action:** Nourianz is an **adenosine A2A receptor antagonist**. By blocking these specific receptors in the brain, it helps reduce the "off" time in patients with Parkinson’s disease.
> - **Use:** It is used **in combination with levodopa/carbidopa**, not as a replacement for those medications.
> - **Dosage:** Typically taken once daily, with or without food.
> - **Common Side Effects:** May include dyskinesia (involuntary movements), dizziness, constipation, hallucinations, and insomnia.
> 
> **Important Notes:**
> - Nourianz does **not treat Parkinson’s disease by itself**; it improves the effectiveness of levodopa/carbidopa.
> - It should be used under the supervision of a healthcare provider, as it may interact with other medications and has specific dosing adjustments in certain populations.
> 
> **Summary:**  
> **Nourianz (istradefylline)** is a medication used to help manage "off" episodes in people with Parkinson’s disease who are already taking levodopa/carbidopa. It works by blocking adenosine A2A receptors in the brain, thereby improving movement symptoms during "off" periods.
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