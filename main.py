from dotenv import load_dotenv
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool
from langchain.agents import AgentType,create_csv_agent

load_dotenv()

def main():
    print("Start...")
    python_agent_executor=create_python_agent(
        llm=ChatOpenAI(temperature=0, model='gpt-3.5-turbo'),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # python_agent_executor.run(""" Install the qrcode package first. Then,
    # Generate and save in the Current Working Directory 15 QR Codes that poiint to www.udemy.com/course/langchain """)


    csv_agent=create_csv_agent(
        llm=ChatOpenAI(temperature=0, model='gpt-3.5-turbo'),
        path="episode_info.csv",
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )

    csv_agent.run("How many columns are there in the file episode_info.csv")

if __name__=="__main__":

    main()
