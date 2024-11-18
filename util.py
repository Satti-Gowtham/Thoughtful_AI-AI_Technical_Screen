import json
from openai import OpenAI, Stream

class Util():
    def __init__(self, api_key, base_url, model):
        self.model = model
        self.api_key = api_key
        self.base_url = base_url
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def load_dataset(self, data_file: str) -> dict:
        with open(data_file) as dataset:
            return json.load(dataset)

    def get_answer(self, query: str, data: list) -> str | Stream:
        # First check if the answer is in the dataset
        for qna in data:
            if query.lower() == qna['question'].lower():  # Case insensitive comparison
                return qna['answer']
        
        # If not found, ask the model
        return self.query_llm(query, data)

    def query_llm(self, query: str, data: list) -> Stream:
        context = "\n".join([f"Q: {entry['question']}\nA: {entry['answer']}" for entry in data])
        
        prompt = f"""
        You are a helpful assistant for a customer support chatbot for Thoughtful AI. Answer the following questions:

        - If the question matches any of the frequently asked questions below, provide the corresponding answer. Output the only answer from the provided data and do not output the question.
        - If the question does not match any of the frequently asked questions, provide a relevant, generic response related to Thoughtful AI.

        Below are some frequently asked questions (FAQs):
        {context}
        """

        # Call the OpenAI API with streaming enabled
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": query}],
            temperature=0.7,
            stream=True
        )

        return response
