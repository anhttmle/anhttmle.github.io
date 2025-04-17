# Why we need to utilize domain knowledge?
- AI is trained on Internet data not specialize data
- AI is uncertain
- Correcting AI by manipulate its data is costly

=> To boost its efficiency, we should detect inefficient step and inject domain knowledge from SMEs

# Inject domain knowledge on dev-time
## Examples:
### 1. Encode knowledge (Indexing COBOL source code)
- Common Solution:
  - use LLM to summarize COBOL source code in Natural Language
  - chunking the summary and convert to vector embedding
  - store the embedding in Vector Database
- Heuristic Solution: Follow SMEs way to extract knowledge from COBOL source code
    - How to read source code (where to start, what to refer, any other document to refer)
    - What we should pay attention on (module name, variable name, ...)
    - How we detect the dependency (database schema, API schema, ...)
    - ...
<img width="244" alt="image" src="https://github.com/user-attachments/assets/be2a2c25-796c-47c8-ba12-0d6a0d209f78" />


### 2. Retrieve knowledge (Retrieve context from indexed data)
- Common Solution:
  - Extract important term from question and search on database
  - Semantic search to find related chunks (vector search)
  - Expand context by increasing **top k** (use bigger **k**)
- Heuristic Solution:
  - Any other tool (like Jira, Google Drive,...) can provide more accurate context
<img width="244" alt="image" src="https://github.com/user-attachments/assets/628582a7-8dab-4b29-80f5-26f13ac5feec" />

# Inject domain knowledge on runtime: Feedback API
- Design feedback loop to let user provide feedback on quality of answer
## Examples:
- COBOL-E, COBOL-BA verify the answer and references
  - Like/Dislike the answer
  - Tag reference that not related
- COBOL-BA proactively provide guideline (by message) to Assistant (this answer is not right, should/must be ...)
