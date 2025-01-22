from langchain.llms import OpenAI 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import List
import os
from CONFIG.config import ConfigData

def decomposeme(query):
    # llm = OpenAI(temperature=0, openai_api_key=ConfigData.OPEN_AI_KEY)
    llm = ChatOpenAI(openai_api_key=ConfigData.OPEN_AI_KEY, model='gpt-4-0125-preview', temperature=0)

    decomposition_examples = """
    Example Decompositions with Confidence Scores:
    1. Query: "What vessels were mentioned in emails about delayed voyages?"
       {
           "email": {
               "query": "Retrieve all emails containing discussions about delayed voyages, extract vessel names and delay details",
               "confidence": 0.9,
               "reasoning": "Emails are primary source for communications about delays"
           },
           "vessel": {
               "query": "List all vessels that have recorded delays in their schedules",
               "confidence": 0.7,
               "reasoning": "Vessel database contains delay records but may not have all communication details"
           },
           "voyage": {
               "query": "Retrieve all voyage records with delay notifications",
               "confidence": 0.8,
               "reasoning": "Voyage records directly track delays but may miss informal communications"
           }
       }

    2. Query: "List all bulk carriers that departed from Singapore last week"
       {
           "vessel": {
               "query": "Find all vessels of type 'bulk carrier'",
               "confidence": 0.95,
               "reasoning": "Vessel database definitively contains vessel types"
           },
           "voyage": {
               "query": "Get all vessel departures from Singapore in the last week",
               "confidence": 0.9,
               "reasoning": "Voyage records directly track port departures"
           }
       }
    """

    decompose_template = """
        You are an expert at analyzing queries and determining which data sources could provide the answer.

        Available Data Sources:
        1. Email Data: {email_example}
           Contains: Email communications with subject, body, sender, recipient, date
        
        2. Vessel Details: {vessel_example}
           Contains: Static vessel information like name, IMO number, vessel type
        
        3. Voyage Range: {voyage_example}
           Contains: Journey details, ports, dates, schedules

        {decomposition_examples}

        Query to Analyze: {input_query}

        Task:
        1. First, identify ALL data sources that could answer this query:
           - Which data sources contain the information needed?
           - Could the answer be found in multiple data sources?
           
        2. Response Format Rules:
           a) If query can be answered from only ONE data source:
              Return dictionary with source key containing query object and confidence score
              Example: {{
                  "email": {{
                      "query": "original query here",
                      "confidence": 0.9,
                      "reasoning": "Explanation of why this source is reliable for this query"
                  }}
              }}
           
           b) If query can be answered from MULTIPLE data sources but no need to decompose:
              Return dictionary with ALL possible sources containing query objects and confidence scores
              Example: {{
                  "email": {{
                      "query": "original query here",
                      "confidence": 0.7,
                      "reasoning": "Explanation for email confidence"
                  }},
                  "vessel": {{
                      "query": "original query here",
                      "confidence": 0.8,
                      "reasoning": "Explanation for vessel confidence"
                  }}
              }}
           
           c) If query needs decomposition across multiple sources:
              Return dictionary with INDEPENDENT sub-questions and confidence scores
              Example: {{
                  "email": {{
                      "query": "Find all schedule change emails from June 2023, extract vessel names and changes",
                      "confidence": 0.85,
                      "reasoning": "Emails contain direct schedule change communications"
                  }},
                  "voyage": {{
                      "query": "List all recorded schedule changes in June 2023 with vessel details",
                      "confidence": 0.9,
                      "reasoning": "Voyage database has authoritative schedule records"
                  }}
              }}

        Confidence Score Guidelines:
        - Score range: 0.0 to 1.0
        - 0.9-1.0: Source is authoritative for this information
        - 0.7-0.8: Source likely contains relevant information
        - 0.5-0.6: Source may contain partial information
        - Below 0.5: Source is not reliable for this query
        - Consider: data completeness, data reliability, data freshness
        - Each confidence score must include reasoning explanation

        CRITICAL RULES FOR DECOMPOSITION:
        1. Each sub-query MUST be completely independent
        2. NEVER reference "mentioned vessels" or "identified vessels" from other queries
        3. Include ALL search criteria in EACH sub-query
        4. Each sub-query should return its OWN complete set of results
        5. Provide confidence score and reasoning for EACH sub-query

        Response:
        """
        
    decompose_prompt = PromptTemplate(
        input_variables=["input_query", "email_example", "vessel_example", 
                        "voyage_example", "decomposition_examples"],
        template=decompose_template
    )

    decompose_chain = LLMChain(
        llm=llm,
        prompt=decompose_prompt
    )

    try:
        input_dict = {
            "input_query": query,
            "email_example": ConfigData.EMAIL_EXAMPLE,
            "vessel_example": ConfigData.VESSEL_EXAMPLE,
            "voyage_example": ConfigData.VOYAGE_EXAMPLE,
            "decomposition_examples": decomposition_examples
        }
        
        raw_response = decompose_chain.run(input_dict)
        
        if not raw_response or raw_response.isspace():
            return {}

        if raw_response.strip().startswith('{') and raw_response.strip().endswith('}'):
            try:
                import ast
                result_dict = ast.literal_eval(raw_response.strip())
                if isinstance(result_dict, dict):
                    valid_keys = {'email', 'vessel', 'voyage'}
                    cleaned_dict = {}
                    
                    for key, value in result_dict.items():
                        if key in valid_keys:
                            if isinstance(value, dict):
                                # Validate confidence score structure
                                if all(k in value for k in ['query', 'confidence', 'reasoning']):
                                    if isinstance(value['confidence'], (int, float)) and \
                                       0 <= value['confidence'] <= 1 and \
                                       isinstance(value['query'], str) and \
                                       isinstance(value['reasoning'], str):
                                        
                                        # Check for dependencies in query
                                        query_lower = value['query'].lower()
                                        dependency_indicators = [
                                            'mentioned', 'identified', 'found', 'above',
                                            'from the', 'these', 'those', 'previous'
                                        ]
                                        
                                        if not any(indicator in query_lower 
                                                 for indicator in dependency_indicators):
                                            cleaned_dict[key] = value
                    
                    # Validate minimum confidence threshold
                    cleaned_dict = {
                        k: v for k, v in cleaned_dict.items() 
                        if v['confidence'] >= 0.5
                    }
                    
                    return cleaned_dict if cleaned_dict else {}
                    
            except Exception as parse_error:
                print(f"Parsing error: {str(parse_error)}")
                return {}

        return {}

    except Exception as e:
        print(f"Error processing response: {str(e)}")
        print(f"Exception type: {type(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return {}
    

    