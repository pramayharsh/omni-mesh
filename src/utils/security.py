import re

class SecurityScanner:
    def __init__(self):
        # Patterns for PII and Secrets
        self.patterns = {
            "EMAIL": r'[\w\.-]+@[\w\.-]+\.\w+',
            "API_KEY": r'(sk-[a-zA-Z0-9]{32,}|hf_[a-zA-Z0-9]{32,})',
            "PHONE": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            "CREDIT_CARD": r'\b(?:\d[ -]*?){13,16}\b'
        }

    def scan_text(self, text: str):
        findings = []
        for label, pattern in self.patterns.items():
            if re.search(pattern, text):
                findings.append(label)
        return findings