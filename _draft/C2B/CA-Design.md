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


# 📦 Level 2: Container

## 🧱 Containers Overview

| Container             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Backend API**       | Core interface exposing REST endpoints to clients and handling user interaction logic |
| **Database**          | Stores structured metadata, user data, chat logs, etc. (PostgreSQL)         |
| **File Storage**      | Stores uploaded COBOL files or intermediary assets                          |
| **AI Core Processor** | Executes pre-defined workflows or agent-based strategies; interfaces with the RAG framework |
| **RAG Framework (Dify)** | Responsible for retrieval-augmented generation and agent orchestration     |
| **Tools Inventory**   | Provides tool services (e.g., spec builder, COBOL highlighter) used by RAG via HTTP |

---

## 🎮 Interaction Channels

| Role           | Interface                                                         |
|----------------|--------------------------------------------------------------------|
| **End Users**      | Chat Interface (CLI, Web, Slack, etc.)                           |
| **Admin/Operator** | Admin Page for managing config, access, feedback loop, etc.       |

---

## ⚙️ Internal API Modules

- **Auth API** – Manage authentication/authorization  
- **Parser API** – Parse and structure COBOL source code  
- **Indexing API** – Index data to metadata DB, graph, search, and vector DBs  
- **Retrieval API** – Query and fetch indexed data  
- **Q&A API** – Handles team queries about code/specs using LLM
- **Spec Gen API** – Generates migration specs from COBOL code  
- **Configuration API** – Manage system behavior and workflows  
- **Feedback API** – Collect user feedback for continuous improvement  

---

## 🌐 External Services

| Service        | Purpose                                           |
|----------------|---------------------------------------------------|
| **PostgreSQL** | Structured metadata & user info                   |
| **Neo4j**      | Graph of COBOL components/modules                 |
| **Elasticsearch** | Textual search                                  |
| **Milvus**     | Vector search for semantic queries                |
| **Redis**      | Caching layer                                     |
| **OpenAI API** | External LLM processing                           |
| **GitHub API** | Retrieve COBOL source from repositories           |


## 🖼️ Mermaid: Container Diagram

```mermaid
flowchart TD
    subgraph Users
        ChatUI[Chat Interface: Web, CLI, Slack]
        AdminUI[Admin Interface]
    end

    ChatUI --> Backend_API[Backend API]
    AdminUI --> Backend_API

    subgraph Backend_API
        AuthAPI[Auth API]
        ParserAPI[Parser API]
        IndexingAPI[Indexing API]
        RetrievalAPI[Retrieval API]
        QAAPI[Q&A API]
        SpecGenAPI[SpecGen API]
        ConfigAPI[Configuration API]
        FeedbackAPI[Feedback API]
    end

    subgraph AICore
        Parser[Parser Module]
        Indexing[Indexing Module]
        Retrieval[Retrival Module]
        QA[QA Module]
        SpecGen[SpecGen Module]
        Feedback[Feedback Module]
    end

    Backend_API --> FileStorage[File Storage]
    Backend_API --> CacheDB
    Backend_API --> GitHub
    Backend_API --> AICore

    Indexing --> MetadataDB
    Indexing --> GraphDB
    Indexing --> SearchEngine
    Indexing --> VectorDB

    Retrieval --> MetadataDB
    Retrieval --> GraphDB
    Retrieval --> SearchEngine
    Retrieval --> VectorDB
    Retrieval --> RAG

    RAG --> Tools[Tools Inventory]

    QA --> Retrieval
    SpecGen --> Retrieval


```
