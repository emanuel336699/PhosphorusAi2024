'''
Main file for the Phosphorus agent system.
'''
import os

# Set environment variable
os.environ["SERPER_API_KEY"] = "ee473426ab93827f3e862103f6a61dc1b5e4866f"

# Your remaining code goes here

from crewai import Agent,Workflow
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama
ollama_llm = Ollama(model="openhermes")
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
def create_agent(agent_name, agent_role):
    '''
    Function to create a new agent with the given name and role.
    '''
    agent = Agent(agent_name)
    agent.set_role(agent_role)
    return agent
def assign_task(agent, task):
    '''
    Function to assign a task to an agent.
    '''
    agent.assign_task(task)
def main():
    '''
    Main function to run the Phosphorus agent system.
    '''
    # Create a workflow
    workflow = Workflow()
    create_agent()
    # Create agents
    agent1 = create_agent("Agent1", "Coding")
    llm=ollama_llm
    verbose=True,
    allow_delegation=False
    search_tool = DuckDuckGoSearchRun
    agent2 = create_agent("Agent2", "Running Code and Debugging")
    llm=ollama_llm
    verbose=True,
    search_tool = DuckDuckGoSearchRun,
    allow_delegation=False
    # Assign tasks to agents
    assign_task(agent1, "Code the interface for the Phosphorus App")
    assign_task(agent2, "Assist Agent 1 in Coding but especially Running And Debbuging, reflecting on all issues you stumble upon togheder")
    # Add agents to the workflow
    workflow.add_agent(agent1)
    workflow.add_agent(agent2)
    # Run the workflow
    workflow.run()