from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from tools import get_tavily_tool

def get_agent(google_key, tavily_key):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=google_key,
        temperature=0.5
    )

    search_tool = get_tavily_tool(tavily_key)
    tools = [search_tool]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are TravelMate, an expert travel planning assistant. "
            "Plan detailed, realistic itineraries using real data from the search tool. "
            "Format your response in clean Markdown."
        )
    )
    
    return agent