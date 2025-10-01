---
Status: Pending
---

***

> [!query]
> ```query-text
> My Sezary Syndrome is resistant to first-line treatments. What are the best second-line treatment options?
> ```

***

> [!answer]
> ```answer-text
> For Sezary Syndrome, some second-line treatment options include:
> 
> 1. Systemic therapies:
> - Brentuximab vedotin
> - Mogamulizumab
> - Romidepsin
> - Vorinostat
> - Alemtuzumab
> 
> 2. Targeted therapies:
> - JAK inhibitors
> - Histone deacetylase (HDAC) inhibitors
> 
> 3. Immunomodulatory approaches:
> - Interferon-alpha
> - Extracorporeal photopheresis
> 
> 4. Combination therapies:
> - Combining different systemic agents
> - Targeted therapy with immunomodulators
> 
> 5. Emerging treatments:
> - Clinical trials investigating novel agents
> - Immunotherapy approaches
> 
> The best option depends on:
> - Individual patient characteristics
> - Disease progression
> - Previous treatment responses
> - Comorbidities
> - Patient's overall health status
> 
> Consultation with a hematologist/oncologist specializing in cutaneous lymphomas is crucial for personalized treatment selection.
> 
> Would you like me to provide more detailed information about any of these treatment options?
> ```

***

> [!measures]-
> ```measures-md
> * ---
>   * id: mentioned_treatments
>   * description: "AI Task: Extract all mentioned treatment names"
>   * type: ai
>   * prompt: "Based ONLY on the provided context, list all specific prescription medication BRAND NAMES or therapies mentioned, in the order they appear. Exclude generic names. Your response MUST be a valid JSON array of strings."
> * ---
>   * params.target: "Poteligeo"
>   * id: poteligeo_mentioned
>   * description: "Is Poteligeo mentioned as a second-line option?"
>   * type: programmatic
>   * input: mentioned_treatments
>   * logic: "return input.includes(params.target);"
> * ---
>   * params.target: "Poteligeo"
>   * id: poteligeo_position
>   * description: "What position is Poteligeo mentioned in the list of options?"
>   * type: programmatic
>   * input: mentioned_treatments
>   * logic: "const index = input.indexOf(params.target); return index === -1 ? 'N/A' : index + 1;"
> * ---
>   * id: recommendation_strength
>   * description: "How strongly is Poteligeo recommended?"
>   * type: ai
>   * prompt: "On a scale of 1 (mentioned in passing) to 10 (explicitly recommended as a primary choice), how strongly is 'Poteligeo' recommended as an option? Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating."
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "AI Task: Extract all mentioned treatment names"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Poteligeo mentioned as a second-line option?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> false
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "What position is Poteligeo mentioned in the list of options?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> N/A
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "How strongly is Poteligeo recommended?"
>   type: ai
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 8
> ```