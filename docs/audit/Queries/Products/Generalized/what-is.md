# Query
What is {{medication}}?

# Measures
* ---
  * id: is_drug_class
  * description: "Does the answer represent {{medication}} as a {{drug_class}}?"
  * type: ai
  * prompt: "Based on the text, does the response identify {{medication}} as a {{drug_class}}? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
* ---
  * id: has_technical_name
  * description: "Is the non-branded name for {{medication}}, {{technical_name}} mentioned?"
  * type: ai
  * prompt: "Based on the text, is the name {{technical_name}} mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
* ---
  * id: has_effect
  * description: "Is it accurately presented that {{medication}} is taken to treat {{effect}}?"
  * type: ai
  * prompt: "Based on the text, is it stated that {{medication}} treats {{effect}}? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
* ---
  * id: language_approachable
  * description: "Rate how approachable the language is for a non-medical professional."
  * type: ai
  * prompt: "In the description of {{effect}}, rate how approachable the language is for a non-medical professional from 1 (very technical) to 10 (very approachable). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. "
* ---
  * id: has_company
  * description: "Is the company Kyowa mentioned?"
  * type: ai
  * prompt: "Based on the text, is the company 'Kyowa' mentioned? Your response MUST be a valid JSON object with a 'response' key containing only `true` (for Yes) or `false` (for No)."
