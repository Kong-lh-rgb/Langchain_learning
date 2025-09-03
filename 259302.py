from dotenv import load_dotenv
load_dotenv()
import os
from langchain.chains.constitutional_ai.prompts import examples
from sympy.physics.units import temperature
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",temperature = 0.0)
examples = [
    {"input":"7 ❀ 3","output":"21"},
    {"input":"2 ❀ 3","output":"6"}
]
example_prompt = ChatPromptTemplate.from_messages([
    ("human","{input}"),
    ("ai","{output}")
])
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
final_prompt = ChatPromptTemplate.from_messages(
    [
        few_shot_prompt,
        ("human", "{input}"),
    ]
)
chain = final_prompt | llm
res = chain.invoke({"input":"什么是7 ❀ 9"})
print(res.content)