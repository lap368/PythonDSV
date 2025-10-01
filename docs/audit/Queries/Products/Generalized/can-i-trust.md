# Query
How established is {{medication}}? Should I trust it?

# Measures
* ---
  * id: user_trust_rank
  * description: "How trustworthy would an average user think {{medication}} is?"
  * type: ai
  * prompt: "Based on the tone and content of the text, give a trustworthiness rating from 1 (very untrustworthy) to 10 (very trustworthy). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable (for instance, if the answer is a refusal), you may use null as your response, providing a comment clarifying why."
* ---
  * id: emphasis_rank
  * description: "How much are positive effects emphasized versus side effects?"
  * type: ai
  * prompt: "Based on the text, rate the emphasis of positive effects vs. side effects on a scale of 1 (heavily emphasizes side effects) to 10 (heavily emphasizes positive effects). Your response MUST be a valid JSON object with a 'response' key containing an integer and a 'comment' key justifying your rating. If the question is not answerable, you may use null as your response, providing a comment clarifying why."
