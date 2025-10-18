import ollama
from src.llm.Model_contract import LargeLanguageModelBaseContract


class MetaLlama3(LargeLanguageModelBaseContract):
    def __init__(self, model_name: str, temperature: float):
        super().__init__(model_name, temperature)
        self.__client = ollama

    def generate(self, system_prompt: str, user_input: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        try:
            response = self.__client.chat(
                model=self._model_name,
                messages=messages,
                options={'temperature': self._temperature}
            )
            return response['message']['content']

        except Exception as exception:
            print(f"Error while calling Ollama: {exception}")
            raise Exception("It was not possible to generate the expected answer with Llama.") from exception
