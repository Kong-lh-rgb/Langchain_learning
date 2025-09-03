from langchain_core.example_selectors.base import BaseExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# 我们的所有示例
examples = [
    {"input": 1, "output": "one"},
    {"input": 2, "output": "two"},
    {"input": 15, "output": "fifteen"},
    {"input": 20, "output": "twenty"},
]

# 我们的“策展人”类
class GreaterThanTenSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples

    def add_example(self, example):
        """Adds a new example to the list."""
        self.examples.append(example)

    def select_examples(self, input_variables):
        # 挑选出所有 input 大于 10 的例子
        filtered_examples = [example for example in self.examples if example["input"] > 10]
        return filtered_examples

# 创建一个我们的“策展人”实例
selector = GreaterThanTenSelector(examples)

# 定义一个例子的格式
example_prompt = PromptTemplate.from_template("Number: {input}\nWord: {output}")

# 告诉 FewShotPromptTemplate 使用我们的“策展人”
prompt = FewShotPromptTemplate(
    example_selector=selector,
    example_prompt=example_prompt,
    prefix="Translate the following numbers to English words:",
    suffix="Number: {input}\nWord:",
    input_variables=["input"],
)

# 打印最终生成的提示
print(prompt.format(input="3"))