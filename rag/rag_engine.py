class RAGEngine:

    def __init__(self, embedder, vector_store, llm):
        self.embedder = embedder
        self.store = vector_store
        self.llm = llm

    def generate(self, query):

        query_emb = self.embedder.encode([query])[0]
        context_docs = self.store.search(query_emb)

        context = "\n".join(context_docs)

        prompt = f"""
        Evidence:
        {context}

        Analyze patient safety risks in:
        {query}

        Provide structured explanation.
        """

        return self.llm.generate(prompt)
