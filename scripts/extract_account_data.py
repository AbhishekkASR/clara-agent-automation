import os
import json
import uuid

INPUT_DIR = "dataset/demo_calls"
OUTPUT_DIR = "outputs/accounts"

def create_empty_schema():

    return {
        "account_id": "",
        "company_name": "",
        "business_hours": {
            "days": "",
            "start": "",
            "end": "",
            "timezone": ""
        },
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": "",
        "non_emergency_routing_rules": "",
        "call_transfer_rules": {
            "timeout": "",
            "retries": ""
        },
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }


def extract_data(text):

    data = create_empty_schema()
    data["account_id"] = str(uuid.uuid4())[:8]

    lines = text.split("\n")

    for line in lines:

        if "Company name" in line:
            data["company_name"] = line.split(":")[1].strip()

        if "Business hours" in line:
            data["business_hours"]["days"] = "Mon-Fri"
            data["business_hours"]["start"] = "09:00"
            data["business_hours"]["end"] = "17:00"

        if "address" in line.lower():
            data["office_address"] = line.split(":")[1].strip()

        if "pipe" in line or "leak" in line or "heater" in line:
            data["services_supported"].append(line.strip())

        if "flood" in line or "burst" in line:
            data["emergency_definition"].append(line.strip())

    data["emergency_routing_rules"] = "Route to on-call technician"
    data["non_emergency_routing_rules"] = "Create service ticket"

    data["call_transfer_rules"]["timeout"] = 20
    data["call_transfer_rules"]["retries"] = 2

    data["after_hours_flow_summary"] = "Collect emergency details and transfer"
    data["office_hours_flow_summary"] = "Collect caller info and route to office"

    return data


for file in os.listdir(INPUT_DIR):

    path = os.path.join(INPUT_DIR, file)

    with open(path, "r") as f:
        text = f.read()

    data = extract_data(text)

    account_folder = os.path.join(OUTPUT_DIR, data["account_id"], "v1")

    os.makedirs(account_folder, exist_ok=True)

    with open(os.path.join(account_folder, "memo.json"), "w") as f:
        json.dump(data, f, indent=4)

    print("Processed:", file)