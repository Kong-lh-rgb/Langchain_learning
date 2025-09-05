from langchain_community.document_loaders import UnstructuredURLLoader
import asyncio
page_url = "https://python.langchain.com/docs/how_to/chatbots_memory/"
loader = UnstructuredURLLoader(urls=[page_url])

docs = []
async def load():
    async for doc in loader.alazy_load():
        docs.append(doc)
    for doc in docs[:5]:
        print(doc.page_content)
if __name__ == "__main__":
    asyncio.run(load())