Takeaways from the audit of Kyowa
# Part 1. AI Messaging
## Process
We created a set of the most pressing questions patients and prescribers want to know about your drugs and the conditions they treat. We then [[AuditReport2025-10-01|asked those questions]]  to two of the most popular AI chat bots in the world, ChatGPT and Claude, and gauged how much of an advocate they were or were not for your product. 

## What we found
Overall, the story these messages spell out is that AI agents **do not know you as well as they should**. 

### Nourianz
Nourianz does not get brought up nearly enough. When asked about treating off episodes in Parkinson's, the models brought up 8 medications on average, yet only named Nourianz in one of the four scenarios, where it was named fifth out of five.  Even worse, neither model brings up Nourianz as a potential alternative to either Ongentys or Kynmobi.

### Crysvita
Crysvita is your success story. It consistently was brought up as the only way to treat XLH and TIO and was always referred to by its brand name. In two cases, the model brought up the company name, Kyowa Kirin, something we otherwise only saw when asking directly about any of the drugs by name. In another, while it was being asked about treatment for TIO, it, un-prompted, brought up that Crysvita also treats XLH. Clearly, the AI agents have an excellent understanding of Crysvita, and it offers us a look at how an AI agent being familiar with one part of your business lifts up how much they will talk about you and advocate for you.

### Potelegio
Potelegio is a mixed bag. While it does get brought up in 3 of 4 cases asking about treatment for Mycosis Fungoides, in all of them it is mentioned only very briefly. When asked about second-line treatment options for MF and for Sezary Syndrome, repeatedly we saw mogamulizumab get brought up, without any mention of Potelegio by name, despite Potelegio being the only mogamulizumab available. That corner on the market should let you get the same advantage that being the only treatment for XLH and TIO gave you with Crysvita; we would love to see Potelegio and Kyowa Kirnin get brought up every single time someone asks about second-line treatment for MF and SS.

### Overall
Kyowa is positioned very well to become a major player in GEO. You have two products which are each unique in their respective treatments, and the models seem to be "familiar with your work" but aren't yet the cheerleaders that we'd like them to be. 

# Part 2. Semantic Web
So, how do we get the AI to vouch for you? We get it to trust you. And how do we get it to trust you? We get it to understand you. And your number one tool for helping AI models to understand you is the semantic web. Unfortunately, your presence in the semantic web is fairly lacking.

## www.kyowakirin.com - A black hole
This top level parent site has absolutely no semantic web annotations whatsoever. It is extremely important in gathering agent trust that you consistently use semantic web content across all points where you are discussing your business or your product. This site having no JSON-LD whatsoever, when it has the opportunity to be a linking hub for all of its child sites, is a massive missed opportunity.

## www.kkna.kyowakirin.com (homepage)  - Non-representative
The JSON-LD present on the homepage, while welcome, is not nearly as comprehensive as it should be, and does not feel representative of what your company is putting forward with this brand. Listed under its MedicalOrganization are three brands, POTELLIGENT, COMPLEGENT, and AccretaMab; none of which are discussed on this site, but on the separate BioWa site (https://www.kyowakirin.com/biowa/index.html). Meanwhile, this brand's three medications, Poteligeo, Nourianz, and Crysvita are not linked in the semantic web at all, despite detailed schema existing for annotating drugs. 

## www.kkna.kyowakirin.com/what-we-do/our-medicines/#medicines Medicines page - Out of date
This page's semantic web content links it to two drugs that Kyowa no longer creates, SANCUSO and FARESTON. This is especially egregious in the case of Sancuso, as that medication is still in production, but from a different company; meaning that this page is misrepresenting the truth, which will lower the site's credibility.

## Prescribing Information Pages - Missed Opportunity
The prescribing information pages would be the perfect place to include thorough annotation of everything about your drugs from their dosage to their interactions via the https://schema.org/Drug schema. Unfortunately, the prescribing information pages are not, in reality, a page, but statically hosted pdfs with no ability to be annotated at all. Furthermore, these pages will rarely be surfaced by search engines, leaving more potential visitors on the table. 

## https://www.kkna.kyowakirin.com/media-center/#latest-news News page - Unmoored
A news page is another perfect place to build your credibility with AI agents, by linking yourself to other known, trustworthy sources and by making authoritative, consistent claims about yourself and your product using the language of the semantic web. Unfortunately, the front page of the news has no additional annotations beyond those universal across the site. The articles have entirely no semantic web content whatsoever, despite that being arguably the most important location for it. Annotating your articles would also let the fact that you embed audio be a greater boost to those pages.

