# 1. System Context:

### What is the name or high-level description of the system you're building?
> (e.g., A web app that helps people manage personal finances)

- The System is an API package, working as Virtual Assistant for whole team who working on migrating COBOL project to JAVA.
   
### Who are the primary users or roles interacting with the system
> (e.g., End users, admins, 3rd-party services, etc.)

- The roles of the End Users (the team) are:
  - COBOL Engineer (a.k.a COBOL-E): Reading COBOL source code and support COBOL BA on making documents & specs (review, describe feature)
  - COBOL Business Analyst (a.k.a COBOL-BA): Making document & specs, interact with COBOL-E to have right understanding
  - JAVA Business Analyst (a.k.a COBOL-BA): Making document & specs for JAVA system, interact with COBOL-BA to have right understanding
  - JAVA Engineer (a.k.a JAVA-E): who will develop new JAVA system base on COBOL documents & Spec. Will interact with COBOL-E & COBOL-BA to understand detail and develop correctly
  - JAVA Product Owner (a.k.a JAVA-PO)
  - JAVA Technical Leader (a.k.a JAVA-TL)
- Administrator or Operator:
  - Will provide account (with authorization) to each member
  - Will adjust setting of system to help the Virtual Assistant smarter
 
### What are the main goals or value your system provides to these users?
> (e.g., track spending, set budgets, get insights, automate savings…)

- COBOL-E can provide COBOL source code (github/gitlab URL or upload a zip file) and COBOL-BA provide document/specs template. And the Virtual Assistant can help building documentation/specs
- Answer the question from the team to help them understanding the document/specs. From that, they will develop new JAVA project

### Are there any external systems or services your system needs to integrate with?
> (e.g., Bank APIs, payment gateways, identity providers…)

- Github: to access to COBOL source code (optional)

# 2. Container:
### What are the main high-level parts of your system?

Examples:

    Backend API
    Frontend Web UI
    Database
    Worker for background tasks
    Vector DB / AI service
    File storage

### How do users interact with the system?

    Do they use a Web UI, or is everything through API calls (e.g., Postman, CLI tools)?
    Will different roles use different interfaces?

### What internal services/modules are planned in the API?

Examples:

    Auth service
    COBOL parser
    Spec/documentation generator
    Q&A engine (LLM-based?)
    GitHub integration service

### What external services or databases are needed?

Examples:

    PostgreSQL for user data
    Vector DB for embedding & retrieval
    Redis for caching
    GitHub API
    OpenAI or internal LLM?
