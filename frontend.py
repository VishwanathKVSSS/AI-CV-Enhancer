import streamlit as st
import requests

# Set Page Title
st.set_page_config(page_title="AI-Powered CV Enhancer", page_icon="📄")

st.title("🚀 AI-Powered CV Enhancer")
st.write("Optimize your resume bullet points based on job descriptions.")

# User Inputs
job_desc = st.text_area("🔹 Paste Job Description:")
resume_bullet = st.text_input("✍ Enter Resume Bullet Point:")

# Button to Optimize
if st.button("Enhance Bullet Point ✨"):
    if job_desc and resume_bullet:
        response = requests.post("http://127.0.0.1:8000/optimize_bullet", json={
            "job_description": job_desc,
            "resume_bullet": resume_bullet
        })
        try:
            response_json = response.json()
            if "optimized_bullet" in response_json:
                st.success(f"✅ Optimized Bullet: {response_json['optimized_bullet']}")
            else:
                st.error(f"⚠ API Error: {response_json.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"⚠ Failed to process API response: {str(e)}")

    else:
        st.error("⚠ Please enter both fields.")
