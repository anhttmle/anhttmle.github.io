# Toward human-intelligence (Yan Lecunn)

- AGI term was created to imply human-level intelligence but human intelligence is not general. We're specialized
- Term in Meta: AMI (Advance Machine Intelligence) -> pronounce "ami", mean "friend" in French
- AMI:
    - Learn
    - Remember    
    - Plan
    - Reason
    - Common Sense
    - Steerable
    - Safe
- We need Human-level AI for Intelligence Assistant
- In near future, all interact with Digital World is through:
    - AI Assistant: Voice, Vision, display, EMG (Electromyography - measures muscle response or electrical activity in response to a nerve's stimulation of the muscle)
- We need machine reach to Human-level intelligence
    - Machine can understand how the world works
        - Systems that can learn world models from sensory inputs
    - Machine that can remember
        - Large scale associative memories
    - Machine that can reason & plan
        - Can fulfill an objective
            - Inventing new solution to unseen problems
    - Machine that are controllable and safe
        - By design not by finetuning
- Inference as Optimization
    - Instead of providing answer by feed forward a bunch of layer, treat and inference request as an optimization request
    - Providing input to model, it will tell us what is compatible answer
    - Like Probabilistic Graphical Model, Bayesian Network
    - In the past, All of AI is Search & Optimization problems
    - Optimization-based inference will give AI system zero-shot learning ability
- Energy-based model
    - Energy function vs Cost function
    - Low energy on compatible (x, y) pair in training set
    - High energy on otherwise
- Auto Regressive LLM use Feed-Forward Inference
- Limitation of LLM: No planing
- AI system for planing & reasoning
    - Perception: Compute abstraction of current state
    - World Model: Predict state result from imagined action sequence
    - Task Objective: Measure divergence to goal
    - Guardrail Objective: Immutable objective terms that ensure safety
    - Operation: Finds an action sequence that minimizes the objectives
<img width="638" alt="image" src="https://github.com/user-attachments/assets/e50bc1cf-d2e8-4295-994d-47822b03f8b5" />
- The world is not deterministic & fully prictable
    - Not deterministic
    - If deterministic, so can't observe all variable

  

# ...
