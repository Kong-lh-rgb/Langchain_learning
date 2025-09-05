from langchain_community.document_loaders import JSONLoader
import json
import os

# 1. 模拟一个JSON文件
json_data = [
  {
    "id": 101,
    "user_id": "user_A",
    "timestamp": "2023-10-26T10:00:00Z",
    "message": "大模型在处理非结构化数据方面非常强大。",
    "platform": "Twitter"
  },
  {
    "id": 102,
    "user_id": "user_B",
    "timestamp": "2023-10-26T10:05:00Z",
    "message": "LangChain 简化了LLM应用的开发流程。",
    "platform": "Forum"
  }
]

with open("temp_data.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

# 2. 定义一个函数，用于从原始JSON对象中提取元数据
def metadata_extractor(record: dict, metadata: dict) -> dict:
    metadata['record_id'] = record.get('id')
    metadata['source_user'] = record.get('user_id')
    metadata['timestamp'] = record.get('timestamp')
    return metadata

# 3. 初始化 JSONLoader
loader = JSONLoader(
    file_path="temp_data.json",
    # ⚠️ 关键修改：将 jq_schema 改为 "." 或 ".[]"
    # 这将返回一个包含所有字典的列表
    jq_schema=".[]",
    content_key="message",
    metadata_func=metadata_extractor,
    text_content=True
)

# 4. 加载文档
docs = loader.load()

# 5. 查看结果
for doc in docs:
    print("-" * 50)
    print(f"核心内容: {doc.page_content}")
    print(f"元数据: {doc.metadata}")

# 清理临时文件
os.remove("temp_data.json")