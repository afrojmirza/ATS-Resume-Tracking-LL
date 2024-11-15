import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
import PyPDF2 as pdf

# Define your API key directly in the model configuration
llm = GoogleGenerativeAI(model='gemini-1.5-flash-latest', api_key='AIzaSyAmRMUmWsJRtFPd8spj0SdgagPzDFS4Nl0')  # Replace with your actual API key

# Define a function to extract text from the uploaded PDF
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
resume: {resume_text}
description: {job_description}

I want the response in table format:
{{"JD Match":"%", "MissingKeywords":[],"Profile Summary":""}}
"""

# Create a PromptTemplate and LLMChain instance
prompt_template = PromptTemplate(input_variables=["resume_text", "job_description"], template=input_prompt)
chain = LLMChain(prompt=prompt_template, llm=llm)

# Streamlit app interface
st.title("Smart ATS")
st.text("Improve Your Resume for ATS")

# Job description input
jd = st.text_area("Please add your Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

# Submit button
if st.button("Submit"):
    if uploaded_file is not None and jd:
        resume_text = input_pdf_text(uploaded_file)
        
        # Generate response using the chain
        response = chain.invoke({"resume_text": resume_text, "job_description": jd})
        health_suggestions = response.get("text", "No suggestions available.")
        
        st.subheader("Evaluation Results")
        st.write(health_suggestions)
    else:
        st.warning("Please provide both the job description and upload your resume.")
