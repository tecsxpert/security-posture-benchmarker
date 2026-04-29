from services.groq_client import call_groq

if __name__ == "__main__":
    response = call_groq("Give 2 cybersecurity tips")
    print("\nAI RESPONSE:\n")
    print(response)