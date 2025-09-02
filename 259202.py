#修剪消息避免超过模型上下文输入限制
from dotenv import load_dotenv
load_dotenv()
import os
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
    trim_messages,
)
from langchain_core.messages.utils import count_tokens_approximately
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    SystemMessage("你是一个机器人"),
    HumanMessage("您好"),
    AIMessage(
        '您好'
    ),
    HumanMessage("你在干嘛"),
    AIMessage(
        "为您服务"
    ),
    HumanMessage("你会做什么"),
]

#注意：systemmessage不算在限制的令牌里面，修剪过程从后往前修剪，最重要加上system返回给大模型，元数据不算做token
# res = trim_messages(
#     messages,
#     strategy="last",
#     token_counter=count_tokens_approximately,
#     max_tokens=14,
#     start_on="human",
#     end_on=("human", "tool"),
#     include_system=True,
#     allow_partial=False,
# )

res = trim_messages(
    messages,
    strategy="last",
    token_counter=len,
    max_tokens=5,
    start_on="human",
    end_on=("human", "tool"),
    include_system=True,
)
print(res)
