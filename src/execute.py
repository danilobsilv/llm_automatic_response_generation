from src.llm.openai_gpt4 import OpenAiGPT4
from src.llm.google_gemini import GoogleGemini
from src.llm.meta_llama3 import MetaLlama3
from src.prompt_engineering.prompts_manager import PromptManager


def execute_agents():
    prompt_manager = PromptManager()

    # --- models ---
    models_temperature = 0.7
    modelos = {
        "OpenAI": OpenAiGPT4(model_name="gpt-4o", temperature=models_temperature),
        "Gemini": GoogleGemini(model_name="gemini-2.5-pro", temperature=models_temperature),
        "Llama3": MetaLlama3(model_name="llama3", temperature=models_temperature)
    }

    user_comment = "A comida continua boa porém o atendimento em relação quando inaugurou não conseguiu manter o padrão. Os Garçons precisam ser mais profissionais e mais atenciosos."

    response_list = []
    for model_name, model_instance in modelos.items():
        print(f"\n{'=' * 20} using model: {model_name} {'=' * 20}")

        for persona in ["sophisticate_and_formal", "welcoming_and_informal"]:
            print(f"\ntesting Persona: {persona.replace('_', ' ').title()}")

            try:
                system_prompt = prompt_manager.get_prompt(
                    prompt_type="zero_shot",
                    persona=persona
                )

                response = model_instance.generate(
                    system_prompt=system_prompt,
                    user_input=user_comment
                )
                response_list.append(response)

                for resp in response_list:
                    print("RESPONSE: ", resp)

            except (ValueError, Exception) as e:
                print(f"Error: {e}")

