# Building News AI agent using CrewAI and Google Gemini Pro LLM models
* Inside this project, I have built an AI agent which will automatically write a blog on topic we give. The data it will collect from the opensource google gemini pro model and serper api
* We need 2 agents, one for researching the topic and report to the writer and one writer agent who will basically write those blogs. Similarly we need 2 tasks for those two agents.

## Setup
* If using VSCode make sure to setup the environment for our model, we can do that by running this command on the terminal : create -p venv python=3.9 -y
* Activate it by using conda activate venv
* Make sure you have latest version of python and VSCode setup
* Lastly install all the required libraries by running pip install -r requirements.txt
  
## Running 
* Run the LLM model by running the crew file using the command : python crew1.py
