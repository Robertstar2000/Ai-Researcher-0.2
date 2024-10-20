
##AI Science Researcher
An AI-powered application that generates comprehensive research papers based on user-provided topics.

#Features

Outline Generation: Creates a detailed outline using recursive refinement.
Content Generation: Generates content for each section with iterative improvements.
Document Processing: Formats the document, processes figures and tables, and manages references.
User Interface: Streamlit-based UI with progress tracking and interactive elements.
Download Options: Provides the final document in MS Word format for download.
Setup Instructions

#Explanation:

The above code provides a modular approach to generating a research paper using AI agents in Python, suitable for a beginner programmer. Each module has been designed with extensive comments to explain the purpose and logic of the functions and classes within:

	•	settings.py: Handles configuration, including setting up API keys and endpoints, and provides a function to make API calls to the AI inference engine.
	•	agents.py: Defines the base Agent class and specialized agents (ResearcherAgent, WriterAgent, CriticAgent) that interact with the AI model to perform research, writing, and critiquing tasks.
	•	style.py: Contains functions that return style prompts based on the document type and visual generation requirements.
	•	outline.py: Uses the agents to generate and refine an outline for the research paper, iteratively improving the section titles and descriptions.
	•	content.py: Expands the outline into detailed content by iteratively refining each section’s content with the help of the agents. It also updates a progress bar to track the process.
	•	visual.py: Generates visuals for the document using descriptions from the content. It creates images using the Pillow library and saves them for inclusion in the document.
	•	assem.py: Assembles the content, visuals, and references into a cohesive Word document, handling the insertion of images and formatting.
	•	main.py: Sets up the Streamlit UI, collects user input, orchestrates the workflow by calling functions from other modules, displays progress, and provides the final document for download.

Note: The AI API calls are simulated with placeholder responses since actual API keys and endpoints are not provided. In a real implementation, you would need to replace these placeholders with actual API calls to the Groq or SambaNova services, including proper error handling and response parsing.

Usage:

	1.	Install the required libraries:
pip install streamlit pillow python-docx
sreamlit run main.py
