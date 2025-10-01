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
> I'm sorry to hear that Poteligeo (mogamulizumab) isn't working as hoped. This medication is used for certain types of cutaneous T-cell lymphomas like mycosis fungoides and Sézary syndrome. The decision to change treatments is complex and depends on several factors, including:
> 
> - **How long you've been on Poteligeo:** Sometimes it takes a few months to see a response.
> - **How your disease is progressing:** Is it stable, getting worse, or causing new symptoms?
> - **Previous therapies tried and your overall health.**
> - **Side effects or tolerability issues.**
> 
> **What to do:**
> - **Contact your oncologist/hematologist** as soon as possible. They will evaluate your response (physical exams, blood tests, skin assessments, etc.) and discuss other options.
> - **Alternative treatments** may include other systemic therapies (e.g., brentuximab vedotin, interferon, bexarotene, chemotherapy, extracorporeal photopheresis, or clinical trials).
> 
> **Don't stop or change your medication without your doctor's guidance.** Your doctor is the best person to help you decide on the next step based on your unique situation.
> 
> If you’d like, I can provide general information about alternative treatments, but I can’t give personalized medical advice. Would you like more information?
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