from dotenv import load_dotenv
import asyncio
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

file_path = (r"D:\pyproject\Langchain_learning\database\pumpkin_book.pdf")
# PyPDFLoader把pdf读取转化成结构化的document数据 不仅包括内容还包括文件路径，页码等
loader = PyPDFLoader(file_path)
# 定义一个异步函数来加载和处理页面
async def load_and_print_pages():
    pages = []
    # 在异步函数内部使用 async for
    async for page in loader.alazy_load():
        pages.append(page)
    # 打印第一页的元数据和内容
    if pages:
        print(f"{pages[1].metadata}\n")
        print(pages[1].page_content)
    vector_store = InMemoryVectorStore.from_documents(pages, GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"))
    docs = vector_store.similarity_search("What is LayoutParser?", k=2)
    for doc in docs:
        print(f"Page {doc.metadata['page']}: {doc.page_content[:300]}\n")
# 在主程序中运行异步函数
if __name__ == "__main__":
    asyncio.run(load_and_print_pages())