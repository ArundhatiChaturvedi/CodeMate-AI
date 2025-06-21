import streamlit as st
import random
import json
from scrapers import *
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
    
    def sanitize_username(input_str):
        return input_str.split("/")[-1] if "/" in input_str else input_str

    lc = sanitize_username(st.text_input("LeetCode Username"))
    cf = sanitize_username(st.text_input("Codeforces Handle"))
    gfg = sanitize_username(st.text_input("GeeksforGeeks Username"))
    cc = sanitize_username(st.text_input("CodeChef Username"))
    at = sanitize_username(st.text_input("AtCoder Username"))
    hr = sanitize_username(st.text_input("HackerRank Username"))
    
    st.markdown("**Note:** If you have a URL, paste it directly. Otherwise, just enter the username.")

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
        
        # Calculate totals and display summary
        total_solved = 0
        platform_data = []
        for platform, stats in user_stats.items():
            solved = stats.get("solved", 0)
            total_solved += solved
            platform_data.append((platform.capitalize(), solved))
        
        st.success("Stats fetched and saved!")
        st.divider()
        
        # Summary cards
        st.subheader("📊 Coding Profile Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Solved", total_solved)
        col2.metric("Platforms Connected", len(platform_data))
        col3.metric("Active Profiles", sum(1 for _, count in platform_data if count > 0))
        
        # Platform breakdown
        st.subheader("Platform Breakdown")
        for platform, count in platform_data:
            st.progress(count / max(1, total_solved), 
                       text=f"{platform}: {count} problems")
        
        # AI-generated topics
        topics_prompt = f"Analyze {user_stats} and list top 5 programming topics covered"
        topics = generate_code_from_prompt(topics_prompt)
        st.subheader("Topics Covered")
        st.markdown(topics)

# Tab 2: Analyze & Roadmap
with tab2:
    st.header("Personalized Coding Roadmap")
    
    if st.button("Generate Roadmap"):
        data = load_user_data()
        if data:
            roadmap = generate_combined_roadmap(data)
            
            # Topics summary (horizontal cards)
            st.subheader("Your Top Focus Areas")
            cols = st.columns(len(roadmap["topics"]))
            for i, topic in enumerate(roadmap["topics"]):
                with cols[i]:
                    st.markdown(f"""
                    <div style='
                        border: 1px solid #e0e0e0;
                        border-radius: 10px;
                        padding: 15px;
                        text-align: center;
                        background: #f9f9f9;
                        height: 120px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    '>
                    <b>{topic}</b>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Detailed roadmap with expanders
            st.subheader("📝 Your 2-Week Action Plan")
            with st.expander("View Full Plan", expanded=True):
                st.markdown(roadmap["detailed_plan"])
            
            # Progress tracking
            st.subheader("Progress Tracker")
            for day in range(1, 15):
                st.checkbox(f"Day {day}: Completed", key=f"day_{day}")
        else:
            st.warning("No user data found. Connect handles first!")
    
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
            with st.spinner('Generating...'):
                st.code(generate_code_from_prompt(prompt), language="python")
        
        st.subheader("Code Review")
        code = st.text_area("Paste your code for review:")
        context = st.text_input("Context (optional):")
        if st.button("Review as Senior Developer"):
            with st.spinner('Analyzing...'):
                st.markdown(review_code_as_senior(code, context))
        
        st.subheader("Security Scan")
        if st.button("Scan Code for Vulnerabilities"):
            issues = scan_security_issues(code)
            st.markdown("\n".join(issues) if isinstance(issues, list) else issues)
    
    with col2:
        st.subheader("Code Evaluator")
        if st.button("Run Code Evaluation"):
            st.write(evaluate_code(code))
        
        st.subheader("Prompt to SQL")
        nl = st.text_input("Ask a data question:")
        if st.button("Convert to SQL"):
            st.code(prompt_to_sql(nl), language="sql")
        
        st.subheader("Code Translator")
        from_lang = st.selectbox("From", ["python", "java", "cpp", "javascript"])
        to_lang = st.selectbox("To", ["java", "python", "cpp", "javascript"])
        if st.button("Translate"):
            st.code(translate_code(code, from_lang, to_lang), language=to_lang)
        
        st.subheader("Performance Benchmark")
        if st.button("Benchmark Code"):
            result = benchmark_code(code)
            st.write(result)
    
    st.markdown("---")
    st.subheader("Coding Interview Simulator")
    
    # Initialize session state
    if 'interview_active' not in st.session_state:
        st.session_state.interview_active = False
    if 'interview_question' not in st.session_state:
        st.session_state.interview_question = ""
    if 'interview_solution' not in st.session_state:
        st.session_state.interview_solution = ""
    
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
    
    if st.button("Simulate Interview", key="simulate_interview_main"):
        selected_question = random.choice(interview_questions)
        st.session_state.interview_question = selected_question
        result = simulate_interview(selected_question, 30)
        st.session_state.interview_active = True
        st.write(result)
    
    if st.session_state.interview_active:
        st.markdown(f"**Current Question:** {st.session_state.interview_question}")
        solution = st.text_area("Write your solution here:", height=300, key="solution_editor")
        st.session_state.interview_solution = solution
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Submit Solution", key="submit_solution_btn"):
                evaluation = evaluate_code(solution)
                st.session_state.evaluation_result = "\n".join(evaluation)
                st.success("Solution submitted for evaluation!")
        with col2:
            if st.button("End Interview", key="end_interview_btn"):
                st.session_state.interview_active = False
        with col3:
            if st.button("Clear Solution", key="clear_solution_btn"):
                st.session_state.interview_solution = ""
                st.experimental_rerun()
        
        if hasattr(st.session_state, 'evaluation_result'):
            st.subheader("Evaluation Feedback")
            st.write(st.session_state.evaluation_result)
            
            if st.button("Benchmark Solution Performance", key="benchmark_solution_btn"):
                benchmark_result = benchmark_code(st.session_state.interview_solution)
                st.write("Performance Metrics:")
                st.json(benchmark_result)

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
