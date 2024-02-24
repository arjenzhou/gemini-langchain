import requests
from IPython.display import Image

image_url = "https://picsum.photos/seed/picsum/300/300"
content = requests.get(image_url).content
Image(content)

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
# example
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "这张图片是什么？",
        },  # You can optionally provide text parts
        {"type": "image_url", "image_url": image_url},
    ]
)
res = llm.invoke([message])
print(res.content)

#  这是马特洪峰的日落景色，马特洪峰是阿尔卑斯山脉的一座山峰，也是瑞士的标志性山峰之一。