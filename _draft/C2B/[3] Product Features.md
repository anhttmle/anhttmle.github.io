# 1. Configuration
- Currently we only support using openAI models
<img width="317" alt="image" src="https://github.com/user-attachments/assets/bcf93f8b-3248-432e-b524-96d7cc7716f9" />

# 2. Authorization
- User can login and using as separate session, also help clarify feedback among users
<img width="1557" alt="image" src="https://github.com/user-attachments/assets/82ef650f-e4ee-4335-b945-ff99faae209f" />

# 4. Indexing data
   - Upload/Index Cobol Repo (Zip file)
<img width="312" alt="image" src="https://github.com/user-attachments/assets/0419c1e0-3a23-43e6-ba84-a125a72c50f1" />

   - Summarize (Backend)
   - Chunking (Backend)
   - Semantic Storing (Backend)

   - Delete Indexed data
<img width="312" alt="image" src="https://github.com/user-attachments/assets/6317d2d0-356c-4c04-9869-7bbc79a112f2" />


   - Visualize Indexing Status
<img width="312" alt="image" src="https://github.com/user-attachments/assets/57560eb1-024e-4d2a-8805-c909ecb3e844" />

# 5. Answer Generation
- Generate data base on user question
<img width="1224" alt="image" src="https://github.com/user-attachments/assets/ccf17aaf-cb73-493a-a542-31511f860df1" />

# 6. Feedback
### A. Tag on Reference
- Users can label references as relevant or irrelevant.
<img width="481" alt="image" src="https://github.com/user-attachments/assets/c825d36f-b078-4344-a968-5b783aad0128" />

> Helps us train the AI to choose better context next time.

### B.👍 Up Vote / 👎 Down Vote on Assistant’s Answer

- Up vote/Down vote:
<img width="1207" alt="image" src="https://github.com/user-attachments/assets/d529c721-e738-4bbe-94a2-48bda3d5affd" />

- Quick way to rate the overall helpfulness of the response:
<img width="393" alt="image" src="https://github.com/user-attachments/assets/898684ae-80aa-4bca-be02-346d557dcaaa" />


> Useful for automated performance tracking.

### C. 💬 Add Comment on Reference ➝ feeds Few-shot Prompt


### D. 💬 Add Comment on Answer ➝ feeds Few-shot Prompt
<img width="470" alt="image" src="https://github.com/user-attachments/assets/0faf4a26-0850-421f-80a8-90b0eb8f71f5" />

    Users can explain what the Assistant got wrong or right.
    We use these comments to fine-tune behavior in similar future cases.
