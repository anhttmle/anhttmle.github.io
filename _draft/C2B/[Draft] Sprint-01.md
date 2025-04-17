# Week 1: Finalize Specs & Architecture Design
## Target modules:
- _Architecture_
- _Userflow_
- _Type of user_

## Task:
- _Finalize user_
- _Architecture Design_
- _Userflow_
- Prepare Infra
  - Deploy Dify
  - Deploy Metadata DB (SQL Lite)
  - _Deploy File Storage (Local File System)_
  - _Deploy VectorDB (Milvus Lite)_

# Week 2: Component Design & Interface Development
## Target modules:
- COBOL Parser module: convert from COBOL repo to appropriate artifact
  - DIVISION
  - Section (multi-level)
  - Line
  - Summary
- Metadata DB: store metadata of chunk, summary, file, repo,...
- Vector DB: similar search for term, chunk, summary,...
- Indexing Module: index data that convert from COBOL parser to appropriate database
- Retrieval Module: retrieve context by request to pre-defined Dify workflow
- API Gateway: distribute workload to coresponding module & centralize interface

## Task: 
- Design COBOL parser module
- Define DB schema
  - Metadata DB
  - Vector DB
- Indexing
  - Define
  - Develop 
- Develop Tool Inventory
  - Tool retrieve from VectorDB
  - Tool retrieve from MetadataDB
- Retrieval pipeline
  - Define 
  - Publish on Dify
  - Develop Retrieval module call from Dify
- API gateway
  - Define
  - Develop
