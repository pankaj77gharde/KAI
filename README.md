# KAI - Knowledge Artificial Intelligence

## Overview

KAI Assistant is a comprehensive data analysis platform designed specifically for the maritime industry. It integrates multiple data sources including emails, vessel information, and voyage data to provide intelligent insights and answers to user queries. The system uses advanced natural language processing and RAG (Retrieval Augmented Generation) techniques to analyze and present relevant information.

## Features

- **Multi-Source Data Integration**: Seamlessly combines data from:
  - Email communications
  - Vessel details and specifications
  - Voyage information and metrics

- **Intelligent Query Processing**:
  - Query decomposition for optimal data source utilization
  - Confidence scoring for source reliability
  - Advanced RAG pipeline for text data 
  - Advanced RAG pipeline with mongoDB queruy generation 

- **Interactive User Interface**:
  - Clean, modern web interface built with Streamlit
  - Real time query processing
  - Organized display of sources and responses
  - Collapsible source sections for better readability

- **Comprehensive Data Analysis**:
  - Vessel performance metrics
  - Financial analysis
  - Route optimization
  - Emissions tracking
  - Contract management

## Technical Architecture

### Core Components

1. **Query Decomposition Engine**
   - Analyzes user queries
   - Determines relevant data sources
   - Assigns confidence scores
   - Generates targeted sub-queries

2. **RAG Pipeline**
   - Processes email data using advanced NLP
   - Vector store implementation with FAISS
   - OpenAI embeddings integration
   - Efficient document chunking and retrieval

3. **Data Processing Systems**
   - MongoDB integration for vessel and voyage data
   - Advanced aggregation pipeline generation
   - Real-time data retrieval and analysis

4. **User Interface**
   - Streamlit-based web application
   - Responsive design
   - Interactive components
   - Organized data presentation

## Setup Requirements

### Prerequisites

- Python 3.7+
- MongoDB
- OpenAI API key
- FAISS 
- Required Python packages (see `requirements.txt`)

### Environment Variables

Configure the following in `config.py`:
- `OPEN_AI_KEY`: OpenAI API key
- `MONGO_DB_URI`: MongoDB connection string
- `DB_NAME`: Database name
- Additional configuration parameters as needed

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables
4. Initialize MongoDB with required collections
5. Process and index email data

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Access the web interface through your browser
3. Enter your query in the text area
4. Click "Get Answer" to process your query
5. View results with source information

## File Structure

- `app.py`: Main Streamlit application
- `config.py`: Configuration and schema definitions
- `decompose_query.py` : Decomposition query into requred number of quetions 
- `doc_email_retrival`: Retrive email data 
- `doc_vessel_retrival`: Query generation for mongobd vessel collection  
- `doc_voyage_retrival`: Query generation for mongobd voyage collection 
- `final_responce`: Use retrived data and create final responce 
- `retrive_decomp_query_data`: orchestra all three verticals with decompose query

## Data Models

### Email Data
- Structured text files containing communication details
- Includes metadata like sender, recipient, date, and subject
- Processed for efficient retrieval

### Vessel Data
- Comprehensive vessel specifications
- Performance profiles
- Contract information
- Technical details

### Voyage Data
- Route information
- Financial metrics
- Emissions data
- Operational details

## Acknowledgments
- OpenAI for providing the language models
- Streamlit for the web framework
- FAISS for vector storage capabilities
- MongoDB for database solutions