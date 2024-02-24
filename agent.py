import os
import getpass

if "SERPAPI_API_KEY" not in os.environ:
    os.environ["SERPAPI_API_KEY"] = getpass.getpass("Provide your Search API Key\n")

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
 
# First, let's load the language model we're going to use to control the agent.

llm = ChatGoogleGenerativeAI(model="gemini-pro") 
# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)
 
# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
 
# Now let's test it out!
agent.invoke("最近五天杭州温度最高是多少？把它乘3是多少？")

# 我需要先搜索杭州最近五天的温度，然后从中找出最高的，再乘以3。
# Action: Search
# Action Input: 杭州最近五天天气
# Observation: {'type': 'weather_result', 'temperature': '36', 'unit': 'Fahrenheit', 'precipitation': '10%', 'humidity': '84%', 'wind': '10 mph', 'location': '中国浙江省杭州市', 'date': 'Saturday', 'weather': 'Cloudy'}
# Thought:我需要把温度从华氏温度转换为摄氏温度。
# Action: Calculator
# Action Input: (36 - 32) * 5 / 9
# Observation: Answer: 2.2222222222222223
# Thought:杭州最近五天的最高温度是2.22摄氏度。
# Action: Calculator
# Action Input: 2.22 * 3
# Observation: Answer: 6.66
# Thought:杭州最近五天的温度最高是2.22摄氏度，乘以3是6.66。
# Final Answer: 6.66