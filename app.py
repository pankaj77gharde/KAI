import streamlit as st
import time
from PIL import Image
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.final_responce import main

def initialize_session_state():
    """Initialize session state variables"""
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    if 'show_sources' not in st.session_state:
        st.session_state.show_sources = {}

def format_response_text(text):
    """Format the response text with proper line breaks and styling"""
    # Split text into paragraphs and add proper spacing
    paragraphs = text.split('\n')
    formatted_paragraphs = []
    
    for para in paragraphs:
        if para.strip():  # Skip empty paragraphs
            # Add bullet points if line starts with "-" or "*"
            if para.strip().startswith(('-', '*')):
                formatted_paragraphs.append(f"{para}")
            else:
                formatted_paragraphs.append(f"{para}")
    
    return '\n\n'.join(formatted_paragraphs)

def display_chat_history():
    """Display chat history with improved formatting, showing latest response first"""
    # Reverse the history list to show latest response at the top
    for idx, (query, response_data) in enumerate(reversed(st.session_state.history)):
        # Calculate the real index for the session state
        real_idx = len(st.session_state.history) - 1 - idx
        
        # Initialize source visibility state
        if real_idx not in st.session_state.show_sources:
            st.session_state.show_sources[real_idx] = {'email': False, 'voyage': False, 'vessel': False}

        with st.container():
            # User Query Section
            st.markdown("#### 👤 Your Query")
            st.info(query)
            
            # KAI Response Section
            st.markdown("#### 🤖 KAI's Response")
            formatted_response = format_response_text(response_data['response'])
            
            # Create a response container with custom styling
            with st.container():
                st.markdown(f"""
                <div style="background-color: #E7F7E7; padding: 20px; border-radius: 10px;">
                    {formatted_response}
                </div>
                """, unsafe_allow_html=True)
            
            # Sources Section
            st.markdown("#### 📚 Sources")
            
            # Create three columns for sources with better spacing
            col1, col2, col3 = st.columns([1, 1, 1])
            
            # Email Sources
            with col1:
                st.markdown("##### 📧 Email Sources")
                if response_data['email_sources']:
                    if st.button(
                        f"{'Hide' if st.session_state.show_sources[real_idx]['email'] else 'Show'} Sources", 
                        key=f"email_{real_idx}"
                    ):
                        st.session_state.show_sources[real_idx]['email'] = not st.session_state.show_sources[real_idx]['email']
                    
                    if st.session_state.show_sources[real_idx]['email']:
                        for source in response_data['email_sources']:
                            st.markdown(f"- {source}")
                else:
                    st.markdown("*No email sources*")
            
            # Voyage Sources
            with col2:
                st.markdown("##### 📦 Voyage Sources")
                if response_data['voyage_sources']:
                    if st.button(
                        f"{'Hide' if st.session_state.show_sources[real_idx]['voyage'] else 'Show'} Sources", 
                        key=f"voyage_{real_idx}"
                    ):
                        st.session_state.show_sources[real_idx]['voyage'] = not st.session_state.show_sources[real_idx]['voyage']
                    
                    if st.session_state.show_sources[real_idx]['voyage']:
                        for source in response_data['voyage_sources']:
                            st.markdown(f"- {source}")
                else:
                    st.markdown("*No voyage sources*")
            
            # Vessel Sources
            with col3:
                st.markdown("##### 🚢 Vessel Sources")
                if response_data['vessel_sources']:
                    if st.button(
                        f"{'Hide' if st.session_state.show_sources[real_idx]['vessel'] else 'Show'} Sources", 
                        key=f"vessel_{real_idx}"
                    ):
                        st.session_state.show_sources[real_idx]['vessel'] = not st.session_state.show_sources[real_idx]['vessel']
                    
                    if st.session_state.show_sources[real_idx]['vessel']:
                        for source in response_data['vessel_sources']:
                            st.markdown(f"- {source}")
                else:
                    st.markdown("*No vessel sources*")
            
            st.divider()

def process_query(query: str):
    """Process the user query and return response with sources"""
    try:
        response = main(query)
        if isinstance(response, dict) and 'text' in response:
            return {
                'response': response["text"],
                'email_sources': response["input_email"],
                'voyage_sources': response["input_voyage"],
                'vessel_sources': response["input_vessel"]
            }
            
    except Exception as e:
        # st.error(f"An error occurred: {str(e)}")
        print(e)
        return {
            'response': "I apologize, but I encountered an issue. Please try again.",
            'email_sources': [],
            'voyage_sources': [],
            'vessel_sources': []
        }

def main_ui():
    st.set_page_config(
        page_title="KAI Assistant",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    initialize_session_state()
    # st.image(r"C:\vnit\Mini_project\exp_test_2\assets\kai_logo.png", width=50)
    # Main title and description with improved formatting
    # st.markdown("""
    # <img src=r'C:\vnit\Mini_project\exp_test_2\assets\kai_logo.png' width='50'/> 
    # # KAI Assistant
    
    # Welcome to the KAI Assistant! 
    
    # One stop solution to get answers from all verticals of organizational data for better deals and management.
    
    # Simply type your question below and I'll help you find the relevant information.
    # """)
    
    # col1, col2 = st.columns([3,20])  

    # with col1:
    st.image(r"C:\vnit\Mini_project\demo3\images\kai.png", width= 200)  ###############################
    # with col2:
    #     st.markdown("<h1 style='font-size: 60px;'><span style='color: #006994;'></h1>", unsafe_allow_html=True)

    st.markdown("""
    <div>Welcome to the KAI Assistant!</div>
    <div style='padding-left: 40px;'>Simply type your question below and I'll help you find the relevant information.</div>
    """, unsafe_allow_html=True)
    st.markdown("<hr style='height: 2px; background-color: #e5e5e5; border: none;'>", unsafe_allow_html=True)
    
    # Query input with improved styling
    query = st.text_area(
        "Enter your query:",
        height=100,
        placeholder="Example: What vessels were mentioned in recent emails?",
        help="Type your question here and press 'Get Answer' to receive a response."
    )
    
    # Process button with improved styling
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("🔍 Get Answer", type="primary", use_container_width=True):
            if not query:
                st.warning("⚠️ Please enter a query first.")
                return
            
            st.session_state.processing = True
            
            with st.spinner("🔄 Processing your query..."):
                time.sleep(0.5)
                response_data = process_query(query)
                st.session_state.history.append((query, response_data))
            
            st.session_state.processing = False
    
    # Display chat history
    if st.session_state.history:
        st.markdown("### 💬 Chat History")
        display_chat_history()
    
    # Footer with improved styling
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666666;'>
        <p>KAI Assistant | Powered by VNIT</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main_ui()