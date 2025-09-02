import os
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# chunks = []
# for chunk in llm.stream("天空什么颜色"):
#     chunks.append(chunk)
#     print(chunk.content, end="|", flush=True)

# 必须在异步函数中使用 await
async def main():
    print("正在获取模型响应...")
    # await llm.astream() 是非阻塞的，可以边等待边做其他事
    async for chunk in llm.astream("天空什么颜色"):
        print(chunk.content, end="", flush=True)
    print("\n响应获取完毕。")
# 运行异步主函数
if __name__ == "__main__":
    asyncio.run(main())