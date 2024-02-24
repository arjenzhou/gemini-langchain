from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI 

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="给制作 {product} 的公司起一个名字",
)

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

res = chain.invoke("杯子")
for name in res.values():
    print(name)

# 杯子
# * 晶耀杯艺
# * 琉璃匠心
# * 彩釉风华
# * 恒彩琉璃
# * 杯之雅韵
# * 琉璃雅居
# * 缤纷杯艺
# * 华彩琉璃
# * 盛辉杯艺
# * 典雅杯艺