

# Smart ATS

**Smart ATS** is an AI-powered application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). It evaluates resumes against job descriptions to provide a compatibility score, identify missing keywords, and suggest improvements. The project leverages **Google Generative AI**, **LangChain**, and **Streamlit** to deliver an intuitive and effective resume optimization experience.

---

## Key Features

- **Resume Evaluation**: Compares your resume with the provided job description.
- **ATS Compatibility Check**: Analyzes the resume and provides a JD match percentage.
- **Keyword Suggestions**: Identifies missing keywords from the job description.
- **Profile Summary Improvement**: Offers a concise summary for better alignment with the job.
- **Interactive UI**: User-friendly Streamlit interface for seamless interaction.

---

## Technologies Used

- **Programming Language**: Python
- **Frameworks & Libraries**:
  - **Streamlit**: For building the interactive web app.
  - **LangChain**: To create AI-driven task pipelines.
  - **Google Generative AI**: For advanced natural language processing.
  - **PyPDF2**: To extract text from PDF resumes.

---

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Set Up a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up the API Key
- Replace the placeholder `api_key` in the code with your **Google Generative AI API Key**:
  ```python
  api_key = 'YOUR_API_KEY_HERE'
  ```

---

## Usage

### Step 1: Run the Application
```bash
streamlit run app.py
```

### Step 2: Open the Web App
- The application will open in your default web browser at `http://localhost:8501`.

### Step 3: Upload Resume and Add Job Description
1. Enter the **Job Description** in the provided text area.
2. Upload your **Resume (PDF format)**.
3. Click the **Submit** button.

### Step 4: View Results
- The application will display:
  - **JD Match Percentage**.
  - **Missing Keywords** from the job description.
  - **Profile Summary** for better alignment.

---

## Project Structure

```plaintext
├── app.py                 # Main application script
├── requirements.txt       # List of project dependencies
├── README.md              # Project documentation
└── assets/                # (Optional) Folder for screenshots
```

---

## Example Screenshots

### 1. Home Page
![Home Page](assets/home_page.png)

### 2. Evaluation Results
![Evaluation Results](assets/evaluation_results.png)

---

## Future Enhancements

- Support for additional file formats (e.g., DOCX).
- Integration with LinkedIn for real-time job recommendations.
- Advanced suggestions based on industry trends.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve the project.

---


