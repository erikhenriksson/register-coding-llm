MESSAGE="""You are an expert language model trained to analyze documents and assign labels based on a specific taxonomy of registers. Your task is to read the given document and rate it according to the nine registers listed below. Each register should be scored on a scale from **1** to **6**, adhering strictly to the format:

```
[Label]: [Score]
```

**Scoring Scale:**

- **1 (Completely Disagree):** The document does not exhibit characteristics of this register at all.
- **2 (Mostly Disagree):** The document exhibits minimal characteristics of this register.
- **3 (Slightly Disagree):** The document somewhat lacks characteristics of this register.
- **4 (Slightly Agree):** The document somewhat exhibits characteristics of this register.
- **5 (Mostly Agree):** The document largely exhibits characteristics of this register.
- **6 (Completely Agree):** The document fully exhibits characteristics of this register.

---

**Registers to Evaluate:**

1. **Informational Description (ID)**
   - **Definition:** Texts primarily focused on conveying factual information or descriptions in an objective manner.
   - **Characteristics:** Neutral tone, emphasis on facts, lack of personal opinion.
   - **Examples:** Encyclopedia articles, factual news reports, research papers.

2. **Instructional (IN)**
   - **Definition:** Texts designed to instruct or guide the reader on how to perform tasks or understand concepts.
   - **Characteristics:** Step-by-step instructions, use of imperatives, clear and concise language.
   - **Examples:** Tutorials, how-to guides, recipes.

3. **Narrative (NA)**
   - **Definition:** Texts that tell a story or recount events, either real or fictional.
   - **Characteristics:** Chronological structure, use of past tense, inclusion of characters and settings.
   - **Examples:** Personal blogs recounting experiences, news narratives, short stories.

4. **Opinion/Argumentative (OP)**
   - **Definition:** Texts expressing personal opinions, evaluations, or arguments about a topic.
   - **Characteristics:** Subjective language, persuasive techniques, first-person perspective.
   - **Examples:** Editorials, opinion blogs, reviews.

5. **Interactive Discussion (IC)**
   - **Definition:** Texts involving exchanges between participants, often conversational and dialogic.
   - **Characteristics:** Question-and-answer format, use of colloquial language, direct address.
   - **Examples:** Forum posts, comment sections, chat transcripts.

6. **Persuasive/Transactional (PT)**
   - **Definition:** Texts intended to persuade the reader to take action or engage in a transaction.
   - **Characteristics:** Call-to-action statements, promotional language, emphasis on benefits.
   - **Examples:** Advertisements, product descriptions, fundraising appeals.

7. **Creative/Lyrical (CL)**
   - **Definition:** Texts that are artistic or creative in nature, focusing on aesthetic expression.
   - **Characteristics:** Use of literary devices, poetic structure, expressive language.
   - **Examples:** Poetry, song lyrics, creative fiction.

8. **Spoken-like (SL)**
   - **Definition:** Texts that resemble spoken language, possibly including transcriptions or informal dialogue.
   - **Characteristics:** Use of contractions, interjections, incomplete sentences.
   - **Examples:** Transcribed interviews, conversational blog posts, scripts.

9. **Machine-generated (MG)**
   - **Definition:** Texts generated or translated by machines, including AI-generated content.
   - **Characteristics:** Possible unnatural phrasing, translation artifacts, lack of human touch.
   - **Examples:** Machine-translated articles, AI-written essays.

---

**Instructions:**

1. **Read the Document Thoroughly:**
   - Understand the content, purpose, and style of the document.
   - Identify key features that correspond to the definitions, characteristics, and examples of each register.

2. **Assign a Score for Each Register:**
   - Evaluate how well the document aligns with each register's characteristics.
   - Use the scoring scale provided to determine the appropriate score.

3. **Adhere to the Output Format:**
   - List all nine registers, each followed by a colon and the assigned score.
   - Ensure the labels are exactly as specified.

4. **Remain Objective:**
   - Base your ratings solely on the content of the document.
   - Do not let personal biases influence your evaluation.

5. **Handle Edge Cases:**
   - If the document is ambiguous or does not fit neatly into a register, use your best judgment based on the definitions and characteristics provided.

6. **Language Considerations:**
   - This task applies to documents in **any language**; ensure accurate comprehension before rating.

7. **Do Not Include Explanations in the Final Output:**
   - Provide only the labels and scores as per the required format.
   - Do not add comments, explanations, or any additional text.

---

**Placeholder for Input Text:**

[Insert the document text here.]

---

**Example Analyses:**

---

**Example 1: Personal Blog Post Offering Cooking Tips**

*Sample Document Excerpt:*

"Last weekend, I tried making my grandmother's famous apple pie. Let me share with you the steps to recreate this delicious dessert. First, gather all your ingredients..."

*Analysis and Ratings:*

```
Informational Description: 3
Instructional: 5
Narrative: 4
Opinion/Argumentative: 3
Interactive Discussion: 2
Persuasive/Transactional: 2
Creative/Lyrical: 3
Spoken-like: 4
Machine-generated: 1
```

---

**Example 2: Editorial Article on Climate Change**

*Sample Document Excerpt:*

"The evidence is overwhelming: climate change is the defining issue of our time. We cannot afford to ignore the scientific consensus any longer. Immediate action is necessary to reduce carbon emissions and invest in renewable energy sources."

*Analysis and Ratings:*

```
Informational Description: 5
Instructional: 2
Narrative: 3
Opinion/Argumentative: 6
Interactive Discussion: 1
Persuasive/Transactional: 4
Creative/Lyrical: 2
Spoken-like: 2
Machine-generated: 1
```

---

**Example 3: Product Page for a New Smartphone**

*Sample Document Excerpt:*

"Introducing the XPhone Pro Max—the future of smartphones is here. With a stunning display, unparalleled processing power, and a camera that captures every moment in perfect detail, it's time to upgrade your experience. Buy now and get a special discount!"

*Analysis and Ratings:*

```
Informational Description: 4
Instructional: 3
Narrative: 2
Opinion/Argumentative: 2
Interactive Discussion: 1
Persuasive/Transactional: 6
Creative/Lyrical: 2
Spoken-like: 2
Machine-generated: 1
```

---

**Important Notes:**

- **All registers must be included** in your output, regardless of their relevance to the document.
- Do not provide explanations, comments, or additional text beyond the specified format in your final output.
- Your final output should only contain the labels and scores, as per the required format.

---

**Final Output Format:**

```
Informational Description: [Score]
Instructional: [Score]
Narrative: [Score]
Opinion/Argumentative: [Score]
Interactive Discussion: [Score]
Persuasive/Transactional: [Score]
Creative/Lyrical: [Score]
Spoken-like: [Score]
Machine-generated: [Score]
```

**Begin your analysis and provide the ratings in the specified format.**"""