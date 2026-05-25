import sys
import requests
import json
import config
from sql_solutions import SQL_QUESTION_1, SQL_QUESTION_2

def run_pipeline():
    print("=" * 60)
    print("       BAJAJ FINSERV HEALTH | QUALIFIER 1 | PYTHON")
    print("=" * 60)
    
    # 1. Prepare candidate data payload
    payload = {
        "name": config.CANDIDATE_NAME,
        "regNo": config.CANDIDATE_REG_NO,
        "email": config.CANDIDATE_EMAIL
    }
    
    print("\n[Step 1/4] Preparing candidate details for webhook generation:")
    print(json.dumps(payload, indent=2))
    
    # 2. On app startup, send POST request to generate webhook
    print(f"\n[Step 2/4] Sending POST request to {config.GENERATE_WEBHOOK_URL}...")
    try:
        response = requests.post(
            config.GENERATE_WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[-] Webhook generation request failed: {e}")
        if response is not None:
            print(f"Response Content: {response.text}")
        sys.exit(1)
        
    res_data = response.json()
    webhook_url = res_data.get("webhook")
    access_token = res_data.get("accessToken")
    
    if not webhook_url or not access_token:
        print("[-] Error: Response did not contain 'webhook' or 'accessToken'.")
        print(f"Response: {res_data}")
        sys.exit(1)
        
    print("[+] Successfully received Webhook URL and Access Token!")
    print(f"    - Webhook URL: {webhook_url}")
    print(f"    - Access Token: {access_token[:20]}...{access_token[-20:]}")
    
    # 3. Determine assigned question based on last digit of registration number
    reg_no = config.CANDIDATE_REG_NO
    print(f"\n[Step 3/4] Determining assigned question based on registration number '{reg_no}':")
    
    # Extract the last digit of the registration number
    # If the last character is not a digit, scan backwards to find the last digit
    last_digit = None
    for char in reversed(reg_no):
        if char.isdigit():
            last_digit = int(char)
            break
            
    if last_digit is None:
        print("[-] Warning: No digit found in registration number. Defaulting to ODD (Question 1).")
        is_odd = True
    else:
        is_odd = (last_digit % 2 != 0)
        print(f"    - Last digit of registration number: {last_digit}")
        print(f"    - Parity: {'Odd (Question 1)' if is_odd else 'Even (Question 2)'}")
        
    # Select query based on parity
    if is_odd:
        assigned_query = SQL_QUESTION_1
        print("    - Assigned Question: [Question 1] (Odd)")
    else:
        assigned_query = SQL_QUESTION_2
        print("    - Assigned Question: [Question 2] (Even)")
        
    print("\nSelected SQL Query:")
    print("-" * 50)
    print(assigned_query)
    print("-" * 50)
    
    # 4. Submit solution (the final SQL query) to the returned webhook URL using the accessToken
    print(f"\n[Step 4/4] Submitting solution to webhook URL: {webhook_url}...")
    submit_headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    submit_payload = {
        "finalQuery": assigned_query
    }
    
    try:
        submit_response = requests.post(
            webhook_url,
            json=submit_payload,
            headers=submit_headers
        )
        submit_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[-] Webhook submission failed: {e}")
        if submit_response is not None:
            print(f"Response Content: {submit_response.text}")
        sys.exit(1)
        
    print("\n" + "=" * 60)
    print("                   SUBMISSION SUCCESSFUL")
    print("=" * 60)
    print(f"Status Code: {submit_response.status_code}")
    print("Response Body:")
    print(json.dumps(submit_response.json(), indent=2))
    print("=" * 60)

if __name__ == "__main__":
    run_pipeline()
