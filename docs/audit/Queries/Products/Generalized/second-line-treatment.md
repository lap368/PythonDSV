# Query
My {{effect}} is resistant to first-line treatments. What are the best second-line treatment options?

# Measures
* ---
  * id: mentioned_treatments
  * description: "AI Task: Extract all mentioned treatment names"
  * type: ai
  * prompt: "Based ONLY on the provided context, list all specific prescription medication BRAND NAMES or therapies mentioned, in the order they appear. Exclude generic names. Your response MUST be a valid JSON array of strings."
* ---
  * id: poteligeo_mentioned
  * description: "Is Poteligeo mentioned as a second-line option?"
  * type: programmatic
  * input: mentioned_treatments
  * params.target: "Poteligeo"
  * logic: "return input.includes(params.target);"
* ---
  * id: poteligeo_position
  * description: "What position is Poteligeo mentioned in the list of options?"
  * type: programmatic
  * input: mentioned_treatments
  * params.target: "Poteligeo"
  * logic: "const index = input.indexOf(params.target); return index === -1 ? 'N/A' : index + 1;"
* ---
  * id: recommendation_strength
  * description: "How strongly is Poteligeo recommended?"
  * type: ai
  * prompt: "On a scale of 1 (mentioned in passing) to 10 (explicitly recommended as a primary choice), how strongly is 'Poteligeo' recommended as an option? Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating."