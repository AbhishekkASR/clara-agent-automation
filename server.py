from flask import Flask, jsonify, send_from_directory
import os
import json
import subprocess

app = Flask(__name__, static_folder="frontend")

BASE_DIR = "outputs/accounts"


@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")


@app.route("/accounts")
def get_accounts():

    accounts = []
    seen = set()

    if not os.path.exists(BASE_DIR):
        return jsonify(accounts)

    for account in os.listdir(BASE_DIR):

        memo_path = os.path.join(BASE_DIR, account, "v2", "memo.json")

        if not os.path.exists(memo_path):
            continue

        with open(memo_path) as f:
            memo = json.load(f)

        company = memo.get("company_name")

        if company in seen:
            continue

        seen.add(company)

        accounts.append({
            "company": company,
            "services": memo.get("services_supported", []),
            "emergencies": memo.get("emergency_definition", [])
        })

    return jsonify(accounts)


import subprocess

@app.route("/run-pipeline", methods=["POST"])
def run_pipeline():

    try:

        result = subprocess.run(
            ["python", "run_pipeline.py"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return jsonify({
                "status": "error",
                "message": result.stderr
            }), 500

        return jsonify({
            "status": "success",
            "message": result.stdout
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)