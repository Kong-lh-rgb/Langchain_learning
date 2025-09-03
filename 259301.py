from dotenv import load_dotenv
load_dotenv()
#嵌入的使用
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = InMemoryVectorStore(embedding=embedding)

document_1 = Document(
    page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
)
document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
)
documents = [document_1, document_2]
vectorstore.add_documents(documents = documents,ids = ["ds1","ds2"])
# vectorstore.delete(ids = "id1")删除文档
# 相似性搜索
# query = "myquery"
# docs = vectorstore.similarity_search(query)
query = "what did you eat at morning"
results = vectorstore.similarity_search(query = query,k = 1)
print("查询结果:")
for doc in results:
    print(f"匹配到的文档内容: {doc.page_content}")
    print(f"元数据: {doc.metadata}")
    print("-" * 20)