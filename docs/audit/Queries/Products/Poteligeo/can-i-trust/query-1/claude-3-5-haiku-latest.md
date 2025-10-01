---
Status: Pending
---

***

> [!query]
> ```query-text
> How established is Poteligeo? Should I trust it?
> ```

***

> [!answer]
> ```answer-text
> Poteligeo (mogamulizumab) is an FDA-approved medication specifically for treating certain types of cutaneous T-cell lymphoma (CTCL). It was approved by the FDA in 2018 for adult patients with mycosis fungoides (MF) or Sézary syndrome who have received at least one prior systemic therapy. 
> 
> The drug is manufactured by Kyowa Kirin and has gone through clinical trials to demonstrate its safety and efficacy. As with any medication, its use should be discussed thoroughly with a healthcare professional who can evaluate its appropriateness for a specific patient's condition.
> 
> While it is an established treatment option for these specific lymphoma types, like all medications, individual experiences and responses can vary. A healthcare provider can provide the most personalized guidance about its use, potential benefits, and side effects.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: user_trust_rank
>   * description: "How trustworthy would an average user think Poteligeo is?"
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
> - measure: "How trustworthy would an average user think Poteligeo is?"
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
> 6
> ```