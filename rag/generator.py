from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class Generator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "groq/compound-mini"

    def generate(self, question , chunks):
        context = "\n\n".join([c["text"] for c in chunks ])
        prompt = f"""
        You are a helpful assistant.

        Answer the question ONLY using the provided context.

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