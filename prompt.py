MESSAGE = """You are an AI language model tasked with analyzing a given text document and rating it according to a specified taxonomy of web registers and subregisters. For each subregister, assign a score from **1 to 6** based on how well the document exhibits the characteristics of that subregister:

- **1 (Completely Disagree):** The document does not exhibit characteristics of this subregister at all.
- **2 (Mostly Disagree):** The document exhibits minimal characteristics of this subregister.
- **3 (Slightly Disagree):** The document somewhat lacks characteristics of this subregister.
- **4 (Slightly Agree):** The document somewhat exhibits characteristics of this subregister.
- **5 (Mostly Agree):** The document largely exhibits characteristics of this subregister.
- **6 (Completely Agree):** The document fully exhibits characteristics of this subregister.

**Instructions:**

1. **Carefully read the entire document provided.**

2. **For each subregister listed in the taxonomy below:**
   - Refer to the **definition** and **examples** provided.
   - Assess the document's content, style, and purpose against these characteristics.
   - Assign a score from **1 to 6** based on the alignment.

3. **Ensure that every subregister is rated**, even if the score is **1 (Completely Disagree)**.

4. **Structure your output** exactly as specified in the "Output Format" section.

5. **Do not include any additional commentary, explanations, or analysis** beyond the scores.

---

### **Taxonomy of Web Registers and Subregisters**

#### **1. Informational Description (ID)**

- **ID-NE (News Reports):** Articles reporting on recent events and developments.
- **ID-EN (Encyclopedic Articles):** Comprehensive overviews on specific topics.
- **ID-RA (Research Articles):** Scholarly publications presenting original research.
- **ID-LT (Legal Terms and Conditions):** Formal legal documents outlining terms or policies.
- **ID-DT (Descriptive Texts):** Detailed descriptions of things, people, or places.
- **ID-FQ (Frequently Asked Questions):** Lists of common questions with provided answers.
- **ID-OT (Other Informational Texts):** Informational content not covered by other subregisters.

#### **2. Instructional (IN)**

- **IN-HT (How-To Guides and Tutorials):** Step-by-step instructions on performing tasks.
- **IN-RC (Recipes):** Instructions for preparing food and beverages.
- **IN-AD (Advice and Tips):** Guidance or recommendations on various topics.
- **IN-ED (Educational Content):** Content designed for learning purposes.
- **IN-OT (Other Instructional Texts):** Instructional content not covered by other subregisters.

#### **3. Narrative (NA)**

- **NA-NB (Narrative Blogs):** Blog posts that narrate personal experiences or stories.
- **NA-NS (News Stories):** News articles presented in a narrative style.
- **NA-FI (Fictional Narratives):** Stories created from imagination.
- **NA-PN (Personal Narratives):** First-person accounts of personal experiences.
- **NA-OT (Other Narrative Texts):** Narrative content not covered by other subregisters.

#### **4. Opinion/Argumentative (OP)**

- **OP-ED (Editorials and Opinion Pieces):** Articles presenting viewpoints on issues.
- **OP-RV (Reviews and Critiques):** Evaluations of products, services, or creative works.
- **OP-OB (Opinion Blogs):** Blogs focusing on personal opinions or commentary.
- **OP-SR (Sermons and Religious Commentary):** Religious teachings or reflections.
- **OP-AV (Advice Columns):** Columns offering advice based on personal opinions.
- **OP-OT (Other Opinionated Texts):** Opinion content not covered by other subregisters.

#### **5. Interactive Discussion (IC)**

- **IC-FP (Forum Posts):** Messages posted in online forums.
- **IC-CM (Comments and Replies):** User comments on web content.
- **IC-QA (Q&A Platforms):** Question-and-answer exchanges.
- **IC-CH (Chats and Instant Messaging):** Real-time text exchanges.
- **IC-OT (Other Interactive Communications):** Interactive content not covered by other subregisters.

#### **6. Persuasive/Transactional (PT)**

- **PT-AD (Advertisements):** Promotional content for products or services.
- **PT-PR (Product Descriptions):** Descriptions aimed at encouraging purchase.
- **PT-JP (Job Postings):** Listings of employment opportunities.
- **PT-EP (Event Promotions):** Content promoting events.
- **PT-FD (Fundraising Appeals):** Requests for donations or support.
- **PT-OT (Other Persuasive Texts):** Persuasive content not covered by other subregisters.

#### **7. Creative/Lyrical (CL)**

- **CL-PY (Poetry):** Poems and poetic works.
- **CL-SL (Song Lyrics):** Lyrics of songs.
- **CL-FI (Fiction):** Creative stories and narratives.
- **CL-HU (Humor and Satire):** Content intended to amuse or parody.
- **CL-SC (Scripts):** Written scripts for plays, films, etc.
- **CL-OT (Other Creative Texts):** Creative content not covered by other subregisters.

#### **8. Spoken-like (SL)**

- **SL-TR (Transcriptions):** Text transcribed from spoken language.
- **SL-IT (Interviews):** Q&A sessions transcribed.
- **SL-DS (Dialogues):** Texts presented as conversations.
- **SL-SP (Speeches and Presentations):** Texts of spoken addresses.
- **SL-OT (Other Spoken-like Texts):** Spoken-like content not covered by other subregisters.

#### **9. Machine-generated (MG)**

- **MG-MT (Machine-Translated Texts):** Texts translated by machine translation tools.
- **MG-AG (AI-Generated Content):** Texts generated by AI models.
- **MG-AT (Automated Transcriptions):** Transcripts created by speech recognition software.
- **MG-OT (Other Machine-Generated Texts):** Machine-generated content not covered by other subregisters.

---

### **Output Format**

Provide your ratings in the exact format below, replacing `[Score]` with the number from **1 to 6** for each subregister:

```
ID-NE (News Reports): [Score]
ID-EN (Encyclopedic Articles): [Score]
ID-RA (Research Articles): [Score]
ID-LT (Legal Terms and Conditions): [Score]
ID-DT (Descriptive Texts): [Score]
ID-FQ (Frequently Asked Questions): [Score]
ID-OT (Other Informational Texts): [Score]

IN-HT (How-To Guides and Tutorials): [Score]
IN-RC (Recipes): [Score]
IN-AD (Advice and Tips): [Score]
IN-ED (Educational Content): [Score]
IN-OT (Other Instructional Texts): [Score]

NA-NB (Narrative Blogs): [Score]
NA-NS (News Stories): [Score]
NA-FI (Fictional Narratives): [Score]
NA-PN (Personal Narratives): [Score]
NA-OT (Other Narrative Texts): [Score]

OP-ED (Editorials and Opinion Pieces): [Score]
OP-RV (Reviews and Critiques): [Score]
OP-OB (Opinion Blogs): [Score]
OP-SR (Sermons and Religious Commentary): [Score]
OP-AV (Advice Columns): [Score]
OP-OT (Other Opinionated Texts): [Score]

IC-FP (Forum Posts): [Score]
IC-CM (Comments and Replies): [Score]
IC-QA (Q&A Platforms): [Score]
IC-CH (Chats and Instant Messaging): [Score]
IC-OT (Other Interactive Communications): [Score]

PT-AD (Advertisements): [Score]
PT-PR (Product Descriptions): [Score]
PT-JP (Job Postings): [Score]
PT-EP (Event Promotions): [Score]
PT-FD (Fundraising Appeals): [Score]
PT-OT (Other Persuasive Texts): [Score]

CL-PY (Poetry): [Score]
CL-SL (Song Lyrics): [Score]
CL-FI (Fiction): [Score]
CL-HU (Humor and Satire): [Score]
CL-SC (Scripts): [Score]
CL-OT (Other Creative Texts): [Score]

SL-TR (Transcriptions): [Score]
SL-IT (Interviews): [Score]
SL-DS (Dialogues): [Score]
SL-SP (Speeches and Presentations): [Score]
SL-OT (Other Spoken-like Texts): [Score]

MG-MT (Machine-Translated Texts): [Score]
MG-AG (AI-Generated Content): [Score]
MG-AT (Automated Transcriptions): [Score]
MG-OT (Other Machine-Generated Texts): [Score]
```

**Example Output:**

```
ID-NE (News Reports): 5
ID-EN (Encyclopedic Articles): 2
ID-RA (Research Articles): 1
ID-LT (Legal Terms and Conditions): 1
ID-DT (Descriptive Texts): 4
ID-FQ (Frequently Asked Questions): 1
ID-OT (Other Informational Texts): 2

IN-HT (How-To Guides and Tutorials): 2
IN-RC (Recipes): 1
IN-AD (Advice and Tips): 3
IN-ED (Educational Content): 2
IN-OT (Other Instructional Texts): 1

NA-NB (Narrative Blogs): 4
NA-NS (News Stories): 3
NA-FI (Fictional Narratives): 1
NA-PN (Personal Narratives): 5
NA-OT (Other Narrative Texts): 2

OP-ED (Editorials and Opinion Pieces): 1
OP-RV (Reviews and Critiques): 2
OP-OB (Opinion Blogs): 1
OP-SR (Sermons and Religious Commentary): 1
OP-AV (Advice Columns): 1
OP-OT (Other Opinionated Texts): 1

IC-FP (Forum Posts): 1
IC-CM (Comments and Replies): 2
IC-QA (Q&A Platforms): 1
IC-CH (Chats and Instant Messaging): 1
IC-OT (Other Interactive Communications): 1

PT-AD (Advertisements): 2
PT-PR (Product Descriptions): 2
PT-JP (Job Postings): 1
PT-EP (Event Promotions): 1
PT-FD (Fundraising Appeals): 1
PT-OT (Other Persuasive Texts): 1

CL-PY (Poetry): 1
CL-SL (Song Lyrics): 1
CL-FI (Fiction): 1
CL-HU (Humor and Satire): 2
CL-SC (Scripts): 1
CL-OT (Other Creative Texts): 1

SL-TR (Transcriptions): 1
SL-IT (Interviews): 1
SL-DS (Dialogues): 2
SL-SP (Speeches and Presentations): 1
SL-OT (Other Spoken-like Texts): 1

MG-MT (Machine-Translated Texts): 1
MG-AG (AI-Generated Content): 1
MG-AT (Automated Transcriptions): 1
MG-OT (Other Machine-Generated Texts): 1
```

---

### **Document to Analyze**

[Insert the text of the document here.]

---

**Remember:**

- **Accuracy is crucial.** Base your scores on the content and characteristics of the document.
- **Consistency is key.** Use the same criteria for each subregister across different documents.
- **No explanations are needed.** Only provide the scores as per the output format.

**Begin your analysis after the document is provided.**

"""
