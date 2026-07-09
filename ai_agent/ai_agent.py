import os
from dotenv import load_dotenv
from openai import OpenAI
from ai_agent.prompts import SYSTEM_PROMPT
from ai_agent.config import MODEL, BASE_URL


def client_setup():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("No OpenRouter API Key Found")

    client = OpenAI(
        base_url=BASE_URL,
        api_key=api_key,
    )
    return client

def get_completion(client, messages, model):
    return client.chat.completions.create(model=model, messages=messages)

def parse_args():
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("default_prompt", type=str, help="Default prompt")
    args = parser.parse_args()
    return args

def build_user_prompt(clothing, forecast_tomorrow):
    user_prompt = f"""
Convert the list of recommended clothing ({clothing}) into markdown text that can be parsed into HTML using an static site generator. Also add some insights on the weather readout from OpenWeather ({forecast_tomorrow})"""
    return user_prompt

def ai_agent_call(clothing, forecast_tomorrow):
    client = client_setup()
    user_prompt = build_user_prompt(clothing, forecast_tomorrow)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ] 

    completion = get_completion(client, messages, MODEL)
    return completion.choices[0].message.content