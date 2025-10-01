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
> **Poteligeo** (generic name: *mogamulizumab*) is a prescription medicine that was approved by the U.S. Food and Drug Administration (FDA) in **August 2018**. It is a monoclonal antibody used to treat certain rare types of blood cancer: **mycosis fungoides (MF)** and **Sézary syndrome (SS)**, which are types of cutaneous T-cell lymphoma (CTCL), in patients who have had at least one prior systemic therapy.
> 
> ### How Established Is Poteligeo?
> 
> - **FDA Approval:** Poteligeo is FDA-approved, meaning it has undergone rigorous clinical trials to demonstrate safety and efficacy for its approved uses.
> - **Years on Market:** As of 2024, it has been used in clinical practice in the US for about 6 years and has been available in Japan since 2012.
> - **Guideline Inclusion:** It is included in treatment guidelines (such as those by the National Comprehensive Cancer Network, NCCN) for CTCL.
> - **Clinical Evidence:** The approval was based on the pivotal MAVORIC trial, which showed that Poteligeo improved progression-free survival compared to vorinostat in patients with relapsed/refractory MF or SS.
> - **Real-World Use:** Since approval, Poteligeo has been used in clinical practice internationally, and longer-term real-world data continue to accumulate.
> 
> ### Should You Trust It?
> 
> - **Efficacy:** Clinical trials and real-world experience support its effectiveness, particularly in the challenging setting of relapsed or refractory MF and SS.
> - **Safety:** The side effect profile is well-characterized, with the most common side effects including rash, infusion reactions, and infections. Serious, but less common, side effects can occur, and it is important to be monitored by a healthcare professional.
> - **Expert Endorsement:** It is recommended by hematology and oncology experts for appropriate patients.
> 
> ### Things To Consider
> 
> - **Not for everyone:** Poteligeo is specifically for certain types of CTCL, and is usually used after other therapies have failed.
> - **Individual Response:** Like all cancer medications, response varies, and the risks, benefits, and alternatives should be discussed with your oncologist.
> - **Ongoing Monitoring:** As with newer therapies, ongoing post-marketing surveillance is in place, and your healthcare team will stay up to date with the latest information.
> 
> ---
> 
> **Summary:**  
> Poteligeo is a well-established, FDA-approved, and guideline-recommended therapy for certain types of cutaneous T-cell lymphoma. If it is being considered for you, it is reasonable to trust its safety and efficacy, as supported by current clinical evidence, but always discuss your specific situation, potential side effects, and alternative treatments with your doctor.
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
> 8
> ```