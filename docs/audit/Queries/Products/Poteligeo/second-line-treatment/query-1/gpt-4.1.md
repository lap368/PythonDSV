---
Status: Pending
---

***

> [!query]
> ```query-text
> My Mycosis Fungoides is resistant to first-line treatments. What are the best second-line treatment options?
> ```

***

> [!answer]
> ```answer-text
> I'm sorry to hear about your situation. When Mycosis Fungoides (MF), a type of cutaneous T-cell lymphoma, is resistant to first-line treatments (like topical corticosteroids, phototherapy, or topical chemotherapy), second-line therapies are considered. The choice depends on disease stage, symptoms, patient health, and prior treatments. Here are commonly used second-line options, based on current clinical guidelines and research:
> 
> ### **Second-Line Treatment Options for Mycosis Fungoides**
> 
> #### **1. Systemic Therapies**
> - **Retinoids** (e.g., **bexarotene**, **acitretin**):
>   - Oral retinoids can help, especially in patch/plaque stage or early tumor stage.
> - **Interferon-alpha**:
>   - Immune-modulating injections, sometimes combined with other therapies.
> - **Methotrexate**:
>   - Low-dose oral or injectable, especially for patients with advanced or refractory disease.
> - **HDAC inhibitors** (e.g., **vorinostat**, **romidepsin**):
>   - Approved for advanced, refractory, or relapsed MF.
> - **Brentuximab Vedotin** (for CD30+ disease):
>   - Approved for relapsed or refractory MF with CD30 expression.
> - **Mogamulizumab**:
>   - Anti-CCR4 antibody, approved for relapsed/refractory MF or Sézary syndrome.
> 
> #### **2. Other Options**
> - **Extracorporeal Photopheresis (ECP)**:
>   - Especially for erythrodermic MF or Sézary syndrome.
> - **Chemotherapy**:
>   - **Single-agent** (e.g., **gemcitabine**, **liposomal doxorubicin**).
>   - **Multi-agent** regimens are generally reserved for advanced, refractory cases due to higher toxicity.
> - **Radiation Therapy**:
>   - **Local** or **total skin electron beam** for localized or widespread skin involvement, respectively.
> 
> #### **3. Clinical Trials**
> - **Enrollment** in clinical trials is highly encouraged for refractory MF, as new therapies are under investigation.
> 
> ---
> 
> **Important notes:**
> - **Treatment is highly individualized**. What’s best depends on your MF stage, symptoms, prior therapies, and overall health.
> - **Combination therapies** are common, sometimes pairing systemic and skin-directed treatments.
> - **Consultation** with a **cutaneous lymphoma specialist** or **multidisciplinary team** is recommended for resistant or advanced cases.
> 
> **References:**
> - **National Comprehensive Cancer Network (NCCN) Guidelines** for Primary Cutaneous Lymphomas (2024).
> - **UpToDate**: Treatment of mycosis fungoides (MF) and Sézary syndrome.
> - **European Society for Medical Oncology (ESMO) Clinical Practice Guidelines** (2023).
> 
> **Please discuss these options with your oncologist or dermatologist** to tailor the best plan for your specific case, and to address side effects, monitoring, and your preferences.
> 
> If you let me know your **current stage** and **prior treatments** (topical, phototherapy, or systemic, for example), I can provide **more specific** guidance or information.
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
> Targretin,Istodax,Adcetris,Poteligeo
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "Is Poteligeo mentioned as a second-line option?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> true
> ```

***

> [!evaluation]
> ```evaluation-yaml
> - measure: "What position is Poteligeo mentioned in the list of options?"
>   type: programmatic
> ```

> [!evaluation-result]
> ```evaluation-result-text
> 4
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