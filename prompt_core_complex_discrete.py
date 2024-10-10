MESSAGE = """You are an AI language model tasked with analyzing a given text document and classifying it according to a specified set of subregisters from the Turku-developed CORE scheme. For each subregister, assign a **1** if the document matches the subregister, and a **0** if it does not.

**Instructions:**

1. **Carefully read the entire document provided.**

2. **For each subregister listed below:**

   - Refer to the **definition** provided for each subregister, which includes detailed characteristics to help you make accurate classifications.

   - Determine whether the document exhibits the characteristics of that subregister.

   - Assign a **1** if it matches the subregister, or a **0** if it does not.

3. **Ensure that every subregister is assigned either a 1 or a 0.**

4. **Structure your output** exactly as specified in the "Output Format" section.

5. **Do not include any additional commentary, explanations, or analysis** beyond the classifications.

---

### **Subregisters and Enhanced Definitions**

**MACHINE TRANSLATED OR GENERATED (MT):**

- **Definition:** Texts that are clearly machine-translated or generated from a template or by an AI, possibly exhibiting unnatural phrasing or errors.

- **Characteristics:**

  - Often found on sites like holiday accommodation or flight booking.

  - It is not necessary to assign another register label if the text is machine-translated or generated.

---

**LYRICAL (LY):**

- **Definition:** Texts that are poetic or song-like in nature, focusing on artistic expression.

- **Characteristics:**

  - Includes song lyrics or poems.

  - Typically originally written by professional songwriters or poets but posted online by fans or contributors.

---

**SPOKEN (SP):**

- **SP-IT (Interview):**

  - **Definition:** Transcriptions of interviews, typically in a question-and-answer format.

  - **Characteristics:**

    - One interviewer and one interviewee.

    - Participants may include journalists and famous persons or experts.

    - Dialogic with a Q&A format.

- **SP-OS (Other Spoken):**

  - **Definition:** Other spoken language texts composed of more than 50% spoken material.

  - **Characteristics:**

    - Includes formal speeches, TV/movie transcripts, or YouTube video transcripts.

---

**INTERACTIVE DISCUSSION (ID):**

- **Definition:** Texts involving interactive communication written by multiple participants in a discussion format.

- **Characteristics:**

  - Includes forum posts, question-and-answer forums.

  - Texts that consist of comments that are clearly part of a discussion.

  - Does not include reader comments following a visible article or blog post.

---

**NARRATIVE (NA):**

- **NA-NE (News report):**

  - **Definition:** Articles reporting on recent events in a factual manner.

  - **Characteristics:**

    - Written by journalists and published by news outlets.

    - Includes releases and newsletters by organizations.

    - Time-sensitive and professionally written.

- **NA-SR (Sports report):**

  - **Definition:** Reports covering recent sports events.

  - **Characteristics:**

    - Written by professional journalists or amateurs on sports club pages.

    - Time-sensitive, focusing on reporting sports events.

- **NA-NB (Narrative blog):**

  - **Definition:** Blog posts that narrate personal experiences or stories.

  - **Characteristics:**

    - Personal, travel, lifestyle blogs.

    - Written by amateur writers.

    - May include comments or interactive aspects.

- **NA-ON (Other narrative):**

  - **Definition:** Other narrative texts not covered above, including fiction and storytelling.

  - **Characteristics:**

    - Focus on narrating events.

    - Includes short stories, fiction, magazine articles.

---

**HOW-TO or INSTRUCTIONS (HI):**

- **HI-RE (Recipe):**

  - **Definition:** Instructions for preparing food and beverages.

  - **Characteristics:**

    - Step-by-step instructions.

    - Includes ingredients and preparation steps.

- **HI-OH (Other how-to):**

  - **Definition:** Guides or tutorials on how to perform tasks or activities.

  - **Characteristics:**

    - Objective instructions, often step-by-step.

    - Includes rules of games, tutorials, filling forms.

    - Subjective advice should be classified as 'Advice' under Opinion.

---

**INFORMATIONAL DESCRIPTION (IN):**

- **IN-EN (Encyclopedia article):**

  - **Definition:** Comprehensive articles providing factual information on specific topics.

  - **Characteristics:**

    - Objective synthesis of knowledge.

    - Often collaborative, on platforms like Wikipedia.

- **IN-RA (Research article):**

  - **Definition:** Scholarly articles presenting original research findings.

  - **Characteristics:**

    - Includes motivation, methods, and findings.

    - Written by academics, targeting specialists.

- **IN-DTP (Description of a thing or person):**

  - **Definition:** Detailed descriptions of objects, places, or individuals.

  - **Characteristics:**

    - Includes administrative information, health descriptions, job postings.

- **IN-FI (FAQ):**

  - **Definition:** Lists of frequently asked questions with corresponding answers.

  - **Characteristics:**

    - Structured as Q&A.

    - Provides specific information.

- **IN-LT (Legal terms and conditions):**

  - **Definition:** Formal legal documents outlining terms, conditions, or policies.

  - **Characteristics:**

    - Official in nature.

    - Includes privacy policies, terms of service, legislation.

- **IN-OI (Other informational description):**

  - **Definition:** Informational texts not covered above, providing factual descriptions.

  - **Characteristics:**

    - Includes course materials, reports, meeting minutes.

    - Presented as objective information.

---

**OPINION (OP):**

- **OP-RV (Review):**

  - **Definition:** Evaluations or critiques of products, services, or creative works.

  - **Characteristics:**

    - Can be on personal, institutional, or commercial websites.

- **OP-OB (Opinion blog):**

  - **Definition:** Blog posts expressing personal opinions or commentary.

  - **Characteristics:**

    - Written by amateur writers.

    - Topics include politics, social issues.

    - Expresses evaluation and stance.

- **OP-RS (Religious blog / sermon):**

  - **Definition:** Religious texts offering teachings, sermons, or reflections.

  - **Characteristics:**

    - Denominational religious content.

- **OP-AV (Advice):**

  - **Definition:** Texts providing guidance or recommendations based on personal opinions.

  - **Characteristics:**

    - Suggests actions to solve problems.

    - Subjective instructions.

    - Topics include health, parenting.

- **OP-OO (Other opinion):**

  - **Definition:** Opinionated texts not covered above.

  - **Characteristics:**

    - May include opinion pieces with less solid argumentation.

---

**INFORMATIONAL PERSUASION (IP):**

- **IP-DS (Description with intent to sell):**

  - **Definition:** Texts describing products or services with the aim of persuading purchase.

  - **Characteristics:**

    - Overtly marketing.

    - Includes book blurbs, product descriptions.

- **IP-ED (News & opinion blog or editorial):**

  - **Definition:** Articles combining news reporting with opinion or editorial commentary.

  - **Characteristics:**

    - Written by professionals.

    - Associated with newspapers or magazines.

- **IP-OE (Other informational persuasion):**

  - **Definition:** Persuasive texts providing information to influence the reader.

  - **Characteristics:**

    - Not overtly marketing.

    - Includes persuasive essays, public health texts, event advertisements.

---

### **Output Format**

Provide your classifications in the exact format below, replacing `[0 or 1]` with either **1** or **0** for each subregister:

```
MT (Machine Translated or Generated): [0 or 1]
LY (Lyrical): [0 or 1]
SP (Spoken):
  - it (Interview): [0 or 1]
  - os (Other spoken): [0 or 1]
ID (Interactive Discussion): [0 or 1]
NA (Narrative):
  - ne (News report): [0 or 1]
  - sr (Sports report): [0 or 1]
  - nb (Narrative blog): [0 or 1]
  - on (Other narrative): [0 or 1]
HI (How-to or Instructions):
  - re (Recipe): [0 or 1]
  - oh (Other how-to): [0 or 1]
IN (Informational Description):
  - en (Encyclopedia article): [0 or 1]
  - ra (Research article): [0 or 1]
  - dtp (Description of a thing or person): [0 or 1]
  - fi (FAQ): [0 or 1]
  - lt (Legal terms and conditions): [0 or 1]
  - oi (Other informational description): [0 or 1]
OP (Opinion):
  - rv (Review): [0 or 1]
  - ob (Opinion blog): [0 or 1]
  - rs (Religious blog / sermon): [0 or 1]
  - av (Advice): [0 or 1]
  - oo (Other opinion): [0 or 1]
IP (Informational Persuasion):
  - ds (Description with intent to sell): [0 or 1]
  - ed (News & opinion blog or editorial): [0 or 1]
  - oe (Other informational persuasion): [0 or 1]
```

**Example Output:**

```
MT (Machine Translated or Generated): 0
LY (Lyrical): 0
SP (Spoken):
  - it (Interview): 0
  - os (Other spoken): 0
ID (Interactive Discussion): 1
NA (Narrative):
  - ne (News report): 0
  - sr (Sports report): 0
  - nb (Narrative blog): 1
  - on (Other narrative): 0
HI (How-to or Instructions):
  - re (Recipe): 0
  - oh (Other how-to): 0
IN (Informational Description):
  - en (Encyclopedia article): 0
  - ra (Research article): 0
  - dtp (Description of a thing or person): 0
  - fi (FAQ): 0
  - lt (Legal terms and conditions): 0
  - oi (Other informational description): 0
OP (Opinion):
  - rv (Review): 0
  - ob (Opinion blog): 1
  - rs (Religious blog / sermon): 0
  - av (Advice): 0
  - oo (Other opinion): 0
IP (Informational Persuasion):
  - ds (Description with intent to sell): 0
  - ed (News & opinion blog or editorial): 0
  - oe (Other informational persuasion): 0
```

---

### **Document to Analyze**

{}

---

**Remember:**

- **Accuracy is crucial.** Base your classifications on the content, style, and purpose of the document.

- **Multiple Labels:** A document can have multiple labels if it features characteristics of more than one subregister.

  - **Examples:**

    - A personal blog that includes a recipe: classify as both 'NA-NB (Narrative blog)' and 'HI-RE (Recipe)'.

    - A marketing text followed by reviews: classify as both 'IP-DS (Description with intent to sell)' and 'OP-RV (Review)'.

    - A sports report that includes the writer's viewpoints: classify as both 'NA-SR (Sports report)' and 'OP-OO (Other opinion)'.

- **Consistency is key.** Use the same criteria for each subregister across different documents.

- **No explanations are needed.** Only provide the classifications as per the output format.

**Begin your analysis after the document is provided.**
"""
