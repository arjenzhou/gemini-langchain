import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key\n")
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("写一段关于 Gemini 的诗")
print(result.content)

# 在广阔的宇宙里，一颗闪耀的宝石，
# Gemini，双生星座，讲述着古老的故事。
# 两个兄弟，一个温柔，一个坚强，
# 他们的命运交织在一起，永不分离。

# 卡斯托尔，驯马师，驰骋疆场，
# 波吕多克斯，拳击手，勇猛无畏。
# 他们一起冒险，经历磨难，
# 友谊和兄弟情谊永不改变。

# 当卡斯托尔倒下，波吕多克斯悲痛万分，
# 他恳求宙斯让他与兄弟同生共死。
# 宙斯被他的忠诚打动，将他们升上天空，
# 化作双子星座，永远在一起。

# 如今，当我们仰望星空，
# 总能看到Gemini闪耀着光芒。
# 它提醒我们兄弟情谊的力量，
# 以及即使面对死亡，爱也能永存。