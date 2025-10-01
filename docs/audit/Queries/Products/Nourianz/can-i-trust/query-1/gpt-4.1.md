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
> **Nourianz** (generic name: **istradefylline**) is an FDA-approved medication used **as an add-on treatment to levodopa/carbidopa in adults with Parkinson’s disease experiencing “off” episodes** (periods when medication isn’t working well and symptoms return).
> 
> ### How Established is Nourianz?
> 
> - **FDA Approval:** Nourianz was approved by the U.S. FDA in **August 2019**. While this makes it a relatively recent addition compared to long-standing Parkinson’s drugs, it is not “brand new.”
> - **Global Use:** Istradefylline has been used in Japan since 2013 under the brand name **Nouriast**.
> - **Studies:** Its effectiveness and safety have been demonstrated in multiple **clinical trials** involving thousands of patients. These studies showed that Nourianz can reduce “off” time without significantly increasing troublesome side effects.
> - **Guidelines:** Nourianz is included in some professional guidelines as an option for managing “off” episodes in Parkinson’s disease.
> 
> ### Should You Trust Nourianz?
> 
> - **Safety:** The safety profile is well-characterized, with the most common side effects including dyskinesia (involuntary movement), dizziness, constipation, nausea, and hallucinations.
> - **Long-Term Data:** While long-term, real-world experience in the U.S. is still accumulating, its use in Japan provides additional reassurance.
> - **Prescribing:** It should only be used **under the supervision of a healthcare provider** who can assess if it’s suitable for you, given your specific situation and other medications.
> 
> ### Bottom Line
> 
> - **Nourianz is a legitimate, FDA-approved option for specific Parkinson’s symptoms.**
> - It is not experimental, but is newer than some other Parkinson’s drugs.
> - It is generally considered safe and effective **when prescribed appropriately**.
> 
> **Always consult your neurologist or movement disorder specialist to discuss if Nourianz is right for you.** Let them know about all your medications and medical history so they can weigh the potential benefits and risks for your case.
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
> 7
> ```