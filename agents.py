import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
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
    
    # Define System Prompt
    system_instruction = f"""
    You are an expert multi-agent AI educational system for CLI Robotic School DHA Quetta.
    Target Student Age Group: {age_group}.
    
    Provide a detailed, structured response based on the syllabus:
    1. Curriculum Breakdown & Pedagogical Method
    2. Coding / Technical Steps (Block coding or Python/C++ code)
    3. Hardware, Sensors & Project Guidance
    """
    
    full_query = f"{system_instruction}\n\nUser Question: {user_query}"
    
    # Initialize Agent using standard execution pipeline
    agent = initialize_agent(
        tools=[search],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    response = agent.run(full_query)
    return response
