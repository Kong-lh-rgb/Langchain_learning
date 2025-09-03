from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
# 这个模型会将 examples 中的每个示例的 input（或整个示例）编码成高维向量。
    GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
# 所有 examples 的嵌入会被存入 Chroma，并建立索引以便快速检索。后续对比调用chroma的检索接口
    Chroma,
    k=1,
)
similar_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input",
    suffix="input: {adjective}\nOutput:",
    input_variables=["adjective"],
)
similar_prompt.example_selector.add_example(
    {"input": "enthusiastic", "output": "apathetic"}
)
print(similar_prompt.format(adjective="passionate"))