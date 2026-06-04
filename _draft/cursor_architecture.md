Reference: https://blog.bytebytego.com/p/how-cursor-shipped-its-coding-agent

# 1. Coding agent vs Agentic coding model

<img width="1456" height="915" alt="image" src="https://github.com/user-attachments/assets/c54a6f28-7efc-4877-bdeb-9aac2aa8824c" />

# 2. System Architecture

<img width="1456" height="1131" alt="image" src="https://github.com/user-attachments/assets/027070dc-1b83-4114-a776-7825fb1fcc5c" />


## 2.1. Router

## 2.2. Agentic coding model

## 2.3. Tools

## 2.4. Context Retrieval

## 2.5. Orchestrator

## 2.6. Sandbox (Execution Environment)

## 2.7. Others
- Long-term memory
- Policy layer
- Safety layer
- Planing modules
- Collaboration features

# 3. Production challenges
## 3.1. The “Diff Problem”
- They ensured their training data contained a high volume of trajectories specifically focused on search and replace tool usage, forcing the model to over-learn the mechanical constraints of these operations

## 3.2. Latency Compounds
- Mixture of Experts (MoE) architecture
- Speculative decoding
- Context compaction

## 3.3. Sandboxing at Scale
- At large scale, it becomes a performance and infrastructure constraint
- Two major issues dominate when training the model:
  - Provisioning time becomes the bottleneck
  - Concurrency makes startup overhead a bottleneck at scale
