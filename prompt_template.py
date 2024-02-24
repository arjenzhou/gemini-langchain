from langchain.prompts import PromptTemplate
 
prompt = PromptTemplate(
    input_variables=["product"],
    template="给制作 {product} 的公司起一个名字",
)

print(prompt.format(product="杯子"))