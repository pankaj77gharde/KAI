
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.doc_email_retrival import EmailRAGPipeline 
from src.doc_vessel_retrival import vess_get_final_out
from src.doc_voyage_retrival import vog_get_final_out
from src.decompose_query import decomposeme 
from CONFIG.config import ConfigData

def pipline_run(query_input):
    # emails_dir = r"C:\vnit\Mini_project\demo3\data\Emails\processed_emails"
    # openai_api_key = ConfigData.OPEN_AI_KEY
    
    emails_dir = r"C:\vnit\Mini_project\demo3\data\Emails\processed_emails"
    openai_api_key = ConfigData.OPEN_AI_KEY
    vector_store_path = "email_vector_store"

    # pipeline = EmailRAGPipeline(
    #     emails_dir=emails_dir,
    #     openai_api_key=openai_api_key
    # )
    pipeline = EmailRAGPipeline(
    emails_dir=emails_dir,
    openai_api_key=openai_api_key,
    vector_store_path=vector_store_path)
    
    # decompose query 
    decomp_querys_dict = decomposeme(query_input)
    print(decomp_querys_dict)
    
    list_keys = list(decomp_querys_dict.keys())
    sources_dict = {}
    for type_doc in list_keys:
        print(f"$$$$$$$$$$$$$$$$$$$$$ {type_doc} $$$$$$$$$$$$$$$$$$$$$$$$")
        if type_doc == "email":
            neseted_dict = decomp_querys_dict[type_doc]
            print(f"$$$$$$$$$$$$$$$$$$$$$ {neseted_dict['confidence']} $$$$$$$$$$$$$$$$$$$$$$$$")
            if neseted_dict["confidence"] >= 0.8 :
                query = neseted_dict["query"]
                print("############################## email #################################")
                print(query)
                response = pipeline.process_query(query) # pipeline.process_query(query)
                print(response["sources"])
                sources_dict["email"] = response["sources"]
                print("###################################################") 
        elif type_doc == "voyage":
            neseted_dict = decomp_querys_dict[type_doc]
            print(f"$$$$$$$$$$$$$$$$$$$$$ {neseted_dict['confidence']} $$$$$$$$$$$$$$$$$$$$$$$$")
            if neseted_dict["confidence"] >= 0.8 :
                vo_query = neseted_dict["query"]
                print("############################## voyage #################################")
                print(vo_query)
                response = vog_get_final_out(vo_query) 
                print(response)
                sources_dict["voyage"] = response
                print("######################## here i am ###########################") 
        elif type_doc == "vessel":
            neseted_dict = decomp_querys_dict[type_doc]
            print(f"$$$$$$$$$$$$$$$$$$$$$ {neseted_dict['confidence']} $$$$$$$$$$$$$$$$$$$$$$$$")
            if neseted_dict["confidence"] >= 0.8 :
                ve_query = neseted_dict["query"]
                print("############################## vessel #################################")
                print(ve_query)
                response = vess_get_final_out(ve_query) 
                print(response)
                sources_dict["vessel"] = response
                print("###################################################") 
        else:
            print(f"{type_doc} is unknown type of document, please chcek input.")
            
    return sources_dict 