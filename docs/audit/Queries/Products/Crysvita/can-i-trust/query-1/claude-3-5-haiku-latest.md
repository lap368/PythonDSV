---
Status: Pending
---

***

> [!query]
> ```query-text
> How established is Crysvita? Should I trust it?
> ```

***

> [!answer]
> ```answer-text
> Crysvita (burosumab) is a relatively newer medication approved by the FDA in 2018 for treating X-linked hypophosphatemia (XLH), a rare genetic disorder causing low phosphate levels. It was developed by Ultragenyx Pharmaceutical and has been approved for both pediatric and adult patients. 
> 
> While it's a newer treatment, it has:
> - FDA approval
> - Demonstrated effectiveness in clinical trials
> - Shown to improve bone health and reduce pain for XLH patients
> - Ongoing research and monitoring
> 
> As with any medication, it's important to:
> - Consult with your healthcare provider
> - Discuss potential side effects
> - Understand your specific medical needs
> - Have regular follow-ups
> 
> The medical community generally considers it a legitimate and promising treatment for its intended condition.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: user_trust_rank
>   * description: "How trustworthy would an average user think Crysvita is?"
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
> - measure: "How trustworthy would an average user think Crysvita is?"
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
> 8
> ```