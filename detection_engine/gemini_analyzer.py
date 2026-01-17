import os
import sys
import google.generativeai as genai

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import GOOGLE_API_KEY

def analyze_with_gemini(attack_type, content):
    """
    Step 3: Gemini Analysis (gemini-1.5-flash)
    Returns: ('High'/'Medium'/'Low', 'Explanation')
    """
    if not GOOGLE_API_KEY or "your_google_api_key" in GOOGLE_API_KEY:
        return "Pending", "API Key Missing"

    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
        Analyze this cyber threat snippet.
        Type: {attack_type}
        Content: "{content}"
        
        Output format:
        Risk: [High/Medium/Low]
        Reason: [Short explanation]
        """
        
        response = model.generate_content(prompt)
        text = response.text
        
        if "Risk: High" in text:
            risk = "High"
        elif "Risk: Medium" in text:
            risk = "Medium"
        elif "Risk: Low" in text:
            risk = "Low"
        else:
            risk = "Medium" # Default
            
        return risk, text.strip()
        
    except Exception as e:
        return "Error", str(e)
