# Why do we need Vector Database?

# How does Vector Database work?

## Storing

## Indexing

## Searching
Typically framed as a nearest-neighbor search problem like kNN
### 1. Naive solution:

#### Description:
- Compute the similarity scores between the query embedding & all vectors in the database (using metrics like L2 or cosine similarity)
- Rank all vectors by their similarity scores
- Return k vectors with the highest similarity scores

#### Pros:
- Simple
- Precise

#### Cons:
- Computationally heavy & slow => scaling base on number of record
=> Should be used only for small datasets

### 2. Approximate Nearest Neighbor

#### LSH - Locality-Sensitive Hashing (1999)

#### HNSW - Hierarchical Navigable Small World

# What are they use for?

## Examples:
- Search
- Recommendation
- Data Organization
- Information Retrieval
- Clustering
- Fraud Detection
- ...
