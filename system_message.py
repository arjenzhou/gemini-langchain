from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
m = model.invoke(
    [
        SystemMessage(content="回答是或者不是"),
        HumanMessage(content="苹果是水果吗？"),
    ]
)
print(m.content)

# 是