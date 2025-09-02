from dotenv import load_dotenv
load_dotenv()
import os
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

#内存缓存
from langchain_core.caches import InMemoryCache
# set_llm_cache(InMemoryCache())
# start_time = time.time()
# res = llm.invoke("讲个笑话")
# end_time = time.time()
# print(res)
# print({end_time - start_time})
# #第二次输入同样地内容会直接使用第一次生成的结果，反应速度很快
# start_time = time.time()
# res = llm.invoke("讲个笑话")
# end_time = time.time()
# print(res)
# print({end_time - start_time})

# 使用SQLiteCache
set_llm_cache(SQLiteCache(database_path=".langchain.db") )
start_time = time.time()
res = llm.invoke("Tell me a joke")
print(res)
end_time = time.time()
print({end_time - start_time})
#打印元数据
print(res.response_metadata)

start_time = time.time()
print(llm.invoke("Tell me a joke"))
end_time = time.time()
print({end_time - start_time})