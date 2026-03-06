import os
import json

ONBOARDING_DIR = "dataset/onboarding_calls"
OUTPUT_DIR = "outputs/accounts"

def apply_updates(text, memo):

    lines = text.split("\n")
    changes = []

    for line in lines:

        if "Updated business hours" in line:
            old = memo["business_hours"]
            memo["business_hours"] = line.split(":")[1].strip()
            changes.append(f"Business hours changed from {old} to {memo['business_hours']}")

        if "sewer backup" in line:
            if "sewer backup" not in memo["emergency_definition"]:
                memo["emergency_definition"].append("sewer backup")
                changes.append("Added new emergency trigger: sewer backup")

        if "assistant manager" in line:
            memo["notes"] = "Fallback routing updated to assistant manager"
            changes.append("Updated fallback routing to assistant manager")

    return memo, changes


for account in os.listdir(OUTPUT_DIR):

    memo_path = os.path.join(OUTPUT_DIR, account, "v1", "memo.json")

    with open(memo_path) as f:
        memo = json.load(f)

    for file in os.listdir(ONBOARDING_DIR):

        with open(os.path.join(ONBOARDING_DIR, file)) as f:
            text = f.read()

        updated_memo, changes = apply_updates(text, memo)

        v2_folder = os.path.join(OUTPUT_DIR, account, "v2")
        os.makedirs(v2_folder, exist_ok=True)

        with open(os.path.join(v2_folder, "memo.json"), "w") as f:
            json.dump(updated_memo, f, indent=4)

        with open(os.path.join(OUTPUT_DIR, account, "changes.md"), "w") as f:
            for change in changes:
                f.write("- " + change + "\n")

        print("Updated account:", account)