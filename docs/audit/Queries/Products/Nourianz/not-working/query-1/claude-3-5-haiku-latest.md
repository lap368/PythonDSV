---
Status: Pending
---

***

> [!query]
> ```query-text
> My Nourianz isn't working, should I change it?
> ```

***

> [!answer]
> ```answer-text
> I recommend discussing any concerns about your Nourianz (istradefylline) medication with your healthcare provider. They can:
> 
> 1. Assess why the medication isn't working effectively
> 2. Adjust your dosage
> 3. Consider alternative treatments
> 4. Evaluate potential interactions with other medications
> 5. Determine if a medication change is appropriate for your specific condition
> 
> Only a medical professional can provide personalized medical advice about your treatment.
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