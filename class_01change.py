import os
import asyncio
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tqdm.asyncio import tqdm
# 加载环境变量
load_dotenv()

# 初始化模型
llm = GoogleGenerativeAI(model="gemini-2.5-pro")

# 定义模板（注意修正方法名：from_messages 不是 from_message）
template = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的机器人，你的名字是{name}"),
    ("human", "{input}")
])

output_parser = StrOutputParser()
chain = template | llm | output_parser

# # 异步调用函数
# async def async_invoke():
#     # 异步批量处理输入（使用 abatch）
#     responses = await chain.abatch(
#         [
#             {"name": "Bob", "input": "你好吗"},
#             {"name": "Bob", "input": "你今天开心吗"}
#         ],
#         return_exceptions=True  # 可选：异常时返回错误而非中断
#     )
#     for resp in responses:
#         print(resp)


# 异步调用函数（使用 abatch_as_completed）
async def async_invoke():
    inputs = [
        {"name": "Bob", "input": "你好吗"},
        {"name": "Bob", "input": "你今天开心吗"},
        {"name": "Bob", "input": "讲个笑话"},
        {"name": "Bob", "input": "1+1等于几"}
    ]

    # 实时处理完成的任务（带进度条）
    async for idx, result in tqdm(
            chain.abatch_as_completed(inputs, return_exceptions=True),
            total=len(inputs),
            desc="处理进度"
    ):
        if isinstance(result, Exception):
            print(f"\n❌ 任务{idx + 1}失败: {type(result).__name__}: {result}")
        else:
            print(f"\n✅ 任务{idx + 1}完成:\n{result}")


# 运行异步主函数
if __name__ == "__main__":
    asyncio.run(async_invoke())