from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
for chunk in llm.stream("写一段关于 Gemini 的小诗"):
    print(chunk.content)
    print("---")
# Note that each chunk may contain more than one "token"

# 双子座，你是风中的精灵，
# 轻盈而飘逸，

# ---
# 你像一朵云彩，
# 在广阔的天空中自由地翱翔。

# 你充满好奇心，
# 对一切都感兴趣，
# 你总是
# ---
# 第一个尝试新事物的人，
# 你总是第一个发现新奇之处的人。

# 你是一个很好的倾听者，
# 你愿意听别人倾诉，
# 你总是能给别人提供帮助，
# 你总是能给别人带来快乐。

# 你是一个很好的朋友，
# 你总是忠诚可靠，

# ---
# 你总是能在别人需要的时候伸出援手，
# 你总是能在别人伤心的时候安慰他们。

# 双子座，你是最迷人的星座，
# 你总是能吸引别人的目光，
# 你总是能让人们对你着迷，
# 你总是能让人们对你念念不忘。
# ---