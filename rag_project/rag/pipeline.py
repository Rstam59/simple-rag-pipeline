from rag.data_loader import load_documents
from rag.embedder import Embedder
from rag.retriever import Retriever
from rag.generator import Generator


class RAGPipeline:
    def __init__(self, doc_path, api_key):
        self.documents = load_documents(doc_path)
        self.embedder = Embedder()
        self.embeddings = self.embedder.embed(self.documents)
        self.retriever = Retriever(self.embeddings, self.documents)
        self.generator = Generator()

    def run(self, query):
        query_embedding = self.embedder.embed([query])[0]
        context_docs = self.retriever.retrieve(query_embedding)
        context = "\n\n".join(context_docs)
        return self.generator.generate(query, context)