#多模态数据输入，还包括音频，文档暂不学习，先学图片输入类比即可
import os
import base64
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

# 加载环境变量
load_dotenv()
# 初始化大模型
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 将本地图片文件转换为 Base64 字符串
def get_base64_image_from_file(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# 图片的本地路径
image_path = "D:/pyproject/Langchain_learning/R-C.jpg"
base64_image_data = get_base64_image_from_file(image_path)

# 构建多模态消息列表
messages = [
    HumanMessage(
        content=[
            {"type": "text", "text": "Describe the weather in this image:"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image_data}"
                },
            },
        ]
    )
]

# 调用大模型
response = llm.invoke(messages)

# 打印响应内容（注意：使用 .content 属性）
print(response.content)