import streamlit as st
import random
from scrapers.leetcode_scraper import fetch_leetcode_data
from scrapers.codeforces_scraper import fetch_codeforces_data
from scrapers.gfg_scraper import fetch_gfg_data
from scrapers.codechef_scraper import fetch_codechef_data
from scrapers.atcoder_scraper import fetch_atcoder_data
from scrapers.hackerrank_scraper import fetch_hackerrank_data

from roadmap_generator import generate_roadmap
from pdf_report_generator import generate_pdf
from weekly_emailer import send_weekly_email
from utils import load_user_data, save_user_data

from code_evaluator import evaluate_code
from senior_dev_feedback import review_code_as_senior
from prompt_to_sql import prompt_to_sql
from code_translator import translate_code
from prompt_to_code import prompt_to_code as generate_code_from_prompt
from security_scanner import scan_security_issues
from coding_interview_simulator import simulate_interview
from code_performance_benchmark import benchmark_code
from codebase_analyzer import analyze_codebase

st.set_page_config(page_title="CodeMate AI", layout="wide")

st.title("CodeMate AI - Your Personalized Coding Mentor")

tab1, tab2, tab3, tab4 = st.tabs(["Connect Handles", "Analyze & Roadmap", "AI Tools", "PDF & Email"])

# Tab 1: Connect Handles
with tab1:
    st.header("Enter Your Coding Handles")
    lc = st.text_input("LeetCode Username")
    cf = st.text_input("Codeforces Handle")
    gfg = st.text_input("GeeksforGeeks Username")
    cc = st.text_input("CodeChef Username")
    at = st.text_input("AtCoder Username")
    hr = st.text_input("HackerRank Username")

    if st.button("Fetch Stats & Save"):
        user_stats = {
            "leetcode": fetch_leetcode_data(lc) if lc else {},
            "codeforces": fetch_codeforces_data(cf) if cf else {},
            "gfg": fetch_gfg_data(gfg) if gfg else {},
            "codechef": fetch_codechef_data(cc) if cc else {},
            "atcoder": fetch_atcoder_data(at) if at else {},
            "hackerrank": fetch_hackerrank_data(hr) if hr else {}
        }
        save_user_data(user_stats)
        st.success("Stats fetched and saved!")

# Tab 2: Analyze & Roadmap
with tab2:
    st.header("Analyze Profile & Get Roadmap")
    if st.button("Generate Roadmap"):
        data = load_user_data()
        if data:
            roadmap = generate_roadmap(data)
            st.markdown(roadmap)
        else:
            st.warning("No user data found. Please connect handles first.")

    st.markdown("---")
    st.subheader("Analyze Codebase")
    uploaded_folder = st.text_input("Enter path to your local codebase folder")
    if st.button("Analyze Codebase"):
        if uploaded_folder:
            summary = analyze_codebase(uploaded_folder)
            st.json(summary)

# Tab 3: AI Tools
with tab3:
    st.header("Intelligent AI Assistants")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Prompt to Code")
        prompt = st.text_area("Describe what you want to build:")
        if st.button("Generate Code"):
            st.code(generate_code_from_prompt(prompt), language="python")

        st.subheader("Code Review")
        code = st.text_area("Paste your code for review:")
        context = st.text_input("Context (optional):")
        if st.button("Review as Senior Developer"):
            st.markdown(review_code_as_senior(code,context))

        st.subheader("Security Scan")
        if st.button("Scan Code for Vulnerabilities"):
            issues = scan_security_issues(code)
            st.markdown(issues)

    with col2:
        st.subheader("Code Evaluator")
        if st.button("Run Code Evaluation"):
            st.write(evaluate_code(code))

        st.subheader("Prompt to SQL")
        nl = st.text_input("Ask a data question:")
        if st.button("Convert to SQL"):
            st.code(prompt_to_sql(nl), language="sql")

        st.subheader("Code Translator")
        from_lang = st.selectbox("From", ["python", "java", "cpp"])
        to_lang = st.selectbox("To", ["java", "python", "cpp"])
        if st.button("Translate"):
            st.code(translate_code(code, from_lang, to_lang), language=to_lang)

        st.subheader("Performance Benchmark")
        if st.button("Benchmark Code"):
            result = benchmark_code(code)
            st.write(result)

    st.markdown("---")  
    st.subheader("Coding Interview Simulator")
    interview_questions = [
    "Reverse a linked list",
    "Find the middle element of a linked list",
    "Implement a stack using queues",
    "Check if a binary tree is balanced",
    "Implement an LRU cache",
    "Find the longest substring without repeating characters",
    "Rotate an array to the right by k steps",
    "Design a parking lot system"
    ]  

    selected_question = random.choice(interview_questions)
i   if st.button("Simulate Interview"):
        result = simulate_interview(selected_question, 30)
        st.write(result)


# Tab 4: PDF & Email
with tab4:
    st.header("Weekly Reminder + Progress Report")
    email = st.text_input("Enter your email:")
    
    if st.button("Send Weekly Email"):
        data = load_user_data()
        roadmap = generate_roadmap(data) if data else "No roadmap available"
        result = send_weekly_email(email, roadmap)
        if result is True:
            st.success("Email sent!")
        else:
            st.error(f"Failed to send email: {result}")

    if st.button("Generate PDF Report"):
        generate_pdf(load_user_data())
        st.success("PDF report saved!")

st.markdown("---")
st.caption("© 2025 CodeMate AI | Arundhati Chaturvedi")
