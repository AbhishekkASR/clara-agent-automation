import os
import json

BASE_DIR = "outputs/accounts"

for account in os.listdir(BASE_DIR):

    memo_path = os.path.join(BASE_DIR, account, "v1", "memo.json")

    if not os.path.exists(memo_path):
        continue

    with open(memo_path) as f:
        memo = json.load(f)

    company = memo.get("company_name", "Unknown Company")

    emergencies = memo.get("emergency_definition", [])
    services = memo.get("services_supported", [])

    emergency_text = ", ".join(emergencies)
    services_text = ", ".join(services)

    agent = {
        "version": "v1",
        "source": "demo_call",
        "agent_name": f"{company} AI Receptionist",
        "voice_style": "professional",

        "system_prompt": f"""
You are the AI receptionist for {company}.

This configuration was generated from an initial demo call.

Your job is to answer calls and collect caller information.

Collect:
- caller name
- phone number
- service request

Services supported:
{services_text}

Emergency cases include:
{emergency_text}

Always remain polite and professional.
"""
    }

    out = os.path.join(BASE_DIR, account, "v1", "agent_spec.json")

    with open(out, "w") as f:
        json.dump(agent, f, indent=4)

    print("Generated v1 agent spec for:", company)