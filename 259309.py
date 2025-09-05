from dotenv import load_dotenv
load_dotenv()
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field, model_validator

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature = "0.0")
class Joke(BaseModel):
    # BaseModel是Pydantic库的核心基类。继承它之后，类就具备了强大的数据验证、解析、序列化和文档生成能力。
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")
    # = Field(...) 是 Pydantic 的一个函数，用于提供额外的元数据。在这里，它为 setup 字段添加了一个描述信息。
    @model_validator(mode="before")
    # 这是一个Pydantic装饰器，用于定义一个模型级别的验证器。
    # model_validator允许你在验证整个模型时执行自定义逻辑。
    # mode = "before"表示这个验证器将在字段的类型检查之前运行。这意味着它接收的是原始的输入数据（通常是一个字典），而不是已经转换好的字段值。
    @classmethod
    # 这是一个Python内置的装饰器，表明question_ends_with_question_mark是一个类方法
    def question_ends_with_question_mark(cls, values: dict) -> dict:#cls指的是Joke类本身
        setup = values.get("setup")
        if setup and setup[-1] != "?":
            raise ValueError("Badly formed question!")
        return values


parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


chain = prompt | model | parser
output = chain.invoke({"query": "Tell me a joke."})
list(output)
