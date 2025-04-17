# Architecture
```mermaid
flowchart TD
    subgraph Users
        ChatUI[Chat Interface: Web, CLI, Slack]
        AdminUI[Admin Interface]
    end

    ChatUI --> API_Gateway[API Gateway]
    AdminUI --> API_Gateway

    subgraph API_Gateway
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
        Q&A[Q&A Module]
        SpecGen[SpecGen Module]
        Feedback[Feedback Module]
    end

    subgraph RAG
        PredefineFlow
    end

    subgraph AI_Databases
        MetadataDB
        GraphDB
        SearchEngine
        VectorDB
    end

    subgraph Tools[Tools Inventory]
        RetrieveMetadata
        RetrieveNeighbordata
        FulltextSearch
        SemanticSearch

        RetrieveMetadata --> MetadataDB
        RetrieveNeighbordata --> GraphDB
        FulltextSearch --> SearchEngine
        SemanticSearch --> VectorDB
    end

    API_Gateway --> FileStorage[File Storage]
    API_Gateway --> CacheDB
    API_Gateway --> Git
    API_Gateway --> AICore

    Parser --> Indexing
    Parser --> FileStorage
    
    Indexing --> MetadataDB
    Indexing --> GraphDB
    Indexing --> SearchEngine
    Indexing --> VectorDB

    Retrieval --> RAG
    RAG --> Tools
    
    Q&A --> Retrieval
    SpecGen --> Retrieval


```

# Strategy

