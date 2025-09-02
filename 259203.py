from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, filter_messages
from langchain_core.runnables import RunnableLambda

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    SystemMessage("you are a good assistant", id="1"),
    HumanMessage("example input", id="2", name="example_user"),
    AIMessage("example output", id="3", name="example_assistant"),
    HumanMessage("real input", id="4", name="bob"),
    AIMessage("real output", id="5", name="alice"),
]

# 错误用法：将列表赋值给变量
# filter = filter_messages(messages,include_types = "human")

# 正确用法：将函数本身作为Runnable来使用
# 1. 直接使用函数作为链的一部分（LangChain 内部会处理）
chain = RunnableLambda(lambda x: filter_messages(x, include_types="human")) | llm

# 2. 或者，如果你需要链来处理整个列表，可以这样调用
# 在这种情况下，invoke的输入就是messages
res = chain.invoke(messages)
print(res.content)