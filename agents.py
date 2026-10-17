import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools import DuckDuckGoSearchRun

def get_groq_llm():
    api_key = os.getenv("GROQ_API_KEY")
    return ChatOpenAI(
        openai_api_base="https://api.groq.com/openai/v1",
        openai_api_key=api_key,
        model_name="openai/gpt-oss-120b",
        temperature=0.7
    )

def run_robotics_consultation(age_group, user_query):
    llm = get_groq_llm()
    search = DuckDuckGoSearchRun()
    
    # Prompt defining the CLI Robotic School DHA Quetta expertise
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are an expert multi-agent AI educational system for CLI Robotic School DHA Quetta. 
        You specialize in the curriculum from Ages 3 to 16 (ranging from tactile play-based logic to Python, C++, and Computer Vision).
        The current student/teacher target level is: {age_group}.
        Provide a comprehensive, structured response covering:
        1. Curriculum & Pedagogical Approach
        2. Coding / Technical Instructions (Block coding, Python, or C++ snippets where applicable)
        3. Hardware, Sensors & Project Guidance
        Use web search if needed to verify technical details."""),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    tools = [search]
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    response = agent_executor.invoke({"input": user_query})
    return response["output"]
