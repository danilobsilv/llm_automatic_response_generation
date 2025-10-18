from src.config import GOOGLE_GEMINI_API_KEY
from src.llm.Model_contract import LargeLanguageModelBaseContract
import google.generativeai as google_ai
from google.generativeai.types import GenerationConfigDict


class GoogleGemini(LargeLanguageModelBaseContract):
    def __init__(self, model_name: str = "gemini-2.5-pro", temperature: float = 0.5):
        super().__init__(model_name, temperature)
        try:
            google_ai.configure(
                api_key=GOOGLE_GEMINI_API_KEY
            )
            self.__client = google_ai.GenerativeModel(
                model_name = self._model_name,
                generation_config= {"temperature": self._temperature}
            )

        except Exception as exception:
            raise ValueError(f"Error while configurating Google GEMINI API: ", str(exception))

    def generate(self, system_prompt: str, user_input: str) -> str:
        prompt = f"{system_prompt}\n\n---\n\n{user_input}"

        try:
            response = self.__client.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"❌ Error calling Gemini API: {e}")
            raise Exception("Could not generate an answer.") from e