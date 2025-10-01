# Categories
## Semantic Web Basics
### Are they notating semantic web at all?

### What are they using?
RDFa, JSON-LD?

### What ontologies exist in their space?
#### How widely are they used, particularly by other businesses at their level, particularly particularly known competitors?
If everyone else is using them - you're behind!
If ontologies exist but are underutilized - you have a chance to get ahead!

#### Is this business using them correctly?
Both in terms of using them as directed by the ontology and in terms of using them across all relevant page types.

## GEO Reach
The basic concept of the GEO reach metric reading is to get a sense of whether different chat bots will bring the business up when related queries are made. A battery of questions will be supplied to a number of different chatbots, and their answers will be graded in terms of whether they brought up the company, the specific product, whether everything was represented correctly, etc.

### Steps in generating GEO Reach Scoring
#### 1. Identify customer types
Specify types of people who we want to be pulled into the site via generative engine answers. For example, for a pharma site we want to get mentioned to patients and doctors alike.

#### 2. Identify question areas 
Identify what topics people may be asking about. May be specific to one persona, may be cross-persona. For a pharma company, question areas may include medications, company reputation, careers, recent news. 

#### 3. Make base-prompt mad-libs
For each question area, identify the core "blank"(s) that can be used to generate wide swaths of questions relevant to. For a medication question area, a core blank may be "medication", which would allow us to make questions of the form "How safe is {medication}?" or "What ingredients are in {medication}?". Make lists of the possible fill-ins for each of the blanks, and lists of questions using those blanks.

#### 4. Create realistic questions at various specificity levels
Populate all of the base-prompt mad-libs with all possible fill-ins for the blanks, then generate more specific and natural questions, targeting each of the following levels of knowledge/prodding for relevant personas:

1. **No Knowledge/Prodding**
	Questions with this level should be questions that would be asked by someone with no particular knowledge in the question area. It's important to note here that "no-knowledge" refers to the imagined state of the user asking the question, not the knowledge required to formulate the question. This is better illustrated with an example:

	**Example**: Given the base-prompt mad-lib "How does {medication} work?", with medication = Crysvita and persona of a patient, a no-knowledge/prodding question may be "How to treat low phosphorous".  While the knowledge "Crysvita treats low phosphorous" is required for the question-writer to write this question, the imagined patient does not know this piece of information.

	Another thing illustrated by this example is that most no knowledge/prodding questions should not directly reference the business or any of their specific products/fill-ins for a blank. A person with no knowledge is often going to be seeking out broad knowledge and our main goal with them is to make sure we are portrayed, portrayed accurately, and portrayed in a positive light.

	**Note**: We can imagine that the creation of questions which omit the fill-in may result in overlap in questions generated; for example, if Kyowa Krin had two medications that treated low phosphorous, we may wind up generating a variation on "How to treat low phosphorous" for each. We will need to come up with processes to mitigate this.

	**PRIMARY TARGET:** Being brought up 
	**Secondary Target**: Accuracy


2. **Field-Familiar Knowledge/Prodding**
	These are questions made by someone who is familiar with the concepts and language of the question area. Questions should be more specific and discerning, and may mention the brand or product, but usually not in isolation.

	A doctor in a separate discipline would generally ask questions falling into this category, as would a patient who has been dealing with a related condition for some time.

	**PRIMARY TARGET**: Accuracy
	**Secondary Target**: Positive comparison to competitors 


3. **Field Expert Knowledge/Prodding**
	These are highly specific questions asked about a particular product/topic by someone who is directly familiar with it and seeking out a specific piece of information.

	**PRIMARY TARGET**: Accuracy
	**Secondary Target**: Positive portrayal in isolation

