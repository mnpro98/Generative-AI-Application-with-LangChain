import os
from dotenv import load_dotenv
from functools import lru_cache
from langchain_anthropic import ChatAnthropic

load_dotenv()

@lru_cache()
def get_claude_llm(model_id="claude-haiku-4-5-20251001", params: tuple = None) -> ChatAnthropic:
    default_params = {
        "max_tokens": 512,
        "temperature": 0.7,
    }

    if params:
        default_params.update(dict(params))

    return ChatAnthropic(
        model=model_id,
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
        **default_params
    )