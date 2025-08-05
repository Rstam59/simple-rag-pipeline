from openai import OpenAI

class Generator:
    def __init__(self):
        self.client = OpenAI()  # uses env variable

    def generate(self, query, context):
        prompt = (
            f"You are a helpful assistant. Only answer based on the given context.\n\n"
            f"If the answer is not present in the context, just respond with \"I don't know.\"\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\nAnswer:"
        )

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Answer strictly based on the provided context. Say 'I don't know.' if unsure."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()
