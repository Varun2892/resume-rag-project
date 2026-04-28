from src.resume_rag import load_resumes, chunk_documents, get_embeddings, store_in_db
from src.job_matcher import match_job

# Step 1: Load resumes
docs = load_resumes("data/resumes")

# Step 2: Chunk documents
chunks = chunk_documents(docs)

# Step 3: Create embeddings
embeddings = get_embeddings()

# Step 4: Store in vector DB
db = store_in_db(chunks, embeddings)

# Step 5: Load job description
with open("data/job_descriptions/jd1.txt", "r") as f:
    job_description = f.read()

# Step 6: Match resumes
results = match_job(db, job_description)

# Step 7: Print results
print(results)