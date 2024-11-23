from crew import Crew, Process
from agents1 import News_Researcher, News_Writer
from tasks1 import Researcher_Task, Writer_Task

crew = Crew(
    agents = [News_Researcher, News_Writer],
    tasks = [Researcher_Task, Writer_Task],
    process = Process.sequential
)

result = crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)