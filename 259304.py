from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",temperature = 0.0)
from langchain_core.output_parsers import StrOutputParser
out = StrOutputParser()
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PipelinePromptTemplate, PromptTemplate
# prompt = (
#     PromptTemplate.from_template("讲一个关于{topic}的笑话")
#     +" make it funny"
#     +" in {language}"
# )
# chain = prompt | llm | out
# # prompt1 = prompt.format(topic = "动物", language = "spanish")
# res = chain.invoke({"topic":"动物","language":"ch"})
#
# print(res)
# prompt = SystemMessage(content = "你是一个助手")
# new_prompt = (
#     prompt + HumanMessage(content="hi") + AIMessage(content="我是一个助手") + "{input}"
# )
# chain = new_prompt | llm | out
# res = chain.invoke({"input":"你是谁"})
# print(res)

