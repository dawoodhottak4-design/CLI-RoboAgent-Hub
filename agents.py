from crewai import Agent
from crewai_tools import DuckDuckGoSearchTool
from langchain_openai import ChatOpenAI
import os

# Initialize DuckDuckGo Search Tool
search_tool = DuckDuckGoSearchTool()

def get_groq_llm():
    """Configures Groq LLM with openai/gpt-oss-120b using environment variables or Streamlit secrets"""
    api_key = os.getenv("GROQ_API_KEY")
    
    return ChatOpenAI(
        openai_api_base="https://api.groq.com/openai/v1",
        openai_api_key=api_key,
        model_name="openai/gpt-oss-120b",
        temperature=0.7
    )

def create_robotics_agents():
    llm = get_groq_llm()

    # 1. Curriculum Specialist Agent (Age-wise planning)
    curriculum_agent = Agent(
        role="CLI Robotics Curriculum Specialist",
        goal="Design structured, age-appropriate robotics and AI curriculum modules based on CLI Robotic School DHA Quetta syllabus (Ages 3 to 16).",
        backstory="""You are an expert educational technologist and robotics curriculum director at CLI Robotic School DHA Quetta. 
        You specialize in breaking down complex concepts—from tactile play-based logic for 3-5 year olds to advanced Python, C++, and computer vision for teenagers—into structured lessons.""",
        verbose=True,
        tools=[search_tool],
        llm=llm
    )

    # 2. Technical Coding & AI Tutor Agent
    coding_agent = Agent(
        role="Robotics Coding & AI Instructor",
        goal="Provide step-by-step programming logic, block coding guides, Python/C++ code snippets, and machine learning concepts.",
        backstory="""You are a senior software engineer and robotics coding expert. You help students transition from block-based programming (ages 6-10) 
        to advanced Python and C++ text-based coding, autonomous robot navigation, and multi-sensor integration.""",
        verbose=True,
        tools=[search_tool],
        llm=llm
    )

    # 3. Hardware & Project Mentor Agent
    hardware_agent = Agent(
        role="Hardware & Capstone Project Mentor",
        goal="Guide students on mechanical builds, sensors (touch, tilt), structural engineering, and national/international robotics competitions.",
        backstory="""You are a veteran robotics hardware engineer who guides students through building motorized structures, gears, levers, 
        and preparing winning capstone projects and competition entries.""",
        verbose=True,
        tools=[search_tool],
        llm=llm
    )

    return curriculum_agent, coding_agent, hardware_agent
