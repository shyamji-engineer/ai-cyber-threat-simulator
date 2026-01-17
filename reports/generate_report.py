import sqlite3
import sys
import os
import pandas as pd

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATABASE_PATH

def generate_report():
    """Generates a markdown report of the simulation/detection results."""
    print("Generating executive report...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    
    # Load data
    df = pd.read_sql_query("SELECT * FROM attacks", conn)
    conn.close()
    
    if df.empty:
        print("No data found to report.")
        return

    # Statistics
    total_attacks = len(df)
    high_risk = len(df[df['final_risk'] == 'High'])
    medium_risk = len(df[df['final_risk'] == 'Medium'])
    low_risk = len(df[df['final_risk'] == 'Low'])
    
    # Manual markdown formatting for Attack Distribution
    attack_counts = df['attack_type'].value_counts()
    attack_types_md = "| Attack Type | Count |\n|---|---|\n"
    for at, count in attack_counts.items():
        attack_types_md += f"| {at} | {count} |\n"
    
    # Identify critical threats
    critical_df = df[df['final_risk'] == 'High'][['id', 'attack_type', 'content', 'rule_risk', 'openai_risk', 'gemini_risk']].head(5)
    
    if not critical_df.empty:
        critical_threats_md = "| ID | Type | Content | Rule | OpenAI | Gemini |\n|---|---|---|---|---|---|\n"
        for _, row in critical_df.iterrows():
            content_snippet = row['content'][:20].replace('|', '') + "..."
            critical_threats_md += f"| {row['id']} | {row['attack_type']} | {content_snippet} | {row['rule_risk']} | {row['openai_risk']} | {row['gemini_risk']} |\n"
    else:
        critical_threats_md = "No high risk threats detected."
    
    report_content = f"""# AI-Powered Cyber Threat Detection Report
**Date:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

## Executive Summary
This report summarizes the findings from the AI-powered cyber threat simulation.

- **Total Attacks Analyzed:** {total_attacks}
- **High Risk Threats:** {high_risk} ({high_risk/total_attacks*100:.1f}%)
- **Medium Risk Threats:** {medium_risk}
- **Low Risk Threats:** {low_risk}

## Attack Distribution
{attack_types_md}

## Top Critical Threats (High Risk)
The following are the top detected high-risk threats requiring immediate attention:

{critical_threats_md}

## Methodology
The system utilizes a multi-layered detection pipeline:
1. **Rule-Based Engine**: Heuristic analysis.
2. **OpenAI GPT-4o-mini**: Contextual semantic analysis.
3. **Google Gemini 1.5 Flash**: Independent verification.
4. **Final Decision Engine**: Aggregates scores and applies highest-severity logic.

---
*Generated automatically by AI-Cyber-Threat-Simulator*
"""
    
    # Save Report
    output_path = os.path.join("reports", "executive_summary.md")
    with open(output_path, "w") as f:
        f.write(report_content)
        
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    generate_report()
