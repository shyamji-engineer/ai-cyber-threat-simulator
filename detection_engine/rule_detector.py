import re

def rule_based_detection(attack_type, content):
    """
    Step 1: Rule-Based Detection
    Returns: 'High', 'Medium', 'Low'
    """
    
    # 1. Email Phishing Heuristics
    if attack_type == "Phishing Email":
        phishing_keywords = ["urgent", "password expired", "wire transfer", "risk", "immediate", "prize", "winner", "account suspended"]
        if any(keyword in content.lower() for keyword in phishing_keywords):
            return "High"
        return "Medium"
        
    # 2. Malicious URL Heuristics
    if attack_type == "Malicious URL":
        suspicious_tlds = [".tk", ".xyz", ".top", ".zip"]
        if any(content.endswith(tld) for tld in suspicious_tlds):
            return "High"
        if "update" in content or "login" in content or "secure" in content:
             # Often used in phishing URLs
             return "Medium"
        return "Low"

    # 3. Suspicious Script Heuristics
    if attack_type == "Suspicious Script":
        dangerous_patterns = ["<script>", "eval(", "base64_decode", "powershell", "curl ", "wget ", "chmod +x"]
        if any(pattern in content for pattern in dangerous_patterns):
            return "High"
        return "Medium"
        
    return "Low"
