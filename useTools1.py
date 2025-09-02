import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from dotenv import load_dotenv
load_dotenv()
from langchain_core.tools import tool
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# @tool
# def add(a:int,b:int) ->int:
#     """求a与b的和"""
#     return a+b
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash").bind_tools([add])
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你是一个善于使用工具的助手，请简洁地回答问题。"),
#     ("human", "{input}"),
#     ("placeholder", "{agent_scratchpad}"),
# ])
#
# # 2. 创建代理。
# # create_tool_calling_agent 会将模型、工具和提示词组合起来，
# # 形成一个能够“思考”并调用工具的代理。
# agent = create_tool_calling_agent(llm, [add], prompt)
#
# # 3. 创建代理执行器。
# # AgentExecutor 负责驱动整个流程：接收用户输入、运行代理、
# # 执行工具、将结果返回给代理，直到得到最终答案。
# # verbose=True 会打印出整个思考和执行过程，便于调试。
# agent_executor = AgentExecutor(agent=agent, tools=[add], verbose=True)
# # 调用代理执行器，它会处理所有工具调用和最终答案的生成。
# result = agent_executor.invoke({"input": "3加5等于多少"})
#
# # 打印最终答案
# print("---")
# print("最终答案:")
# print(result["output"])



@tool
def add(a:int,b:int) ->int:
    """求两个数的和"""
    return a+b

@tool
def multiply(a:int,b:int) ->int:
    """两个数的乘法"""
    return a*b

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Use the provided tools to answer questions."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

tools = [add, multiply]
agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({"input":"4乘4等于多少"})
print(result["output"])