from dotenv import load_dotenv
from langchain.tools import tool , Tool
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain_ollama import ChatOllama
from typing import Union , List


load_dotenv()

@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with {text =}")
    text = text.strip("'\n").strip(
        '"'
    ) #stripping away non alphabetic characters just in case
    return len(text)


def find_tool_by_name(tools: List[Tool] , tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f'Tool with name {tool_name} not found!')

if __name__ == "__main__":
    print("Hello Reac Langchain")
    tools = [get_text_length]

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:
    """

    promt = PromptTemplate.from_template(template=template).partial(
        tools = render_text_description(tools),
        tool_names = ', '.join([t.name for t in tools])
    )

    llm = ChatOllama(model="llama3" , temperature=0, stop = ["\nObservation","Observation"])