from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from llms.gemini_llm import get_gemini_llm


def summarize(text):
    params = (
        ("max_output_tokens", 128),
        ("temperature", 0.5),
    )

    template = """Summarize the following text: "{text}"
    """
    prompt = PromptTemplate.from_template(template)

    llm = get_gemini_llm(params=params)

    chain = (
            RunnableLambda(lambda inputs: prompt.format(**inputs))
            | llm
            | StrOutputParser()
    )

    response = chain.invoke({"text": text})
    print(response)
    return response