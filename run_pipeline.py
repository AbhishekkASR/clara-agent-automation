import os

print("Starting Clara Automation Pipeline...")

os.system("python scripts/extract_account_data.py")
os.system("python scripts/generate_agent_spec.py")
os.system("python scripts/apply_updates.py")
os.system("python scripts/generate_agent_spec_v2.py")
os.system("python scripts/task_tracker.py")

print("Pipeline completed successfully.")