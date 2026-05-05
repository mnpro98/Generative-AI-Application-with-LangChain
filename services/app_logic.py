from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_community.tools import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from llms.gemini_llm import get_gemini_llm

REACT_TEMPLATE = """You are a fact-checking assistant. Your goal is to verify the accuracy of the claims in the provided text using available tools, and then produce a fact-check report. You have access to the following tools:

{tools}

Use the following format:

Text: the text containing claims you must fact-check
Thought: identify a specific claim in the text that needs verification
Action: the action to take, should be one of [{tool_names}]
Action Input: the search query to verify the claim
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times, once per claim)
Thought: I have verified all the key claims and can now produce a report
Final Answer: a structured fact-check report listing each claim and whether it is TRUE, FALSE, or UNVERIFIED, with a brief explanation for each. For every claim, you must include the source URL that was consulted to verify it, formatted as "Source: <url>".

Begin!

Text: {input}
Thought:{agent_scratchpad}"""


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


def fact_check(text):
    agent_prompt = PromptTemplate.from_template(REACT_TEMPLATE)

    params = (
        ("max_output_tokens", 1024),
        ("temperature", 0.5),
    )

    llm = get_gemini_llm(params=params)

    tools = [TavilySearchResults(max_results=1)]

    agent = create_react_agent(llm, tools, agent_prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
    )

    chain = (
            RunnableLambda(lambda x: {"input": x["text"]})
            | agent_executor
            | RunnableLambda(lambda x: x["output"])
    )

    response = chain.invoke({"text": text})
    print(response)
    return response