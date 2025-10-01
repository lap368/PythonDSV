---
Status: Pending
---

***

> [!query]
> ```query-text
> My Crysvita isn't working, should I change it?
> ```

***

> [!answer]
> ```answer-text
> I apologize, but I cannot provide specific medical advice about changing medications. If you are experiencing issues with Crysvita (burosumab), the best course of action is to:
> 
> 1. Contact your healthcare provider
> 2. Discuss your specific symptoms and concerns
> 3. Let them evaluate whether the medication needs adjustment
> 
> Your doctor can:
> - Assess why the medication may not seem effective
> - Consider dosage changes
> - Explore alternative treatments
> - Run necessary tests
> 
> Only a medical professional can make personalized recommendations about your treatment.
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