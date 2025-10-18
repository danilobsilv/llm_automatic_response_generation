# from src.llm.openai_gpt4 import OpenAiGPT4
from src.llm.google_gemini import GoogleGemini
from src.prompt_engineering.prompts_manager import PromptManager

def execute_agents():
    prompt_manager = PromptManager()

    # --- models ---
    modelos = {
        # "OpenAI": OpenAiGPT4(model_name="gpt-4o", temperature=0.8),
        "Gemini": GoogleGemini(model_name="gemini-2.5-pro", temperature=0.0)
    }

    user_comment = "A comida continua boa porém o atendimento em relação quando inaugurou não conseguiu manter o padrão. Os Garçons precisam ser mais profissionais e mais atenciosos."

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

                print(f"Response:\n{response}")

            except (ValueError, Exception) as e:
                print(f"Error: {e}")