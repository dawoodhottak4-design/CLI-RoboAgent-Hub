from crewai import Task

def create_robotics_tasks(curriculum_agent, coding_agent, hardware_agent, age_group, user_query):
    
    # Task 1: Curriculum & Pedagogical Breakdown
    curriculum_task = Task(
        description=f"""Analyze the user's request: '{user_query}' for the age group: '{age_group}' keeping in mind the CLI Robotic School DHA Quetta syllabus framework.
        Provide a structured pedagogical approach, learning objectives, and core concepts to cover.""",
        expected_output="A detailed curriculum breakdown with clear learning objectives, milestones, and teaching methodologies tailored for the specified age group.",
        agent=curriculum_agent
    )

    # Task 2: Code or Technical Explanation
    coding_task = Task(
        description=f"""Based on the age group '{age_group}' and query '{user_query}', provide the relevant technical content. 
        If it's for younger ages (6-10), explain block coding logic. If it's for older groups (11-16), provide clean, commented Python/C++ code snippets or AI/Machine Learning workflow steps.""",
        expected_output="Step-by-step coding instructions, logic explanations, or production-ready code snippets with comments.",
        agent=coding_agent
    )

    # Task 3: Hardware, Mechanics & Project Guidance
    hardware_task = Task(
        description=f"""Provide practical guidance on hardware components, sensors (touch, tilt, ultrasonic), mechanical structures (gears, levers), 
        or project implementation tips related to '{user_query}' for age group '{age_group}'.""",
        expected_output="Practical hardware integration tips, troubleshooting steps, and project development guidelines.",
        agent=hardware_agent
    )

    return [curriculum_task, coding_task, hardware_task]
