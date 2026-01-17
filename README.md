# AI-Powered Cyber Threat Simulation & Detection System

A complete cybersecurity simulation framework that processes synthetic attacks through a multi-layered detection pipeline involving Rule-Based Heuristics, OpenAI GPT-4o, and Google Gemini.

> **Disclaimer**: This tool is for educational and defensive purposes only. It generates **safe**, non-executable synthetic data.

---

## 🌟 Key Features

- **Red Team Simulation**: Generates realistic (safe) phishing emails, malicious URLs, and obfuscated script snippets.
- **Multi-Model Detection**:
  - **Rule-Based**: Instant detection of known patterns (e.g., `<script>`, `.exe`).
  - **OpenAI GPT-4o**: Context-aware analysis of phishing intent and social engineering.
  - **Google Gemini**: Secondary verification to reduce false positives.
- **Real-Time Dashboard**: Streamlit interface to see attacks and AI analysis live.
- **Automated Reporting**: Generates markdown executive summaries for stakeholders.
- **Orchestration Engine**: "Highest Severity Wins" logic ensures critical threats aren't missed.

---

## 🏗️ Architecture

The system operates in a rigorous linear pipeline:

1.  **Attack Generation**: `attack_generator` creates synthetic threats.
2.  **Ingestion**: Attacks are stored in SQLite with a status of `Pending`.
3.  **Detection Pipeline** (`final_decision.py`):
    *   **Layer 1 (Static)**: Regex & keyword matching. Fast, low compute.
    *   **Layer 2 (Semantic)**: OpenAI API analyzes the *intent* of the text.
    *   **Layer 3 (Verification)**: Gemini API provides a second opinion.
    *   **Layer 4 (Consensus)**: The system takes the *highest* risk score from all 3 layers.
4.  **Presentation**: Dashboard and Reports visualize the data.

---

## 🚀 Setup Instructions

### 1. Prerequisites
- **Python 3.9+** installed.
- **API Keys** for:
  - OpenAI (Credits required, free tier may be limited).
  - Google Gemini (Google AI Studio).

### 2. Installation
```bash
# 1. Clone the repository (if not already local)
# git clone https://github.com/your-repo/ai-cyber-threat-simulator.git
cd ai-cyber-threat-simulator

# 2. Install Python dependencies
pip install -r requirements.txt
```

### 3. Configuration
The system uses a `.env` file to manage secrets securely.

1.  Create or edit the `.env` file in the project root:
    ```bash
    # Linux/Mac
    touch .env
    ```
2.  Add your keys (replace with your actual secrets):
    ```ini
    OPENAI_API_KEY=sk-proj-12345...
    GOOGLE_API_KEY=AIzaSy...
    ```

### 4. Initialize Database
Create the SQLite database and tables:
```bash
python database/init_db.py
```

---

## 💻 Usage Guide

### Step 1: Generate Attacks (Red Team)
Populate the database with new synthetic threats:
```bash
python attack_generator/generate_attacks.py
```
*Output: Generates 10-20 random phishing/script/URL events.*

### Step 2: Run Detection Engine (Blue Team)
Process pending attacks through the AI models:
```bash
python detection_engine/final_decision.py
```
*Output: Analyzes each attack, queries APIs, and saves results.*

### Step 3: View Dashboard (SOC View)
Launch the real-time web interface:
```bash
streamlit run dashboard/app.py
```
*Access at: `http://localhost:8501`*

### Step 4: Generate Report
Create a static Markdown summary for review:
```bash
python reports/generate_report.py
```
*Report saved to: `reports/executive_summary.md`*

---

## 📂 Project Structure

```text
ai-cyber-threat-simulator/
├── attack_generator/       # Red Team tools
│   └── generate_attacks.py # Generates safe fake threats
├── detection_engine/       # Blue Team AI logic
│   ├── rule_detector.py    # Regex/Keyword logic
│   ├── openai_analyzer.py  # GPT-4o integration
│   ├── gemini_analyzer.py  # Gemini integration
│   └── final_decision.py   # Main pipeline orchestrator
├── dashboard/              # UI layer
│   └── app.py              # Streamlit web app
├── database/               # Persistence
│   ├── init_db.py          # Schema setup
│   └── attacks.db          # SQLite database (auto-created)
├── reports/                # Output
│   └── generate_report.py  # Report generator script
├── .env                    # API Keys (Git ignored)
├── config.py               # Central config loader
├── requirements.txt        # Python libraries
└── README.md               # This file
```

---

## 🔧 Troubleshooting

### Common Errors

#### 1. `OpenAI Error: 429 - You exceeded your current quota`
*   **Cause**: Your OpenAI API account is out of credits.
*   **Fix**: Go to [OpenAI Billing](https://platform.openai.com/account/billing/overview) and add credits ($5 minimum). Free tiers often expire after 3 months.

#### 2. `Gemini Error: 404 - models/gemini-1.5-flash is not found`
*   **Cause**: The model version might be deprecated or your API key doesn't have access.
*   **Fix**: 
    - Open `detection_engine/gemini_analyzer.py`.
    - Change `gemini-1.5-flash` to `gemini-pro`.
    - Ensure "Generative AI API" is enabled in your Google Cloud Console.

#### 3. `ModuleNotFoundError: No module named ...`
*   **Cause**: Dependencies aren't installed.
*   **Fix**: Run `pip install -r requirements.txt` again.

---

## 📝 Interview & Resume Materials

### Resume-Ready Description
**Project: AI-Powered Cyber Threat Simulation & Detection System**
*   **Architecture**: Designed a modular Python framework decoupling attack simulation (Red Team) from threat detection (Blue Team) using SQLite as an intermediate message broker.
*   **AI Integration**: Orchestrated a multi-LLM pipeline (GPT-4o + Gemini) to analyze unstructured text data (phishing emails), achieving higher accuracy than traditional pattern matching alone.
*   **Visualization**: Built a reactive SOC dashboard using Streamlit to visualize threat distribution and real-time AI reasoning logs.
*   **Engineering**: Implemented robust error handling, environment variable security pattern, and clean architecture principles.

### Interview Explanation (STAR Method)

**Situation**: Traditional rule-based firewalls often miss context-heavy attacks like Social Engineering or obfuscated scripts.

**Task**: Create a detection system that combines the speed of rules with the reasoning of Large Language Models, suitable for a portfolio demonstration.

**Action**: 
- I built a **hybrid detection engine**. First, a fast Python regex filter catches obvious threats.
- Second, I integrated **OpenAI** to analyze the "tone" and "urgency" of emails (common phishing traits).
- Third, I added **Google Gemini** as a "second opinion" validator.
- I tied it all together with a **Streamlit dashboard** that successfully demonstrated live attack-defense loops.

**Result**: The system successfully differentiates between legitimate "urgent" emails and phishing attempts, providing a clear "Risk Score" and "AI Explanation" for security analysts.

---

## 👨‍💻 About the Author

**👋 Hi, I'm Shyamji**

I am a cybersecurity, data science, and AI-focused professional with hands-on experience in building practical, Python-based systems for cyber threat simulation, detection, and risk analysis. My work combines **data-driven analysis**, **rule-based security logic**, and **Generative AI models** to solve real-world security problems.

I enjoy developing end-to-end, executable solutions that reflect real **Security Operations Center (SOC)** workflows, including:
*   Threat classification
*   Analytical dashboards
*   Automated security reporting
