from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
prompt = ChatPromptTemplate.from_template("讲个关于 {animal} 的笑话")
chain = prompt | llm | StrOutputParser()

# 使用 stream() 方法，逐块打印输出
for chunk in chain.stream({"animal": "猫"}):
    time.sleep(2)
    print(chunk, end="", flush=True)