# Week 1: Finalize Specs & Architecture Design
## Target modules:
- Architecture
- Userflow
- Type of user

## Task:
- Finalize user
- Architecture Design
- Userflow
- Prepare Infra
  - Deploy Dify
  - Deploy Metadata DB (SQL Lite)
  - Deploy File Storage (Local File System)
  - Deploy VectorDB (Milvus Lite)

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
