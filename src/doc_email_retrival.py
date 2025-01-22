
import os
from typing import List, Dict
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import logging
from CONFIG.config import ConfigData

class EmailRAGPipeline:
    def __init__(self, emails_dir: str, openai_api_key: str, vector_store_path: str = "email_vector_store"):
        """
        Initialize the RAG pipeline for email querying.
        
        Args:
            emails_dir (str): Directory containing formatted email txt files
            openai_api_key (str): OpenAI API key for accessing models
            vector_store_path (str): Path to save/load vector store
        """
        self.emails_dir = emails_dir
        self.openai_api_key = openai_api_key
        self.vector_store_path = vector_store_path
        self.embeddings = None
        self.vector_store = None
        self.qa_chain = None
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Initialize the pipeline
        self._setup_pipeline()

    def _setup_embeddings(self):
        """Setup OpenAI embeddings"""
        self.logger.info("Setting up OpenAI embeddings")
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=self.openai_api_key
        )

    def _check_existing_vector_store(self) -> bool:
        """Check if a vector store already exists at the specified path"""
        return os.path.exists(self.vector_store_path)

    def _setup_pipeline(self):
        """Setup the complete pipeline"""
        try:
            # Setup embeddings first as they're needed for both paths
            self._setup_embeddings()
            
            # Check for existing vector store
            if self._check_existing_vector_store():
                self.logger.info(f"Found existing vector store at {self.vector_store_path}")
                self.load_vector_store(self.vector_store_path)
            else:
                self.logger.info("No existing vector store found. Creating new one...")
                # Load and process documents
                documents = self._load_documents()
                texts = self._split_documents(documents)
                
                # Setup vector store
                self._setup_vector_store(texts)
                
                # Save the newly created vector store
                self.save_vector_store(self.vector_store_path)
            
            # Setup QA chain
            self._setup_qa_chain()
            
            self.logger.info("Pipeline setup completed successfully")
            
        except Exception as e:
            self.logger.error(f"Error setting up pipeline: {str(e)}")
            raise

    def _load_documents(self) -> List:
        """Load documents from the emails directory"""
        self.logger.info(f"Loading documents from {self.emails_dir}")
        loader = DirectoryLoader(
            self.emails_dir,
            glob="*.txt",
            loader_cls=TextLoader
        )
        documents = loader.load()
        return documents

    def _split_documents(self, documents: List, chunk_size: int = 500):
        """Split documents into chunks"""
        self.logger.info("Splitting documents into chunks")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=50,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        texts = text_splitter.split_documents(documents)
        return texts

    def _setup_vector_store(self, texts: List):
        """Setup FAISS vector store"""
        self.logger.info("Setting up FAISS vector store")
        self.vector_store = FAISS.from_documents(
            texts,
            self.embeddings
        )

    def _setup_qa_chain(self):
        """Setup the QA chain"""
        self.logger.info("Setting up QA chain")
        
        prompt_template = """You are a helpful assistant that answers questions about email content.
        Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Keep your answers concise and to the point.
        
        Context: {context}
        
        Question: {question}
        
        Answer: """

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        # llm = OpenAI(
        #     temperature=0.3,
        #     model_name='gpt-3.5-turbo-0125',
        #     openai_api_key=self.openai_api_key,
        #     max_tokens=500
        # )
        llm = ChatOpenAI(openai_api_key=ConfigData.OPEN_AI_KEY, model='gpt-4-0125-preview', temperature=0)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(
                search_kwargs={"k": 3}
            ),
            chain_type_kwargs={"prompt": PROMPT},
            return_source_documents=True,
            callbacks=[StreamingStdOutCallbackHandler()]
        )

    def process_query(self, query: str) -> Dict:
        """
        Process a user query and return the answer with sources.
        
        Args:
            query (str): User's question about email content
            
        Returns:
            Dict: Contains answer and source documents
        """
        try:
            self.logger.info(f"Processing query: {query}")
            result = self.qa_chain({"query": query})
            
            response = {
                "answer": result["result"],
                "sources": [doc.page_content for doc in result["source_documents"]]
            }
            
            return response
            
        except Exception as e:
            self.logger.error(f"Error processing query: {str(e)}")
            return {
                "answer": "Sorry, I encountered an error processing your query.",
                "sources": []
            }

    def save_vector_store(self, path: str = None):
        """Save the vector store for later use"""
        save_path = path or self.vector_store_path
        if self.vector_store:
            self.vector_store.save_local(save_path)
            self.logger.info(f"Vector store saved to {save_path}")

    def load_vector_store(self, path: str = None):
        """Load a previously saved vector store"""
        load_path = path or self.vector_store_path
        if os.path.exists(load_path):
            self.vector_store = FAISS.load_local(
                load_path, 
                self.embeddings,
                allow_dangerous_deserialization=True  # Safe to use since we created these files
            )
            self.logger.info(f"Vector store loaded from {load_path}")