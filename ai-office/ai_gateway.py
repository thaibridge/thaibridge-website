import os
from openai import OpenAI

class AIGateway:
    def __init__(self, provider="deepseek"):
        self.provider = provider

        if self.provider == "deepseek":
            api_key = os.getenv("DEEPSEEK_API_KEY")
            if not api_key:
                raise ValueError("Missing DEEPSEEK_API_KEY. 请先设置 DeepSeek API Key。")

            self.client = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com"
            )
            self.model = "deepseek-chat"

        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def chat(self, system_prompt, user_prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
