from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent
from tools import search_tool, wiki_tool, save_tool
from langchain.agents import AgentExecutor


import os
import sys
import time
try:
    import openai  # For catching specific OpenAI exceptions
except Exception:  # pragma: no cover
    openai = None

load_dotenv()

# Ensure OpenAI API key is available for the underlying client
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    print(
        "Missing ANTHROPIC_API_KEY. Please create a .env file with ANTHROPIC_API_KEY=your_key"
    )
    sys.exit(1)
else:
    print("ANTHROPIC_API_KEY is set")


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

model_name = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-1-20250805")
llm = ChatAnthropic(model=model_name, api_key=ANTHROPIC_API_KEY)

#response = llm.invoke("What is the capital of France?")
#print(response)

# takes the output and parses it into a pydantic structured format
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a research assistant that will help generate a research paper. Answer the user query and use neccessary tools. Wrap the output in this format and provide no other text\n{format_instructions}"),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[search_tool, wiki_tool, save_tool]
)

#executes the agent
agent_executor = AgentExecutor(agent=agent, tools=[search_tool, wiki_tool, save_tool], verbose=True)
raw_response = agent_executor.invoke({"query": "What is the capital of France?"})
try:
    strucutred_response = parser.parse(raw_response.get("output", "")[0]["text"])
    print(strucutred_response.topic)
   # print(strucutred_response.summary)
    #print(strucutred_response.sources)
    #print(strucutred_response.tools_used)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
    print("Raw Response - ", raw_response)






