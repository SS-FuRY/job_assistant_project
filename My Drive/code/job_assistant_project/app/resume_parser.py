import os
from pdfminer.high_level import extract_text
import docx

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_resume_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

def parse_resume(file_path):
    text = extract_resume_text(file_path)

    # Very basic parsing — replace with better NLP later
    keywords = {
        'skills': ['Python', 'SQL', 'Excel', 'Pandas', 'Flask', 'Machine Learning'],
        'experience': ['Intern', 'Developer', 'Analyst', 'Engineer'],
        'education': ['Bachelor', 'Master', 'PhD', 'University']
    }

    parsed = {key: [] for key in keywords}
    for section, words in keywords.items():
        for word in words:
            if word.lower() in text.lower():
                parsed[section].append(word)

    return parsed
