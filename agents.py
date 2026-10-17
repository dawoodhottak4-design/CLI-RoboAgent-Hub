import os
from langchain_openai import ChatOpenAI
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
    
    # Pre-fetch supplementary search context safely if needed
    search_context = ""
    try:
        search = DuckDuckGoSearchRun()
        search_results = search.run(f"CLI robotics school {age_group} {user_query}")
        if search_results:
            search_context = f"\n\n### Additional Online Context:\n{search_results}"
    except Exception:
        search_context = ""

    # Comprehensive Prompt for Multi-Agent System reasoning
    prompt = f"""
    You are an expert multi-agent AI educational and robotics assistant for CLI Robotic School DHA Quetta.
    
    Current Target Student Age Group: {age_group}
    User Query / Request: {user_query}
    {search_context}

    Please provide a detailed, highly structured, step-by-step response tailored to the CLI Robotic School syllabus:
    
    1. 🧠 **Curriculum & Pedagogical Method**: Age-appropriate learning objectives, logic breakdown, and teaching strategy.
    2. 💻 **Coding / Technical Content**: Block coding logic (for younger ages 3-10) or Python / C++ code snippets with detailed comments (for ages 11-16).
    3. ⚙️ **Hardware, Mechanics & Sensors**: Practical building tips, sensors (touch, tilt, ultrasonic, vision), and project execution guide.
    """

    response = llm.invoke(prompt)
    return response.content
