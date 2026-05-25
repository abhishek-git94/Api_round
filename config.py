import os

# Candidate Information
CANDIDATE_NAME = os.getenv("CANDIDATE_NAME", "Abhishek Pal")
CANDIDATE_REG_NO = os.getenv("CANDIDATE_REG_NO", "0827AL231009")
CANDIDATE_EMAIL = os.getenv("CANDIDATE_EMAIL", "ap036291@gmail.com")

# Endpoints
GENERATE_WEBHOOK_URL = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
SUBMIT_WEBHOOK_URL_FALLBACK = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
