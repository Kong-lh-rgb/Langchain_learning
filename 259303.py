from langchain_core.prompts import PromptTemplate
from datetime import datetime
# prompt = PromptTemplate.from_template("{foo}{bar}")
# partial_prompt = prompt.partial(foo="foo")
# print(partial_prompt.format(bar="baz"))

# 简洁的用法
# prompt = PromptTemplate(
#     template="{foo}{bar}",
#     input_variables=["bar"],
#     partial_variables={"foo": "foo"}
# )
# print(prompt.format(bar="baz"))

# 函数
def get_time():
    time = datetime.now()
    return time.strftime("%Y-%m-%d %H:%M:%S")

prompt = PromptTemplate(
    template="现在是{time}，讲一个{abject}的笑话",
    input_variables=["abject"],
    partial_variables = {"time":get_time()}
)
print(prompt.format(abject = "funny"))