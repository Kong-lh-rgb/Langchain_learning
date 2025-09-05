#加载网页
#加载为字符串
from dotenv import load_dotenv
load_dotenv()
import asyncio
import bs4
from langchain_community.document_loaders import WebBaseLoader
page_url = "https://python.langchain.com/docs/how_to/chatbots_memory/"
loader = WebBaseLoader(
    web_path=[page_url],
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(class_="theme-doc-markdown markdown"),
    },
    bs_get_text_kwargs={"separator": " | ", "strip": True},
)
async def load_and_print_pages():
    docs = []
    async for doc in loader.alazy_load():
        docs.append(doc)
    assert len(docs) == 1
    doc = docs[0]
    print(f"{doc.metadata}\n")
    print(doc.page_content[:500])
if __name__ == "__main__":
    asyncio.run(load_and_print_pages())