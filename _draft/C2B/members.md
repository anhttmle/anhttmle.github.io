# AI Expert
**Name**: The-Anh Tran
<br>
**Experience**: 10 years
<br>
**Core Skills**: 
- AI
  - Learning Algorithm:
    - Supervise

   
# AI Engineer
### Name: Minh Chi Bui
### Experience: 5 years
### Core Skills:
- Machine Learning
  - Proficiency: Natural Language Processing, Deep Learning, Computer Vision
  - Intermediate: Data analytics, Visualization
- Programming Languages
  - Proficiency: Python
  - Intermediate: Java, bash
- Tools and Frameworks
  - Proficiency: Pytorch, Git, Docker
  - Intermediate: Tensorflow, Keras, Flask, FastAPI
- Database & Cloud
  - Proficiency: SQL (MySQL, PostgreSQL), VectorDB (Milvus, ChromaDB)
  - Intermediate: NoSQL (MongoDB), GCP
  - Basic: AWS, Azure
- Others
  - K8S, Crontab, Ubuntu, MLOps, Cybersecurity

### Publications:
- Thanh Dat Hoang, Chi Minh Bui, Khac Hoai Nam Bui. ”Viettel-AI at SemEval-2023 Task 6:
Legal Document Understanding with Longformer for Court Judgment Prediction with Explanation”.
Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023).
- Thanh-Do Nguyen, Chi Minh Bui, Thi-Hai-Yen Vuong and Xuan-Hieu Phan. ”Passage-based BM25
Hard Negatives: A Simple and Effective Negative Sampling Strategy For Dense Retrieval”. Proceedings
of the 37th Pacific Asia Conference on Language, Information and Computation. (PACLIC 37)

### Projects:
- News Categories Classification
  - Developed and optimized the model for CPU servers with improved overall accuracy to 85% and
  reduced latency by more than 30% compared with older models.
  - Automated the labeling phase, significantly reducing financial and labor costs, and integrated the
  application into the website system.
  - Designed a recommendation model focusing on delivering personalized news for private customers.
  Outcome: Successfully integrated into the Reputa system, supporting 200+ companies for social lis-
  tening purposes.
- End-to-End QA System
  - Designed deep learning models for an end-to-end question answering system, achieving a top-3 in
  ZALO AI Challenge.
  - Leveraged GPUs and optimized code for cross-training and parallel training.
  - Implemented bi-encoder and evaluated cross-encoder for the retrieval phase.
  - Built a Docker services and integrated in K8S
- Research on LLM
  - Experimented with and deployed a advanced RAG pipeline, including fine-tuning LLM models (e.g.,
  Llama series, Qwen series) with LoRA, qLoRA and augmenting data for specific use cases (e.g., legal
  QA), using LangChain and custom libraries.
  - Deployed and optimized inference speed for Llama and decoder-based LLMs using vLLM and exLlama.
  - Leveraged SFT and DPO for Llama3 series to achieved SOTA in VMLU (Vietnamese LLM benchmark)
  using crawled and synthetic data from top models.
- Further research and implementations
  - Developed a domain-centric Knowledge Graph, optimized using the GraphRAG approach, and sub-
  mitted findings to SIGIR 2025.
  - Built and integrated services into Kubernetes (K8s) for scalable and efficient production deployment
- Court Judgement Prediction and Explanation
  - Used large sparse transformer models (Longformer) combined with lexical models to enhance infor-
  mation and improve task accuracy.
  - Achieved first place in competitions with a scientific paper accepted at SemEval (ACL).
- Auto tuning firewall project
  - Developed a system that detect anomaly user behaviors for auto tuning WAF system.
  - Built a system that collected the data and detect bad requests to reduce false positive from traditional
  WAF (Web ApplicationFirewall).
  - Built a profile prototype and a model to tracked IP to rank users rating.
  - Reduced the human workforce in monitoring with an acceptable accuracy.
  - Applied quantization to the model to reduce the latency (support around 100 mils user requests per
  day).
  - Developed a DNS monitor module (tracking DNS to alert redirect site) using cron job.
  
  Product: The application has integrated into the WAF and served more than 100 millions requests
  per day and denied around 100 to 1000 IP attackers per day
- Duplicate news and video detection
  - Designed an algorithm for video recommendation within the stipulated time. Used and applied tensor-
  flow as main application and flask for api. Worked with a 5-members research team for accomplishing
  this.
  - Increased the average time per devices by 5-10% and the total amounts of time by 13% by A/B
  testing.
  - Detected duplicate news cover 95% accuracy over a thousand news per day. This helped the moder-
  ators to reduced 80% working hours to check the duplicate ones.
  
  Product: The features has applied in Mocha (app for Android and IOS) and Netnews.vn
- Tracking human workforce using vband
  - Worked with Human Activity Recognition (HAR) problems to helped the manager tracking em-
  ployees workforce. (https://news.microsoft.com/vi-vn/2021/09/06/vantix-ung-dung- tri-tue-nhan-tao-
  nang-cao-nang-suat-lao-dong/)
  - Used various timeseries model and approached to improved the accurate of the predictions. (Worked
  with RNN, CNN, ensemble models and XGBoost)
  - Worked with GPS correction problems for tracking worker in the construction (applied in VinHomes
  construction).
  - Used Kalman-Filtering algorithms to improved the roadmap for GPS and also reduced the GPS flash-
  ing, flicking problems.
  - Built a FastAPI demo for map tracking and dockerized the application into production.
  
  Product: The application has served all the VinPearls and some VinHomes projects
