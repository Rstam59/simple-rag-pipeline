from rag.pipeline import RAGPipeline
import os

if __name__ == '__main__':
    api_key = os.getenv("OPENAI_API_KEY")
    doc_path = "/Users/rustamalizada/Desktop/simple-rag-pipeline/rag_project/docs"
    pipeline = RAGPipeline(doc_path, api_key)
    
    while True:
        query = input("Ask a question (or 'exit'): ")
        if query.lower() == 'exit':
            break
        answer = pipeline.run(query)
        print("\nAnswer:\n", answer, "\n")
