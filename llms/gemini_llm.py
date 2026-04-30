import os
from dotenv import load_dotenv
from functools import lru_cache
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@lru_cache()
def get_gemini_llm(model_id="gemini-3.1-flash-lite-preview", params: tuple = None) -> ChatGoogleGenerativeAI:
    default_params = {
        "max_output_tokens": 512,
        "temperature": 0.7,
    }

    if params:
        default_params.update(dict(params))

    return ChatGoogleGenerativeAI(
        model=model_id,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        **default_params
    )