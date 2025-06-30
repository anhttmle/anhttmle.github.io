# API Gateway Plan for C2B Virtual Assistant

## 1. Auth API
- Login
- Logout
- Register
- View Profile & User's Setting
  - Profile: Username, Password
  - User Setting: Language, Theme
- Update User's Setting

## 2. Parser API
- Upload Repo
- Upload Biz Context
- Start Parsing Job for a Repo
- Get Parsing Job status by Job Id
- Stop Parsing Job by Job Id
- Get list of Running Parsing Job

## 3. Indexing API
- Start Chunking Job (convert document to chunks)
- Start Extract Metadata Job
- Start Extract Graph Knowledge Job
- Start Insert Text Job
- Get Job status by Job Id and type (Chunking, ExtractMetadata, ExtractGraphKnowledge, InsertText)
- Stop Job by Job Id
- Get list of Running Jobs

## 4. QA API
- Create Conversation
- Delete Conversation
- Get List of Conversation by User
- Start Query Job (request a question to Assistant)
- Get Query Job status by Job Id
- Stop Query Job by Job Id
- Get list of Running Query Job

## 5. Specs Gen API
- Start Gen Specs Job (generate specification from repo's source code)
- Get Gen Specs Job status by Job Id
- Stop Gen Specs Job by Job Id
- Download Specs in Markdown
- Start Gen Sub Specs Job (zoom into a specific section of generated Specs or SubSpecs and request Assistant gen a SubSpecs)
- Get Gen Sub Specs Job status by Job Id
- Stop Gen Sub Specs Job
- Get list Generated Specs (Root Node: Specs, Intermediate Node: Sub Specs, Leaf Node: Sub Specs)
- Get Specs by Spec id
- Get Sub Specs by SubSpecs Id

## 6. Configuration API
- Create Object Configuration
- Update Object Configuration

## 7. Feedback API
- Rating for an answer
- Text feedback for an answer
- Refine an answer

## 8. Retrieval API
- Create Chat Retrieval Job (execute flow of retrieve context for a user's question)
- Get Chat Retrieval Job status by Job Id
- Stop Chat Retrieval Job by Job Id
- Get list of Running Chat Retrieval Job

---

## Mapping với UI
- /repos: Upload, list, delete repo, parse, specs gen
- /specs: List, view, download, edit specs, sub-specs
- /assistant: Q&A, conversation, feedback, refine
- /profile: get/update profile, language, theme, password
- /analytics: dashboard, job status
- /config: object config
- /feedback: answer rating, text feedback, refine
- /retrieval: context retrieval for QA 
