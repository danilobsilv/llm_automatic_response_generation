from abc import ABC, abstractmethod


class LargeLanguageModelBaseContract(ABC):
    def __init__(self, model_name: str, temperature: float = 0.5):
        self._model_name = model_name
        self._temperature = temperature


    @abstractmethod
    def generate(self, system_prompt: str, user_input: str) -> str:
        pass
