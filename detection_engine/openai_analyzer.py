import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import OPENAI_API_KEY
from openai import OpenAI

def analyze_with_openai(attack_type, content):
    """
    Step 2: OpenAI Analysis (gpt-4o-mini)
    Returns: ('High'/'Medium'/'Low', 'Explanation')
    """
    if not OPENAI_API_KEY or "your_openai_api_key" in OPENAI_API_KEY:
        return "Pending", "API Key Missing"

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        prompt = f"""
        You are a cybersecurity expert. Analyze the following potential threat.
        
        Type: {attack_type}
        Content: "{content}"
        
        Task:
        1. Determine the risk level (High, Medium, or Low).
        2. Provide a 1-sentence explanation.
        
        Format: Risk: [Level] | Reason: [Explanation]
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        
        result = response.choices[0].message.content.strip()
        
        # Parse result
        if "Risk: High" in result:
            risk = "High"
        elif "Risk: Medium" in result:
            risk = "Medium"
        elif "Risk: Low" in result:
            risk = "Low"
        else:
            risk = "Medium" # Default fallback
            
        return risk, result
        
    except Exception as e:
        return "Error", str(e)
