import re

SKILLS_DB = ["Python", "Java", "SQL", "Machine Learning", "AI", "NLP", "TensorFlow", "Django"]

def extract_skills(text):
    return [skill for skill in SKILLS_DB if skill.lower() in text.lower()]


def extract_experience(text):
    match = re.search(r'(\d+)\+?\s+years', text.lower())
    return int(match.group(1)) if match else 0