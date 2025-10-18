# LLM Automatic Response Generation

## About the project:
This project is a Python framework designed to automate the generation of responses to customer reviews (such as those found on platforms like TripAdvisor). It uses a flexible and extensible architecture that supports multiple Large Language Models (LLMs), allowing responses to be tailored to different personas and tones of voice, such as "sophisticated and formal" or "welcoming and informal."

The solution is ideal for companies that need to manage a large volume of online feedback, ensuring consistency, quality, and agility in customer interactions.

## Main Features:

* **Multi-Model Architecture**: Integrated support for:
    * OpenAI GPT-4o
    * Google Gemini 1.5 Pro
    * Meta Llama 3 (running locally via Ollama)
* **Abstract Model Contract**: The `LargeLanguageModelBaseContract` base class makes it easy to add new LLMs with minimal effort, ensuring that any new model follows the same interface.
* **Centralized Prompt Engineering**: The `PromptManager` class manages all personas and prompt types, decoupling prompt logic from model generation logic.
* **Security**: Securely manage API keys through environment variables with a `.env` file.
* **Easy to Use**: A single script (`main.py`) executes the logic, iterating over the configured models and personas to generate and display the responses.

