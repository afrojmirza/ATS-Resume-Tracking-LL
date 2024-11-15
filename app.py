import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import json

# Configure the API key
genai.configure(api_key='AIzaSyAmRMUmWsJRtFPd8spj0SdgagPzDFS4Nl0')

def get_gemini_response(input_text):
    # Use the ChatGoogleGenerativeAI API to generate a response
    response = genai.generate_text(model='gemini-1.5-flash-latest', prompt=input_text)
    return response.result  # Access the result text from the response object

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page_content = reader.pages[page].extract_text()
        text += str(page_content)
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analysis,
and big data engineering. Your task is to evaluate the resume based on the given job description.
Consider that the job market is very competitive, and provide the best assistance for improving
the resume. Assign the percentage match based on JD and the missing keywords with high accuracy.
resume:{text}
description:{jd}

I want the response in table format:
{{"JD Match":"%", "MissingKeywords":[],"Profile Summary":""}}
"""

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume for ATS")

# Job description input
jd = st.text_area("Please add your Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

# Submit button
if st.button("Submit"):
    if uploaded_file is not None and jd:
        resume_text = input_pdf_text(uploaded_file)
        prompt_filled = input_prompt.format(text=resume_text, jd=jd)
        response = get_gemini_response(prompt_filled)
        st.subheader("Evaluation Results")
        st.write(response)
    else:
        st.warning("Please provide both the job description and upload your resume.")
