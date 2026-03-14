from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class Generator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "openai/gpt-oss-20b"

    def generate(self, question , chunks):
        context = "\n\n".join([c["text"] for c in chunks ])
        prompt = f"""
            You are a document question-answering assistant.

            Use ONLY the information from the provided context to answer the question.

            If the answer is not contained in the context, respond with:
            "I could not find the answer in the provided documents."

            Context:
            {context}

            Question:
            {question}

            Answer clearly and concisely.
            """

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role":"user","content":prompt}
            ]
        )

        return completion.choices[0].message.content