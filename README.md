# CodeMate AI – Your Personalized AI Coding Mentor

> Supercharge your DSA + CP prep with smart scrapers, AI feedback, roadmaps, weekly goals, PDF reports, interview simulation, security analysis, and even natural language to code/query tools – all 100% FREE and integrated with your existing coding profiles like LeetCode, Codeforces, GFG, CodeChef, HackerRank, and AtCoder.

---

## Why CodeMate AI?

Unlike static websites or video tutorials, **CodeMate AI** actively learns from your live progress on multiple coding platforms and gives you actionable suggestions, weekly targets, senior developer feedback, security scans, and mock interviews — all through a **Streamlit-based interactive dashboard**.

---

## Key Features

### Competitive Profile Integrator
- Enter your handles for:
  - LeetCode
  - Codeforces
  - GeeksforGeeks
  - CodeChef
  - AtCoder
  - HackerRank
- See your current ratings, problems solved, and upcoming contests.

### Smart Roadmap Generator
- Personalized suggestions based on your current strengths & weaknesses.
- Get topic-level suggestions (e.g., "Solve 5 Graph problems this week").

### Weekly Email Reminders
- Get gentle nudges in your inbox

### PDF Report Generator
- Download a progress report (useful for mentorship reviews, interviews).

### Code Evaluator + Code Translator
- Paste code and get feedback.
- Translate code from one language to another (e.g., Python to C++).

### Prompt to Code / SQL
- Just describe the task — get working code or SQL in return!

### Senior Developer Feedback Simulator
- Get mock review of your codebase with detailed suggestions.

### Security Scanner & Code Quality
- Scan your code for vulnerabilities and bad practices.

### Mock Interview Simulator
- Simulates behavioral + coding interviews based on your skill profile.

---

## Folder Structure
```bash
CodeMateAI/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── data/
│   └── user_data.json
├── scrapers/
    ├── __init__.py
│   ├── leetcode_scraper.py
│   ├── codeforces_scraper.py
│   ├── gfg_scraper.py
│   ├── codechef_scraper.py
│   ├── atcoder_scraper.py
│   └── hackerrank_scraper.py
├── roadmap_generator.py
├── weekly_emailer.py
├── pdf_report_generator.py
├── utils.py
├── code_evaluator.py
├── senior_dev_feedback.py
├── prompt_to_sql.py
├── prompt_to_code.py
├── prompt_to_code_translation.py
├── code_translator.py
├── security_scanner.py
├── codebase_analyzer.py
├── coding_interview_simulator.py
├── code_performance_benchmark.py
└── .streamlit/
    └── config.toml
```

## Installation

# 1. Download / Clone the repo
cd CodeMateAI

# 2. Create a virtual environment
python -m venv codemate-env
.\codemate-env\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file in root directory
# Example content:
EMAIL_ADDRESS=youremail@example.com
EMAIL_PASSWORD=your-app-password

# 5. Launch the app locally
streamlit run main.py
