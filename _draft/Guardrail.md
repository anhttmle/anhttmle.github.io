Before: RAG -> Prompt -> LLM -> Output
After: RAG -> Prompt -> Guardrail -> LLM -> Guardrail -> Output

Input Guardrail:
- Contain PII
- Proprietary Info
- Jail Break attempt

Output Guardrail:
- Hallucinations
- NSFW
- Sensitive Topics

Guardrail type:
- Heuristic:
  - Regular Expression -> Matching phone number, email,...
  - Pattern Matching
  - Keyword/Filters
- ML:
  - Classification
  - Factuality
  - Topic Detection
  - NER
- LLM call:
  - Score for Toxicity
  - Rate tone of voice
  - Verify coherence
