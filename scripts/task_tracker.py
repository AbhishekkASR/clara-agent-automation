import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

scope = [
"https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
"config/google_credentials.json",
scope
)

client = gspread.authorize(creds)

sheet = client.open("Clara_Agent_Tracker").sheet1

existing_ids = sheet.col_values(1)

BASE_DIR = "outputs/accounts"

for account in os.listdir(BASE_DIR):

    memo_path = os.path.join(BASE_DIR, account, "v1", "memo.json")

    with open(memo_path) as f:
        memo = json.load(f)

    account_id = memo["account_id"]

    # Skip if already exists
    if account_id in existing_ids:
        print("Skipping duplicate:", memo["company_name"])
        continue

    sheet.append_row([
        memo["account_id"],
        memo["company_name"],
        "Agent Created",
        "v1"
    ])

    print("Added to tracker:", memo["company_name"])