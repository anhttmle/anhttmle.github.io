# For building AI Agent
1. System Design

Agent system is software => need skill to design a software system to design the agents system (building an orchestra)
=> Need to design how agents talk to each other, use tools effectively,...

3. Tool & contract design

Each tool has its own contract, any fuzzy part might lead to agent hallucination
=> Need to clarify the details on schema/input/output/purpose

5. Retrieval engineering 

Using RAG for enhancing context
- Chunking
- Embbed
- Reranking

6. Reliability engineering 

- Fail
    - Retry 
    - Timeout 
    - Circus breaker

7. Security and safety 

- Prompt injection
- Input validation
- Output filter
- Permission boundary

8. Evaluation and observability

- Can not improve what can not measure
- Need tracing, log... Complete timeline of what agent did and why
- Metric: success rate, latency, cost per task
- Automate tests that catch regressions before they ship

9. Product thinking (most important)

- when agent ask for clarification
- when escalate to actual human
- how to build trust so people actually use it in real work
- UX design for system inherently unpredictable
- Think about the others end not just the code in the middle

# 
