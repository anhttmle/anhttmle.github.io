# AI Expert
**Name**: The-Anh Tran
<br>
**Experience**: 10 years
<br>
**Core Skills**: 
- AI
  - Learning Algorithm:
    - Supervise
   
### Publications:
- An extensive examination of discovering 5-Methylcytosine Sites in Genome-Wide DNA Promoters using machine learning based approaches (IEEEFeb 1, 2022)
> It is well-known that the major reason for the rapid proliferation of cancer cells are the hypomethylation of the whole cancer genome and the hypermethylation of the promoter of particular tumor suppressor genes. Locating 5-methylcytosine (5mC) sites in promoters is therefore a crucial step in further understanding of the relationship be-tween promoter methylation and the regulation of mRNA gene expression. High throughput identification of DNA 5mC in wet lab is still time-consuming and labor-extensive. Thus, finding the 5mC site of genome-wide DNA pro-moters is still an important task. We compared the effectiveness of the most popular and strong machine learning techniques namely XGBoost, Random Forest, Deep Forest, and Deep Feedforward Neural Network in predicting the 5mC sites of genome-wide DNA promoters. A feature extraction method based on k-mers embeddings learned from a language model were also applied. Overall, the performance of all the surveyed models surpassed deep learning models of the latest studies on the same dataset employing other encoding scheme. Furthermore, the best model achieved AUC scores of 0.962 on both cross-validation and independent test data. We concluded that our approach was efficient for identifying 5mC sites of promoters with high performance.
- Incorporating a transfer learning technique with amino acid embeddings to efficiently predict N-linked glycosylation sites in ion channels (Computers in Biology and Medicine - Jan 7, 2021)
> Glycosylation is a dynamic enzymatic process that attaches glycan to proteins or other organic molecules such as lipoproteins. Research has shown that such a process in ion channel proteins plays a fundamental role in modulating ion channel functions. This study used a computational method to predict N-linked glycosylation sites, the most common type, in ion channel proteins. From segments of ion channel proteins centered around N-linked glycosylation sites, the amino acid embedding vectors of each residue were concatenated to create features for prediction. We experimented with two different models for converting amino acids to their corresponding embeddings: one was fed with ion channel sequences and the other with a large dataset composed of more than one million protein sequences. The latter model stemmed from the idea of transfer learning technique and emerged as a more efficient feature extractor. Our best model was obtained from this transfer learning approach and a hyperparameter tuning process with a random search on 5-fold cross-validation data. It achieved an accuracy, specificity, sensitivity, and Matthews correlation coefficient of 93.4%, 92.8%, 98.6%, and 0.726, respectively. Corresponding scores on an independent test were 92.9%, 92.2%, 99%, and 0.717. These results outperform the position-specific scoring matrix features that are predominantly employed in post-translational modification site predictions. Furthermore, compared to N-GlyDE, GlycoEP, SPRINT-Gly, the most recent N-linked glycosylation site predictors, our model yields higher scores on the above 4 metrics, thus further demonstrating the efficiency of our approach. 

--------------------------------------------------------------------------------------------------------------------------------------------
   
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
