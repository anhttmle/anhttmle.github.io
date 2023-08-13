---
layout: default
title: "NAL Purchase Forcasting Evaluation"
---

# 1. Objective:
Develop a higher quality prediction model that utilizes the existing training and evaluation dataset.

# 2. Dataset:
Current model's feature and label data for training and evaluation
- Full: 4B
- Valuable: 1B

# 3. Model Evaluation:
- LogLoss: Log of Binary Cross-entropy **???**
- Precision of top 5% user in prediction score for a few clients. The list of clientid will be provided:
  - List of clients is not provided **!!!**
  - Top 5% users: criteria of the 5% **???** (such as "**5% of the most used users**")

# 4. Computational Efficiency:
- How to measure?
- Training and inference < 5 hours -> **On how many data points?**
- Hardware requirement should not exceed 400$ -> **On 01 Day, 01 Month or any time unit?**

# 5. Deliverables:
- Code and Model deployment document 
  - **Inference code or Training source code included?**
  - **Any requirement on packaging model such as API/gRPC/Message Queue?**
- Evaluation Results: **Any requirement such as**:
    - metrics result by date/user/overall...
    - feature engineering
    - model hyper-parameters optimizations
    - training log
    - sampling method
    - ...