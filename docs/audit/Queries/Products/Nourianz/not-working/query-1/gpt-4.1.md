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
> I'm sorry to hear you're having trouble with Nourianz (istradefylline). Whether you should change your medication depends on several factors, including why you feel Nourianz "isn't working," what symptoms you're experiencing, and your overall treatment plan.
> 
> **A few important points:**
> - **Nourianz** is used as an add-on treatment for Parkinson’s disease, specifically to help with "off" episodes (times when your usual medication isn’t working well).
> - If you aren't seeing benefit, or if symptoms have worsened, this could be due to disease progression, medication interactions, dosing issues, or other factors.
> 
> **What to do next:**
> 1. **Don’t stop Nourianz abruptly** without consulting your neurologist, as this could worsen symptoms.
> 2. **Track your symptoms:** Write down when you take your medications, what symptoms you have, and when you have "off" periods. This information can help your doctor.
> 3. **Contact your neurologist:** They can assess your medication regimen, consider adjusting the dose, switching medications, or adding other therapies. Sometimes, benefit from Nourianz may take a few weeks, or adjustments may be needed.
> 
> **Do not change, stop, or add medications on your own.** Parkinson’s treatment is complex, and changes should be guided by your healthcare provider.
> 
> **If you have serious symptoms** (such as severe worsening, inability to move, or new, concerning symptoms), seek medical attention immediately.
> 
> Would you like more information on common reasons Nourianz may not work, or tips for tracking your symptoms to discuss with your doctor?
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
> 9
> ```