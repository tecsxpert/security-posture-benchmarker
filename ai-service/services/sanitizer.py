import bleach

def sanitize_input(text):
    # Remove HTML tags
    clean_text = bleach.clean(text, tags=[], strip=True)

    # Detect prompt injection patterns
    blocked_patterns = [
        "ignore previous instructions",
        "act as",
        "system prompt",
        "jailbreak",
        "bypass"
    ]

    for pattern in blocked_patterns:
        if pattern.lower() in clean_text.lower():
            return None

    return clean_text