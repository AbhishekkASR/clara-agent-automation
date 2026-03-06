import os
import json

BASE_DIR = "outputs/accounts"

for account in os.listdir(BASE_DIR):

    memo_path = os.path.join(BASE_DIR, account, "v2", "memo.json")

    if not os.path.exists(memo_path):
        continue

    with open(memo_path) as f:
        memo = json.load(f)

    company = memo.get("company_name", "Unknown Company")

    # Handle business hours safely
    hours = memo.get("business_hours", {})

    if isinstance(hours, dict):
        business_hours = f"{hours.get('days','')} {hours.get('start','')} - {hours.get('end','')} {hours.get('timezone','')}"
    else:
        business_hours = hours

    # Services and emergencies
    emergencies = memo.get("emergency_definition", [])
    services = memo.get("services_supported", [])

    emergency_text = ", ".join(emergencies)
    services_text = ", ".join(services)

    agent = {
        "version": "v2",
        "source": "onboarding_update",
        "agent_name": f"{company} AI Receptionist",
        "voice_style": "professional",

        "system_prompt": f"""
You are the AI receptionist for {company}.

Your job is to answer inbound calls and help route customer requests correctly.

-------------------------
BUSINESS HOURS FLOW
-------------------------
1. Greet the caller professionally.
2. Ask the reason for their call.
3. Collect the caller's name and phone number.
4. Determine if the request is emergency or non-emergency.
5. Transfer the call to the appropriate technician or office staff.
6. If transfer fails, inform the caller that someone will call them back shortly.
7. Ask if the caller needs anything else.
8. Politely close the call.

-------------------------
AFTER HOURS FLOW
-------------------------
1. Greet the caller.
2. Ask the purpose of the call.
3. Confirm if the issue is an emergency.
4. If emergency:
   - collect caller name
   - phone number
   - service address
5. Attempt transfer to the on-call technician.
6. If transfer fails:
   - apologize
   - assure quick follow-up
7. If non-emergency:
   - collect details
   - confirm follow-up during business hours
8. Ask if anything else is needed.
9. Close the call politely.

-------------------------
COMPANY DETAILS
-------------------------
Business hours: {business_hours}

Emergency cases include:
{emergency_text}

Services supported:
{services_text}

Always remain polite, professional, and efficient.
"""
    }

    out = os.path.join(BASE_DIR, account, "v2", "agent_spec.json")

    with open(out, "w") as f:
        json.dump(agent, f, indent=4)

    print("Generated v2 agent spec for:", company)