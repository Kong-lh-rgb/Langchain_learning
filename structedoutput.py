#使用结构化输出（这个太繁琐）
import getpass
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
llm = GoogleGenerativeAI(model="gemini-2.5-pro")
from typing import Optional
from pydantic import BaseModel,Field

class Joke(BaseModel):
    start:str = Field(description="讲个笑话")
    end:str = Field(description="笑话的最后一段")
    rating: Optional[int] = Field(
        default=None, description="笑话有多好笑, from 1 to 10"
    )

parser = PydanticOutputParser(pydantic_object=Joke)


prompt = ChatPromptTemplate.from_template(
    """请讲一个关于{topic}的笑话，按以下格式输出：
{format_instructions}"""
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser

result = chain.invoke({"topic":"狗"})
print(result)

#定义结构化输出语句
