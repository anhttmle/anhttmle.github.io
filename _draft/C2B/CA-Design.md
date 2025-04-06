# COBOL to JAVA Virtual Assistant API


# 🧭 Level 1: System Context

## 🔷 System Overview

### Virtual Assistant API
A backend API package acting as a virtual assistant for the team involved in migrating legacy COBOL systems to modern JAVA systems.

---

## 👥 Primary Users

| Role                    | Responsibilities                                                                 |
|-------------------------|----------------------------------------------------------------------------------|
| **COBOL Engineer (COBOL-E)**     | Provides COBOL source code and clarifies legacy system behavior               |
| **COBOL Business Analyst (COBOL-BA)** | Prepares specs/documents from COBOL understanding                             |
| **JAVA Business Analyst (JAVA-BA)**   | Writes specs for JAVA system; aligns with COBOL-BA                             |
| **JAVA Engineer (JAVA-E)**       | Develops JAVA system based on translated documents/specs                      |
| **JAVA Product Owner (JAVA-PO)** | Ensures delivery matches business expectations                               |
| **JAVA Technical Leader (JAVA-TL)**   | Oversees architecture and dev best practices                                  |
| **Administrator/Operator**      | Manages accounts, configures and fine-tunes the Virtual Assistant             |

---

## 🎯 System Goals

- Parse and analyze COBOL source code (via GitHub/GitLab or ZIP upload)
- Assist in building documentation/specs for JAVA migration
- Act as a central knowledge assistant to answer team questions
- Enable cross-role collaboration through shared understanding of legacy code

---

## 🔗 External Systems

- **GitHub/GitLab (Optional):** For accessing COBOL source repositories

## 🖼️ Diagram
```mermaid
graph TD
    subgraph Users
        COBOL_E[COBOL Engineer]
        COBOL_BA[COBOL Business Analyst]
        JAVA_BA[JAVA Business Analyst]
        JAVA_E[JAVA Engineer]
        JAVA_PO[JAVA Product Owner]
        JAVA_TL[JAVA Technical Leader]
        Admin[Administrator / Operator]
    end

    subgraph System
        VA[Virtual Assistant API]
    end

    COBOL_E -->|Upload COBOL code<br>Ask questions| VA
    COBOL_BA -->|Provide spec template<br>Ask questions| VA
    JAVA_BA -->|Review specs<br>Ask questions| VA
    JAVA_E -->|Review documents<br>Ask questions| VA
    JAVA_PO -->|Review feature coverage| VA
    JAVA_TL -->|Validate architecture| VA
    Admin -->|Manage users & config| VA
    GitHub[(GitHub/GitLab)] -->|Provide source code| VA

```


# 🧱 C4 Level 2: Container – "COBOL to JAVA Virtual Assistant API"

## 📦 Containers in the System

| Container                 | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| **API Gateway**           | Entry point for all API calls (authentication, routing)            |
| **Indexing API**          | Parses and indexes COBOL source code into multiple data stores     |
| **Memory API**      | Indexes intermediate/inferred user/system data                     |
| **Retrieval API**         | Retrieves indexed content for answering user questions             |
| **Configuration API**     | Admin-facing API to configure system behavior                      |
| **Feedback API**          | Collects feedback to improve assistant performance                 |
| **Auth Service**          | Handles authentication and authorization                           |
| **COBOL Parser**          | Extracts information from COBOL code                               |
| **Spec/Doc Generator**    | Builds specs/docs from parsed data                                 |
| **Q&A Engine**            | Responds to questions using data from storage and LLM              |
| **GitHub Integration Service** | Interacts with GitHub for code access                         |
| **AI Core Processor**     | Orchestrates calls to RAG framework or agent-based workflow        |
| **RAG Framework (Dify)**  | External orchestrator for Retrieval-Augmented Generation           |
| **Tools Inventory**       | Provides tools invoked via HTTP for the RAG engine                 |
| **Admin Page**            | Interface for Admins to manage system                              |
| **Chat Interface**        | Interface where end-users interact with the assistant              |

---

## 🗃️ Databases / External Services

| Service              | Role                                                                |
|----------------------|---------------------------------------------------------------------|
| **PostgreSQL (MetadataDB)** | Stores structured metadata about COBOL system                 |
| **Neo4j (GraphDB)**         | Stores relationships between entities/features/modules        |
| **ElasticSearch**           | Full-text search index for COBOL code and docs                |
| **Milvus (VectorDB)**       | Stores embeddings for semantic search                         |
| **Redis**                   | Caching for performance                                       |
| **OpenAI API**              | Language model for answering and reasoning                    |
| **GitHub API**              | Source for COBOL code (optional)                              |

---

## 👨‍💻 User Interfaces

- **Chat Interface**: Used by COBOL-E, COBOL-BA, JAVA-BA, JAVA-E, JAVA-TL, JAVA-PO  
- **Admin Page**: Used by Administrator/Operator

---

## 🖼️ Mermaid: Container Diagram

```mermaid
flowchart TB
  subgraph Client[" (Web, CLI, Slack, etc.)"]
    ChatUI["Chat Interface"]
    AdminUI["Admin Page"]
  end

  subgraph API_Gateway["API Gateway"]
    IndexingAPI["Indexing API"]
    TmpIndexingAPI["Tmp Indexing API"]
    RetrievalAPI["Retrieval API"]
    ConfigAPI["Configuration API"]
    FeedbackAPI["Feedback API"]
    AuthAPI["Auth Service"]
  end

  subgraph Services
    COBOLParser["COBOL Parser"]
    DocGen["Spec/Doc Generator"]
    QAEngine["Q&A Engine"]
    GitHubService["GitHub Integration"]
    AICore["AI Core Processor"]
    Tools["Tools Inventory"]
  end

  subgraph External
    PostgreSQL["PostgreSQL\n(MetadataDB)"]
    Neo4j["Neo4j\n(GraphDB)"]
    Elastic["ElasticSearch"]
    Milvus["Milvus\n(Vector DB)"]
    Redis["Redis\n(Cache)"]
    OpenAI["OpenAI API"]
    GitHub["GitHub API"]
    Dify["RAG Framework\n(Dify)"]
  end

  ChatUI --> RetrievalAPI
  ChatUI --> FeedbackAPI
  ChatUI --> QAEngine

  AdminUI --> ConfigAPI
  AdminUI --> FeedbackAPI

  IndexingAPI -->|Store data| PostgreSQL
  IndexingAPI --> Neo4j
  IndexingAPI --> Elastic
  IndexingAPI --> Milvus

  TmpIndexingAPI --> PostgreSQL
  TmpIndexingAPI --> Milvus

  RetrievalAPI --> PostgreSQL
  RetrievalAPI --> Elastic
  RetrievalAPI --> Milvus
  RetrievalAPI --> QAEngine

  QAEngine --> AICore
  AICore --> Dify
  Dify --> Tools
  Dify --> OpenAI
  Dify --> Redis

  GitHubService --> GitHub
  COBOLParser --> IndexingAPI
  COBOLParser --> TmpIndexingAPI
  DocGen --> RetrievalAPI

  ConfigAPI --> Redis
  FeedbackAPI --> PostgreSQL
  AuthAPI --> Redis

```
