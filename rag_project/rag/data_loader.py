import os

def load_documents(path):
    docs = []
    for filename in os.listdir(path):
        if filename.endswith(".txt") or filename.endswith(".md"):
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
                docs.append(file.read())
    return docs

