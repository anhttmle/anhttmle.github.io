# ---- Auth API ----

## 1. Login
## 2. Logout
## 3. View Profile & User's Setting
- Profile:
  - Username
  - Password
- User Setting:
  - Language
  - Theme
## 4. Update User's Setting
## 5. Register

# ---- Parser API ----

## 1. Upload Repo
## 2. Upload Biz Context
## 3. Start "Parsing Job" for a Repo
## 4. Get "Parsing Job" status by Job Id
## 5. Stop "Parsing Job" by Job Id
## 6. Get list of Running "Parsing Job"

# ---- Indexing API ----

## 1. Start "Chunking Job" which convert document to chunks
## 2. Start "Extract metadata Job" which extract metadata from document
## 3. Start "Extract Graph Knowledge Job" which extract entities from document
## 4. Start "Insert text Job" which insert document to Text Search Engine
## 5. Get Job status by Job Id and type
- Job type:
  - Chunking
  - ExtractMetadata
  - ExtractGraphKnowledge
  - InsertText
## 6. Stop Job by Job Id
## 7. Get list of Running Jobs

# ---- QA API ----

## 1. Create Conversation
## 2. Delete Conversation
## 3. Get List of Conversation by User
## 4. Start "Query Job" which is request a question to Assistant
## 5. Get "Query Job" status by Job Id
## 6. Stop "Query Job" by Job Id
## 7. Get list of Running "Query Job"

# ---- Sepcs Gen API ----

## 1. Start "Gen Specs Job" which generate specificatio from repo's source code
## 2. Get "Gen Specs Job" status by Job Id
## 3. Stop "Gen Specs Job" by Job Id
## 4. Download Specs in Markdown
## 5. Start "Gen Sub Specs Job" which is zoom into a specific section of generated Specs or SubSpecs and request Assistant gen a SubSpecs
## 6. Get "Gen Sub Specs Job" status by Job Id
## 7. Stop "Gen Sub Specs Job"
## 8. Get list Generated Specs
- Root Note: Specs
- Intermediate Node: Sub Specs
- Leaf Node: Sub Specs
## 9. Get Specs by Spec id
## 10. Get Sub Specs by SubSpecs Id


# ---- Configuration API ----

## 1. Create Object Configuration
## 2. Update Object Configuration

# ---- Feedback API ----

## 1. Rating for an answer
## 2. Text feedback for an answer
## 3. Refine an answer

# ---- Retrieval API ----

## 1. Create "Chat Retrieval Job" which is execute flow of retrieve context for a user's question
## 2. Get "Chat Retrieval Job" status by Job Id
## 3. Stop "Chat Retrieval Job" by Job Id
## 4. Get list of Running "Chat Retrieval Job"
