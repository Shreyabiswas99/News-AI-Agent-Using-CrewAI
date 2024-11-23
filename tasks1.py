from crewai import Task
from tools1 import tool
from agents1 import News_Researcher, News_Writer

Researcher_Task = Task(
    description = ("Identify the next big trend in {topic}."
                   "Focus on identifying pros and cons and the overall narrative."
                   "Your final report should clearly articulate the key points,"
                   "its market opportunities, and potential risks."),
    expected_output = 'A detailed and comprehensive 3 paragraphs report on {topic}',
    tools = [tool],
    agent = News_Researcher
)

Writer_Task = Task(
    description = ("Compose an insightful article on {topic}."
                   "Focus on the latest trends and how it's impacting the industry."
                   "This article should be easy to understand, engaging, and positive."),
    expected_output = 'A 4 paragraph article on {topic} formatted as markdown.',
    tools = [tool],
    agent = News_Writer,
    async_execution = False,
    output_file = 'new-report.md'
)