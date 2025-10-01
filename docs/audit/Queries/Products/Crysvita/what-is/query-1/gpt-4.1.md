---
Status: Pending
---

***

> [!query]
> ```query-text
> What is Crysvita?
> ```

***

> [!answer]
> ```answer-text
> **Crysvita** is the brand name for **burosumab**, a prescription medication used to treat **X-linked hypophosphatemia (XLH)** and certain other rare conditions that cause low phosphate levels in the blood.
> 
> ### What is Crysvita used for?
> - **X-linked hypophosphatemia (XLH):** A rare inherited disorder that causes low phosphate levels, leading to soft, weak bones (rickets or osteomalacia), bone pain, and growth problems.
> - **Tumor-induced osteomalacia (TIO):** In some cases, Crysvita is used to treat adults with TIO, a rare disease caused by certain tumors that lower phosphate levels.
> 
> ### How does Crysvita work?
> Crysvita is a **monoclonal antibody** that binds to and inhibits a protein called **fibroblast growth factor 23 (FGF23)**. FGF23 is responsible for reducing phosphate reabsorption in the kidneys and lowering vitamin D production. By blocking FGF23, Crysvita increases blood phosphate and active vitamin D levels, helping to improve bone mineralization and strength.
> 
> ### How is Crysvita given?
> Crysvita is given as a **subcutaneous (under the skin) injection**, usually every two or four weeks, depending on the patient’s age and condition. Dosage and administration are determined by a healthcare professional.
> 
> ### What are common side effects?
> Some possible side effects include:
> - Injection site reactions (redness, swelling, pain)
> - Headache
> - Muscle pain
> - Nausea
> - Tooth abscess (especially in children)
> - Increased blood phosphate (hyperphosphatemia)
> 
> ### Important information
> Crysvita should only be used under the supervision of a healthcare provider experienced in treating rare bone disorders. Regular blood tests are necessary to monitor phosphate and calcium levels.
> 
> ---
> 
> **In summary:**  
> Crysvita (burosumab) is a medication for certain rare diseases that cause low phosphate in the blood, helping to strengthen bones and improve symptoms.
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: is_drug_class
>   * description: "Does the answer represent Crysvita as a monoclonal antibody?"
>   * type: ai
>   * prompt: "Based on the text, does the response identify Crysvita as a monoclonal antibody? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_technical_name
>   * description: "Is the non-branded name for Crysvita, burosumab (or burosumab-twza) mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the name burosumab (or burosumab-twza) mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_effect
>   * description: "Is it accurately presented that Crysvita is taken to treat X-linked hypophosphatemia (XLH)?"
>   * type: ai
>   * prompt: "Based on the text, is it stated that Crysvita treats X-linked hypophosphatemia (XLH)? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: language_approachable
>   * description: "Rate how approachable the language is for a non-medical professional."
>   * type: ai
>   * prompt: "In the description of X-linked hypophosphatemia (XLH), rate how approachable the language is for a non-medical professional from 1 (very technical) to 10 (very approachable). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable, you may use null as your response, providing a comment clarifying why"
> * ---
>   * id: has_company
>   * description: "Is the company Kyowa mentioned?"
>   * type: ai
>   * prompt: "Based on the text, is the company 'Kyowa' mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> * ---
>   * id: has_effect_2
>   * description: "Is it accurately presented that Crysvita is taken to treat tumor-induced osteomalacia (TIO)?"
>   * type: ai
>   * prompt: "Based on the text, is it stated that Crysvita treats tumor-induced osteomalacia (TIO)? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Does the answer represent Crysvita as a monoclonal antibody?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is the non-branded name for Crysvita, burosumab (or burosumab-twza) mentioned?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is it accurately presented that Crysvita is taken to treat X-linked hypophosphatemia (XLH)?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Rate how approachable the language is for a non-medical professional."
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 8
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is the company Kyowa mentioned?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> false
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is it accurately presented that Crysvita is taken to treat tumor-induced osteomalacia (TIO)?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```