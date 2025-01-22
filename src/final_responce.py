from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from CONFIG.config import ConfigData

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.retrive_decomp_query_data import pipline_run

def answer_query_gpt(uquery, einput, veinput, voinput):  
    llm_openai = ChatOpenAI(openai_api_key=ConfigData.OPEN_AI_KEY, model='gpt-4-0125-preview', temperature=0)  
    prompt_template_for_creating_query_2 = """
        You are a helpful analytical assistant with expertise in data interpretation and insights generation. You excel at:

            1. Deep analysis of complex data formats including JSON, text, and email
            2. Converting raw data into meaningful business insights and patterns
            3. Providing clear, conversational explanations that connect data points to practical implications
            4. Contextualizing findings by considering industry trends and business impact
            5. Generating both high-level summaries and detailed breakdowns based on user needs

        When analyzing data, you:
            - First examine the data structure and quality
            - Identify key patterns, trends, and anomalies
            - Draw meaningful conclusions that answer the user's specific questions
            - Provide supporting evidence for your insights
            - Suggest potential actions or recommendations based on the findings
            - Use clear language to explain technical concepts
            - Proactively highlight important findings that may not be directly asked but are relevant

        you use following data to answer user query. :

        Query : {user_query} 
        
        Data : 
            Email Data : {input_email}
            
            Vessle JSON Data : {input_vessel}
            
            Voyage JSON Data : {input_voyage}
        
        Note : 
            - Provide answer which will give more clearty from given data. 
            - Provide answer in paragraph explaning things in details.
            - Strictly do NOT generate any informetion by your self, which is not given in provided data .
            - Do not explain your answer or flow to find answer, just provide hummanly answer.
            - Do not provide code as answer
            - If any of the data shows none then ignore that and focus on data you have.
        """
        
    query_creation_prompt_2 = PromptTemplate(
        template=prompt_template_for_creating_query_2,
        input_variables=["user_query", "input_email", "input_vessel", "input_voyage"],
    )
    llmchain_2 = LLMChain(llm=llm_openai, prompt=query_creation_prompt_2, verbose=True)

    response = llmchain_2.invoke({
        "user_query": uquery,
        "input_email": einput, 
        "input_vessel": veinput, 
        "input_voyage": voinput
    })

    return response

def main(uquery):
    decomp_querys_dict = pipline_run(uquery)
    einput = None
    veinput = None
    voinput = None
    for ty in decomp_querys_dict.keys():
        if ty == "email":
            einput = decomp_querys_dict["email"]
        elif ty == "vessel":
            veinput = decomp_querys_dict["vessel"]
        elif ty == "voyage":
            voinput = decomp_querys_dict["voyage"]

    out_responce = answer_query_gpt(uquery, einput, veinput, voinput)

    return out_responce

