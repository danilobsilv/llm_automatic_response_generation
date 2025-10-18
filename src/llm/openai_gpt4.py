from src.llm.Model_contract import LargeLanguageModelBaseContract
from openai import OpenAI
from src.config import OPENAI_API_KEY


class OpenAiGPT4(LargeLanguageModelBaseContract):

    def __init__(self, model_name: str = "gpt-4o", temperature: float = 0.5):
        super().__init__(model_name, temperature)
        self.__client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, system_prompt: str, user_input: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        try:
            response = self.__client.chat.completions.create(
                model=self._model_name,
                messages=messages,
                temperature=self._temperature
            )
            return response.choices[0].message.content

        except Exception as exception:
            print(f"Error while calling OPENAI API: {exception}")
            raise Exception("It was not possible to generate the expected answer.") from exception
