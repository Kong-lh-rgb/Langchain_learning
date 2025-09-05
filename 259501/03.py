from langchain_community.document_loaders import JSONLoader
import json
from pathlib import Path
from pprint import pprint


file_path='./example_data/facebook_chat.json'
data = json.loads(Path(file_path).read_text())
# 以一种美观、可读性强的方式来打印复杂的数据结构
pprint(data)