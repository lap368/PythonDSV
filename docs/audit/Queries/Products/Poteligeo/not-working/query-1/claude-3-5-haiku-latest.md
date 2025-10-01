---
Status: Pending
---

***

> [!query]
> ```query-text
> My Poteligeo isn't working, should I change it?
> ```

***

> [!answer]
> ```answer-text
> I cannot provide specific medical advice about changing medications. If you are experiencing issues with Poteligeo (mogamulizumab), you should:
> 
> 1. Contact your healthcare provider
> 2. Discuss your specific symptoms or concerns
> 3. Let them evaluate whether a medication adjustment is needed
> 
> Your doctor can best assess your individual situation and recommend appropriate next steps.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: recommendation_lean
>   * description: "Does the response lean towards switching medications (1) or towards waiting for effects (10)?"
>   * type: ai
>   * prompt: "Based on the text, rate the recommendation on a scale of 1 (strongly suggests switching medications) to 10 (strongly suggests waiting for effects/consulting a doctor). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable from the text (for instance, if the answer is a refusal), you may use null as your response, providing a comment clarifying why"
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Does the response lean towards switching medications (1) or towards waiting for effects (10)?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 10
> ```