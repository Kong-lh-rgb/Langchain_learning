import os
from os import system
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
load_dotenv()
from langchain_google_genai import GoogleGenerativeAI
from langchain_zhipuai import ZhipuAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm = GoogleGenerativeAI(model="gemini-2.5-pro")

#from_message精细控制对话流程和角色分工
template = ChatPromptTemplate.from_messages([
    ("system","你是一个有用的机器人，你的名字是{name}"),
    ("placeholder","{conversation}"),
    # 预设机器人先发送消息
    # SystemMessage(content = "hello"),
    ("human","hi你好吗"),
    ("ai","我感觉不错"),
    ("human","{input}")
])
#from_template一句话快速生成用户输入模板
# template = ChatPromptTemplate.from_template(
#     "你是一个助手，用户输入{input}"
# )


out = StrOutputParser()
chain = template | llm | out
res = chain.invoke(
    {
        #设置历史对话
        # "conversation": [
        #         ("human", "Hi!"),
        #         ("ai", "How can I assist you today?"),
        #         ("human", "Can you make me an ice cream sundae?"),
        #         ("ai", "No.")
        # ],
        "name":"Bob",
        "input":"你好吗",
    }
)
# prompt_value = template.invoke(
#     {
#         "name":"Bob",
#         "input":"你叫什么名字？"
#     }
# )
print(res)