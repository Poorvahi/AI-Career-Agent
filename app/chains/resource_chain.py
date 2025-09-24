from langchain_core.prompts import ChatPromptTemplate
from app.utils.llm_config import get_openai_llm
llm = get_openai_llm()
prompt = ChatPromptTemplate.from_template(
   """For the following careers:
   {careers}
   Suggest one free learning platform or online course per career.
   Format: Career- Platforms: Course Title - URL Be concise and helpful.
   """
)

def get_resource_chain():
    return prompt |llm