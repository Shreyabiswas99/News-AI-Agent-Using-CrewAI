from crewai import Agent
from tools1 import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

LLM = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    verbose = True,
    temperature = 0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

News_Researcher = Agent(
    role = 'Research news and information',
    goal = 'Uncover ground breaking technologies on {topic}',
    verbose = True,
    memory = True,
    backstory = ("Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools = [tool],
    llm = LLM,
    allow_delegation = True
)

News_Writer = Agent(
    role = 'Write news based on the research',
    goal = 'Narrate compelling technical stories on the {topic} based on the research',
    verbose = True,
    memory = True,
    backstory = ("With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    ),
    tools = [tool],
    llm = LLM,
    allow_delegation = False
)

