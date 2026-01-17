# AI-Powered Cyber Threat Simulation & Detection System

A complete cybersecurity simulation framework that processes synthetic attacks through a multi-layered detection pipeline involving Rule-Based Heuristics, OpenAI GPT-4o, and Google Gemini 1.5 Flash.

> **Disclaimer**: This tool is for educational and defensive purposes only.

---

## 🏗️ Architecture

The system operates in a linear flow:

1.  **Red Team Module**: Generates safe synthetic attacks (Phishing, Malicious URLs, Scripts).
2.  **Database Layer**: SQLite stores all events.
3.  **Blue Team Detection Engine**:
    *   **Step 1 - Rule-Based**: Standard pattern matching (Regex/Keywords).
    *   **Step 2 - OpenAI**: Semantic analysis and intent classification.
    *   **Step 3 - Gemini**: Independent verification and context checking.
    *   **Step 4 - Decision Engine**: Aggregates scores (High > Medium > Low) and updates the database.
4.  **Reporting & Dashboard**: Automated Markdown reports and real-time Streamlit visualization.

---

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.9+
- OpenAI API Key
- Google Gemini API Key

### 2. Installation
```bash
# Clone the repository (if applicable) or navigate to root
cd ai-cyber-threat-simulator

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
1.  Open `.env` file.
2.  Add your API keys:
    ```env
    OPENAI_API_KEY=sk-...
    GOOGLE_API_KEY=AIza...
    ```

### 4. Initialize Database
```bash
python database/init_db.py
```

---

## 💻 Usage Commands

### Phase 1: Attack Simulation (Red Team)
Generate synthetic attacks:
```bash
python attack_generator/generate_attacks.py
```

### Phase 2: Threat Detection (Blue Team)
Run the AI analysis pipeline:
```bash
python detection_engine/final_decision.py
```

### Phase 3: Reporting
Generate an executive summary:
```bash
python reports/generate_report.py
```

### Phase 4: Control Dashboard
Launch the interactive UI:
```bash
streamlit run dashboard/app.py
```

---

## 📝 Interview & Resume Materials

### Resume-Ready Description
**Project: AI-Powered Cyber Threat Simulation & Detection System**
*   Designed and built a full-stack automated threat detection pipeline using Python and SQLite.
*   Implemented a multi-model approach combining Rule-Based Heuristics with LLM analysis (OpenAI GPT-4o & Gemini 1.5) to reduce false positives.
*   Developed a "Red Team" module to simulate phishing and script injection attacks for system stress testing.
*   Created a real-time Streamlit dashboard for monitoring threat severity and analyzing AI-generated risk assessmenets.

### Interview Explanation (STAR Method)

**Situation**: I needed to demonstrate how modern AI can augment traditional cybersecurity detection methods against evolving threats like sophisticated phishing.

**Task**: Build a system that not only detects threats using standard rules but also leverages multiple LLMs for deeper context analysis, without relying on complex enterprise infrastructure.

**Action**: 
- I architected a Python-based pipeline where synthetic attacks are first filtered by regex heuristics. 
- Suspicious items are then sent to OpenAI and Gemini asynchronously for second and third opinions.
- I implemented a "Highest Severity Wins" logic in the final decision engine to prioritize safety.
- I used SQLite for lightweight persistence and Streamlit for immediate visual feedback.

**Result**: The system successfully identifies complex phishing attempts that rule-based systems miss, provides detailed AI-generated explanations for analysts, and visualizes the risk landscape in real-time.
