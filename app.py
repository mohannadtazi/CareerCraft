__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import tempfile
import os
from src_py.crew import crew
import asyncio

if not asyncio.get_event_loop().is_running():
    asyncio.set_event_loop(asyncio.new_event_loop())


# Set favicon and page configuration
fav_icon = Image.open("CareerCraft.png")
st.set_page_config(page_title="Career Craft", page_icon=fav_icon)

st.title('Career Craft')
st.write('Welcome to Career Craft! This platform allows you to explore different career paths and learn about the skills required for each career. You can also take a quiz to find out which career path suits you the best!')

# File uploader for resume
def convert_file_url_to_path(file_url):
    if file_url.startswith("file:///"):
        return file_url[7:]  # Remove 'file:///' (7 characters)
    return file_url


resume = st.file_uploader('Upload your resume here', type=["pdf", "docx"])
temp_file_path=""
if resume:
    # Create a temporary file to store the uploaded CV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf" if resume.type == "application/pdf" else ".docx") as temp_file:
        temp_file.write(resume.getbuffer())
        temp_file_path = file_path = convert_file_url_to_path(temp_file.name)
    st.info('Resume uploaded successfully!')

    # Input for desired position
    position = st.text_input('Desired position')
    
    st.write('Click the button below to get started!')

    if st.button('Get started!'):
        st.write('The job search has been initiated! Please wait for the results.')
        
        # Kickoff the Crew AI process
        result = crew.kickoff({"position": position, "pdf_url": temp_file_path})
        
        st.write('The job search has been completed! Please check the results below.')
        st.write(result.raw)

        # Read and display the profile analysis markdown file
        profile_file_path = 'profile_analysis.md'  # Ensure this file exists in your directory
        if os.path.exists(profile_file_path):
            with open(profile_file_path, 'r') as profile_file:
                profile_content = profile_file.read()
            st.markdown(profile_content)
        else:
            st.error("Profile analysis file not found.")
