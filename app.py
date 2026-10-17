import streamlit as st
import os
from crewai import Crew, Process
from agents import create_robotics_agents
from multiprocessing import Queue

# Streamlit Page Config
st.set_page_config(
    page_title="CLI RoboAgent Hub | DHA Quetta",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 CLI RoboAgent Hub - DHA Quetta")
st.markdown("### Multi-Agent Educational & Robotics Assistant (Beginner to Advanced)")

# Sidebar for Configuration & Age Group selection
st.sidebar.header("⚙️ Configuration & Navigation")

# Load API Key securely from Streamlit Secrets
groq_api_key = None
if "GROQ_API_KEY" in st.secrets:
    groq_api_key = st.secrets["GROQ_API_KEY"]
else:
    groq_api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key
else:
    st.warning("⚠️ Please provide your Groq API Key in Streamlit Secrets or sidebar to run the agents.")

# Age Group Selection mapped with CLI Robotic School Syllabus
age_group = st.sidebar.selectbox(
    "Select Student Age Group / Level:",
    [
        "Age 3-5: Robotics Discovery (Tactile Learning & Logic)",
        "Age 6-8: Junior Robotics (Block Coding & Motorized Models)",
        "Age 9-10: Robotics Builder (Intermediate Block Coding & Multi-Sensors)",
        "Age 11-13: AI Innovator (Python, Basic ML & Autonomous Navigation)",
        "Age 14-16: Advanced Robotics & AI (C++, Computer Vision & Capstone Projects)"
    ]
)

# Main Query Input
user_query = st.text_area(
    "What would you like to learn, build, or teach today?",
    placeholder="e.g., Create a lesson plan and Python code for a line-following autonomous robot using ultrasonic sensors."
)

if st.button("🚀 Run Multi-Agent Robotics Session", type="primary"):
    if not groq_api_key:
        st.error("Please configure your Groq API Key first!")
    elif not user_query.strip():
        st.error("Please enter a query or topic!")
    else:
        with st.spinner("🤖 CrewAI Agents are collaborating on your request... Please wait."):
            try:
                # Initialize Agents and Tasks
                curr_agent, cod_agent, hw_agent = create_robotics_agents()
                tasks = create_robotics_tasks(curr_agent, cod_agent, hw_agent, age_group, user_query)

                # Create Crew
                crew = Crew(
                    agents=[curr_agent, cod_agent, hw_agent],
                    tasks=tasks,
                    process=Process.sequential,
                    verbose=True
                )

                # Kickoff Crew Execution
                result = crew.kickoff()

                st.success("🎉 Multi-Agent Analysis Complete!")
                st.markdown("### 📋 Expert Response & Output:")
                st.markdown(str(result))

            except Exception as e:
                st.error(f"An error occurred during execution: {e}")
