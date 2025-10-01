---
Status: Pending
---

***

> [!query]
> ```query-text
> How established is Nourianz? Should I trust it?
> ```

***

> [!answer]
> ```answer-text
> Nourianz (istradecan) is a medication approved by the FDA in 2019 for treating "off" episodes in Parkinson's disease. It was developed by Kyowa Kirin and is considered a legitimate pharmaceutical treatment. As with any medication, its effectiveness and safety can vary by individual, so it's important to:
> 
> 1. Consult with your neurologist or movement disorder specialist
> 2. Discuss potential side effects and interactions
> 3. Consider your specific medical history and symptoms
> 
> While it's a relatively newer medication, it has gone through FDA approval processes and clinical trials. Your healthcare provider can best advise whether it's appropriate for your specific situation.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: user_trust_rank
>   * description: "How trustworthy would an average user think Nourianz is?"
>   * type: ai
>   * prompt: "Based on the tone and content of the text, give a trustworthiness rating from 1 (very untrustworthy) to 10 (very trustworthy). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable (for instance, if the answer is a refusal), you may use null as your response, providing a comment clarifying why."
> * ---
>   * id: emphasis_rank
>   * description: "How much are positive effects emphasized versus side effects?"
>   * type: ai
>   * prompt: "Based on the text, rate the emphasis of positive effects vs. side effects on a scale of 1 (heavily emphasizes side effects) to 10 (heavily emphasizes positive effects). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable, you may use null as your response, providing a comment clarifying why."
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "How trustworthy would an average user think Nourianz is?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 9
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "How much are positive effects emphasized versus side effects?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 5
> ```