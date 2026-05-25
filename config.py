import os

# Candidate Information
# Can be overridden by environment variables or default to the provided John Doe info
CANDIDATE_NAME = os.getenv("CANDIDATE_NAME", "John Doe")
CANDIDATE_REG_NO = os.getenv("CANDIDATE_REG_NO", "REG12347")
CANDIDATE_EMAIL = os.getenv("CANDIDATE_EMAIL", "john@example.com")

# Endpoints
GENERATE_WEBHOOK_URL = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
SUBMIT_WEBHOOK_URL_FALLBACK = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
