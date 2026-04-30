import os
from dotenv import load_dotenv
from functools import lru_cache
#from langchain.chains import LLMChain  # Still using this for backward compatibility

from langchain_ibm import WatsonxLLM

load_dotenv()

@lru_cache()
def get_watson_llm(model_id="ibm/granite-3-3-8b-instruct", params=None) -> WatsonxLLM:
    """
    Factory function to initialize WatsonxLLM using environment variables.
    """

    default_params = {
        "max_new_tokens": 512,
        "min_new_tokens": 1,
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "decoding_method": "sample"
    }

    if params:
        default_params.update(dict(params))

    # Create LLM directly
    return WatsonxLLM(
        model_id=model_id,
        url=os.getenv("WATSONX_URL"),
        apikey=os.getenv("WATSONX_API_KEY"),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        params=default_params
    )
