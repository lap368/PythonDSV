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
> **Crysvita** (burosumab) is a **prescription medication** used primarily to treat **X-linked hypophosphatemia (XLH)** and certain cases of **tumor-induced osteomalacia (TIO)**, both rare disorders that affect phosphate metabolism and bone health.
> 
> ### How Established Is Crysvita?
> - **Approval Status:**  
>   - **FDA-approved:** First approved in the United States in 2018 for XLH in both children and adults.
>   - **EMA-approved:** Also approved by the European Medicines Agency.
> - **Guidelines:** Included in clinical guidelines as a treatment for XLH.
> - **Studies:**  
>   - Multiple **clinical trials** have shown that Crysvita improves phosphate levels, bone health, and physical function in XLH.
>   - Long-term data (several years) indicate continued effectiveness and a generally acceptable safety profile.
> - **Use:**  
>   - Widely prescribed and used in the US, Europe, and other regions.
>   - Considered a **standard of care** for XLH in many settings.
> 
> ### Should You Trust Crysvita?
> - **Efficacy:**  
>   - Proven to increase phosphate levels and improve rickets and bone pain in children and adults with XLH.
>   - Reduces the need for conventional therapy (phosphate and vitamin D supplements).
> - **Safety:**  
>   - **Common side effects** include injection site reactions, headache, and sometimes increased phosphate in the blood.
>   - **Serious side effects** (rare) may include hypersensitivity or ectopic calcification (calcium deposits in soft tissues).
>   - **Regular monitoring** is required during treatment.
> - **Expert Supervision:**  
>   - **Only to be used under the supervision of a specialist** (endocrinologist, metabolic bone disease expert, or geneticist).
>   - Not appropriate for all phosphate or bone disorders.
> 
> ### Summary Table
> 
> | Aspect           | Details                                                                                    |
> |------------------|-------------------------------------------------------------------------------------------|
> | **Approval**     | FDA and EMA approved (since 2018)                                                         |
> | **Indications**  | XLH (children and adults), TIO (ineligible for surgery)                                   |
> | **Evidence**     | Strong, from multiple clinical trials and years of real-world use                          |
> | **Safety**       | Generally well-tolerated, side effects and labs must be monitored by a specialist          |
> | **Trust**        | Considered **standard of care** for XLH, **trustworthy** when prescribed and monitored     |
> 
> ---
> 
> **Bottom line:**  
> **Crysvita is a well-established, trusted, and effective therapy** for XLH and certain TIO cases **when prescribed and monitored by a qualified specialist**. If you are a candidate, **ask your doctor** for more information and discuss the **risks and benefits** in your specific situation.
> 
> **If you have a specific diagnosis, age, or concern, share more details and I can tailor the information for you.**
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