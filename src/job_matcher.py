from collections import defaultdict
import re

# Extract skills
def extract_skills(text):
    skills = ["Python", "Java", "SQL", "Machine Learning", "AI", "NLP"]
    return [s for s in skills if s.lower() in text.lower()]

# Extract experience
def extract_experience(text):
    match = re.search(r'(\d+)\+?\s+years', text.lower())
    return int(match.group(1)) if match else 0

# Extract name (first line)
def extract_name(text):
    import re
    match = re.search(r'Name:\s*([A-Za-z ]+?)\s+Skills', text)
    
    if match:
        name = match.group(1)
        return " ".join(name.split())   # 🔥 removes extra spaces
    
    return "Unknown"

def match_job(db, job_description, k=10):
    results = db.similarity_search(job_description, k=k)

    grouped = defaultdict(list)

    # 🔹 Group chunks by resume file
    for doc in results:
        path = doc.metadata.get("source")
        grouped[path].append(doc.page_content)

    final_results = []

    for path, texts in grouped.items():
        full_text = " ".join(set(texts))

        name = extract_name(full_text)
        skills = extract_skills(full_text)
        exp = extract_experience(full_text)

        # 🔥 scoring
        score = min(len(skills) * 20 + exp * 5, 100)

        final_results.append({
            "candidate_name": name,
            "resume_path": path,
            "match_score": score,
            "matched_skills": skills,
            "experience_years": exp,
            "relevant_excerpts": full_text[:150],
            "reasoning": f"{len(skills)} skills matched, {exp} years experience"
        })

    # 🔹 Sort by score
    return sorted(final_results, key=lambda x: x["match_score"], reverse=True)