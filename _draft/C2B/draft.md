- API Gateway
   - Indexing API: index COBOL source code to DB (require MetadataDB - PostgreSQL, GraphDB - Neo4j, Search Engine - Elastic Search, VectorDB - Milvus)
   - Tmp Indexing API: index intermediate data (new data provide by user or system inferenced one)
   - Retrieval API: retrieve data that indexed by Indexing API/Tmp Indexing API
   - Configuration API
   - Feedback API: feedback from user to help Virtual Assistant give better answer in the future)
   - ...
- Database:
   - MetadataDB - PostgreSQL
   - GraphDB - Neo4j
   - Search Engine - Elastic Search
   - VectorDB - Milvus
- AI Core Processing: will request to RAG framework to running pre-defined workflow or contain agent strategy
- RAG framework - Dify
- Tools inventory: Providing tool for RAG framework request to by http

### How do users interact with the system?

> Do they use a Web UI, or is everything through API calls (e.g., Postman, CLI tools)?
> Will different roles use different interfaces?

- Client can integrate the API package to a chat application (like CLI, Web App, Slack,...)
- End user will interact with Chat Interface
- Admin/Operator will interact with Admin Page

### What internal services/modules are planned in the API?

> Examples:
> 
> Auth service
> 
> COBOL parser
> 
> Spec/documentation generator
> 
> Q&A engine (LLM-based?)
> 
> GitHub integration service

- Indexing API: index COBOL source code to DB (require MetadataDB - PostgreSQL, GraphDB - Neo4j, Search Engine - Elastic Search, VectorDB - Milvus)
- Tmp Indexing API: index intermediate data (new data provide by user or system inferenced one)
- Retrieval API: retrieve data that indexed by Indexing API/Tmp Indexing API
- Configuration API
- Feedback API: feedback from user to help Virtual Assistant give better answer in the future)
- Auth Service
- COBOL parser
- Spec/Documentation Generator
- Q&A Engine
- Github integration service

### What external services or databases are needed?

> Examples:
>
> PostgreSQL for user data
> 
> Vector DB for embedding & retrieval
>
> Redis for caching
> 
> GitHub API
> 
> OpenAI or internal LLM?

- MetadataDB - PostgreSQL
- GraphDB - Neo4j
- Search Engine - Elastic Search
- VectorDB - Milvus
- Caching - Redis
- LLM - OpenAI API
- COBOL Source code - Github API
