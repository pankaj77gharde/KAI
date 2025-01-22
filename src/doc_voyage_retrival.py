from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import json, re, pymongo
from CONFIG.config import ConfigData

def voyage_get_query(user_question):
    llm_openai = ChatOpenAI(openai_api_key=ConfigData.OPEN_AI_KEY, model='gpt-3.5-turbo-0125')#, temperature=0) # gpt-4o-2024-05-13   gpt-3.5-turbo-0125
    # llm_openai = ChatOpenAI(openai_api_key=ConfigData.OPEN_AI_KEY, model='gpt-4-0125-preview')
    table_schema = ConfigData.TABLE_SCHEMA_VOYAGE
    schema_description = ConfigData.SCHEMA_DESCRIPTION_VOYAGE
    json_ex_1 = ConfigData.FEW_SHOT_EXAMPLE_1_VOYAGE
    json_ex_string = json.dumps(json_ex_1)
    prompt_template_for_creating_query = """
                You are an expert MongoDB query architect specializing in generating JSON-compatible aggregation pipelines.

                Table Schema: """ + table_schema + """ 
                Schema Description: """ + schema_description + """

                QUERY REQUIREMENTS:
                1. Generate a MongoDB aggregation pipeline as a JSON array
                2. Use proper MongoDB operators ($match, $group, $lookup etc.)
                3. In case of date calcultion do it by yourself in backend and only provide values in query
                4. All property names and string values MUST use double quotes
                5. No trailing commas
                6. Numbers should be unquoted
                7. Boolean values must be lowercase (true/false)
                8. Do not use ISODate or commands like that 

                Example Format:
                Input: Get each route of Stena Performance and respective costing
                Output: {json_ex_string_1}

                RESPONSE FORMAT:
                - Output MUST be a valid JSON array of pipeline stages
                - Pipeline must be an array of aggregation stages to run query
                - Each stage must be a properly formatted JSON object
                - No explanations or comments, just the query array

                Input Query: {user_question}
                """
    # Note : Please provide source file name from source_file when getting data from database.   
    query_creation_prompt = PromptTemplate(
        template=prompt_template_for_creating_query,
        input_variables=["user_question", "json_ex_string_1"],
    )
    llmchain = LLMChain(llm=llm_openai, prompt=query_creation_prompt, verbose=True)


    response = llmchain.invoke({
        "user_question": user_question,
        "json_ex_string_1": json_ex_string
    })

    response_text = response['text'].replace("Output: ", "")
    pattern = r'db\.collectionName\.aggregate\(\s*\['

    output_string = re.sub(pattern, '', response_text)

    return json.loads(output_string)

def vog_get_final_out(question):
    client = pymongo.MongoClient(ConfigData.MONGO_DB_URI)
    db = client[ConfigData.DB_NAME]
    collection_name = db[ConfigData.COLLECTION_NAME_VOYAGE]
    query_1 = voyage_get_query(user_question=question)
    pipeline = query_1
    result = collection_name.aggregate(pipeline)
    final_out = []
    for doc in result:
        final_out.append(doc)
    return final_out