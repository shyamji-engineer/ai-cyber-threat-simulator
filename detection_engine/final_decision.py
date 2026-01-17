import sqlite3
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATABASE_PATH
from detection_engine.rule_detector import rule_based_detection
from detection_engine.openai_analyzer import analyze_with_openai
from detection_engine.gemini_analyzer import analyze_with_gemini

def calculate_severity_score(risk_level):
    """Convert risk level to numeric score for comparison."""
    if risk_level == "High": return 3
    if risk_level == "Medium": return 2
    if risk_level == "Low": return 1
    return 0

def run_detection_pipeline():
    """
    Step 4: Final Risk Decision Engine
    Orchestrates the full detection pipeline.
    """
    print("Starting Detection Pipeline...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Fetch pending attacks
    cursor.execute("SELECT id, attack_type, content FROM attacks WHERE final_risk = 'Pending'")
    pending_attacks = cursor.fetchall()
    
    print(f"Found {len(pending_attacks)} pending attacks to analyze.")
    
    for attack in pending_attacks:
        attack_id, attack_type, content = attack
        print(f"Analyzing Attack #{attack_id} ({attack_type})...")
        
        # --- PIPELINE START ---
        
        # STEP 1: Rule-Based
        rule_risk = rule_based_detection(attack_type, content)
        
        # STEP 2: OpenAI Analysis
        openai_risk, openai_reason = analyze_with_openai(attack_type, content)
        
        # STEP 3: Gemini Analysis
        gemini_risk, gemini_reason = analyze_with_gemini(attack_type, content)
        
        # STEP 4: Final Decision (Highest Severity Wins)
        scores = {
            "Rule": calculate_severity_score(rule_risk),
            "OpenAI": calculate_severity_score(openai_risk),
            "Gemini": calculate_severity_score(gemini_risk)
        }
        max_score = max(scores.values())
        
        if max_score == 3:
            final_risk = "High"
        elif max_score == 2:
            final_risk = "Medium"
        else:
            final_risk = "Low"
            
        # Compile Explanation
        final_reason = f"Combined Analysis.\n[Rule]: {rule_risk}\n[OpenAI]: {openai_risk} ({openai_reason[:50]}...)\n[Gemini]: {gemini_risk} ({gemini_reason[:50]}...)"
        
        # Update DB
        cursor.execute('''
            UPDATE attacks 
            SET rule_risk = ?, openai_risk = ?, gemini_risk = ?, final_risk = ?, ai_reason = ?
            WHERE id = ?
        ''', (rule_risk, openai_risk, gemini_risk, final_risk, final_reason, attack_id))
        
        print(f"Finished Attack #{attack_id} -> Final Risk: {final_risk}")
        
    conn.commit()
    conn.close()
    print("Detection pipeline complete. Results saved.")

if __name__ == "__main__":
    run_detection_pipeline()
