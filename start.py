from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9)
text = "给制作杯子的公司起一个名字"
res = llm.invoke(text)
print(res.content)

# 1. 瓷雅陶杯
# 2. 品茗雅杯
# 3. 水晶琉璃阁
# 4. 陶韵杯艺
# 5. 琉璃雅艺
# 6. 瓯茗雅杯
# 7. 天沐杯艺
# 8. 御瓷雅韵
# 9. 匠心陶坊
# 10. 精艺杯器