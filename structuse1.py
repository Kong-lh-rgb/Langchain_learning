#正确的结构化输出
import getpass
import os
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
# 加载环境变量
load_dotenv()
# 初始化模型
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
# Pydantic
class Joke(BaseModel):
    """Joke to tell user."""
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )

structured_llm = llm.with_structured_output(Joke)
structured_llm.invoke("Tell me a joke about cats")