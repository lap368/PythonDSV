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
> I'm sorry to hear that you're concerned about your Crysvita (burosumab) treatment. Crysvita is a medication often used to treat X-linked hypophosphatemia (XLH) and some other rare conditions affecting phosphate metabolism.
> 
> **If you feel that Crysvita isn't working as expected, here are some important steps:**
> 
> 1. **Do Not Stop or Change Medication on Your Own:**  
>    Never stop or change the dose of Crysvita without talking to your healthcare provider.
> 
> 2. **Assess What "Not Working" Means:**  
>    - Are you experiencing continued symptoms?
>    - Are your phosphate levels not improving on lab tests?
>    - Are you having new or worsening side effects?
> 
> 3. **Track Your Symptoms and Results:**  
>    - Keep a record of your symptoms, lab results, and any side effects.
>    - Note any changes since starting treatment.
> 
> 4. **Talk to Your Healthcare Provider Promptly:**  
>    - Share your concerns and your records with your doctor.
>    - Your provider might adjust your dose, check your labs, or consider other causes for your symptoms.
> 
> 5. **Other Considerations:**  
>    - Sometimes it takes time to see the benefits of Crysvita.
>    - Other factors (diet, other medications, new health issues) can affect your response.
> 
> **Bottom line:**  
> **Do not make any changes to your treatment without consulting your doctor.** Only your healthcare provider can determine if a change in medication, dose, or approach is needed.
> 
> If you are experiencing severe or new side effects, or your symptoms are rapidly worsening, contact your healthcare provider urgently.
> 
> Would you like more specific advice about your symptoms or lab results? If you share more details, I can provide more tailored information (but this is not a substitute for your doctor's advice).
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