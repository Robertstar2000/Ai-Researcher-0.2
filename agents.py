
# agents.py

# This module defines agent classes for research, writing, and critiquing.

from settings import groq_api_call

class Agent:
    """
    Base class for all agents.

    Attributes:
        role (str): The role of the agent.
        goal (str): The goal or objective of the agent.
        tools (list): Tools available to the agent (e.g., APIs, databases).
    """
    def __init__(self, role, goal, tools=None):
        """
        Initializes the Agent with a role, goal, and optional tools.

        Args:
            role (str): The role of the agent.
            goal (str): The goal of the agent.
            tools (list, optional): A list of tools available to the agent.
        """
        self.role = role
        self.goal = goal
        self.tools = tools if tools else []

class ResearcherAgent(Agent):
    """
    Agent responsible for conducting research.

    Methods:
        research(subject): Performs research on the given subject.
    """
    def __init__(self, role='Researcher', goal='Conduct research', tools=None):
        """
        Initializes the ResearcherAgent with default role and goal.

        Args:
            role (str, optional): The role of the agent. Defaults to 'Researcher'.
            goal (str, optional): The goal of the agent. Defaults to 'Conduct research'.
            tools (list, optional): Tools available to the agent.
        """
        super().__init__(role, goal, tools)

    def research(self, subject):
        """
        Generates research content based on the subject.

        Args:
            subject (str): The subject to research.

        Returns:
            str: Research findings.
        """
        # Construct the prompt for the AI model.
        prompt = f"As a {self.role}, your goal is to {self.goal}.\nPlease conduct research on the following subject:\n\n{subject}\n\nProvide detailed findings."

        # Call the AI API to get the response.
        response = self._generate_response(prompt)
        return response

    def _generate_response(self, prompt):
        """
        Makes an API call to the AI service and returns the response.

        Args:
            prompt (str): The prompt to send to the AI model.

        Returns:
            str: The AI-generated response.
        """
        response = groq_api_call(prompt)
        return response

class WriterAgent(Agent):
    """
    Agent responsible for writing content.

    Methods:
        write(prompt): Creates content based on the provided prompt.
    """
    def __init__(self, role='Writer', goal='Write content', tools=None):
        """
        Initializes the WriterAgent with default role and goal.

        Args:
            role (str, optional): The role of the agent. Defaults to 'Writer'.
            goal (str, optional): The goal of the agent. Defaults to 'Write content'.
            tools (list, optional): Tools available to the agent.
        """
        super().__init__(role, goal, tools)

    def write(self, prompt):
        """
        Creates content based on the provided prompt.

        Args:
            prompt (str): The prompt containing instructions and information.

        Returns:
            str: Written content.
        """
        # Call the AI API to generate content.
        response = groq_api_call(prompt)
        return response

class CriticAgent(Agent):
    """
    Agent responsible for critiquing content.

    Methods:
        critique(content): Reviews and critiques the given content.
    """
    def __init__(self, role='Critic', goal='Critique content', tools=None):
        """
        Initializes the CriticAgent with default role and goal.

        Args:
            role (str, optional): The role of the agent. Defaults to 'Critic'.
            goal (str, optional): The goal of the agent. Defaults to 'Critique content'.
            tools (list, optional): Tools available to the agent.
        """
        super().__init__(role, goal, tools)

    def critique(self, content):
        """
        Provides critique and suggestions for improvement on the content.

        Args:
            content (str): The content to critique.

        Returns:
            str: Critique and suggestions.
        """
        prompt = f"As a {self.role}, your goal is to {self.goal}.\nPlease critique the following content and suggest improvements:\n\n{content}\n\nProvide constructive feedback."
        response = groq_api_call(prompt)
        return response