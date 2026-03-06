# Clara AI Agent Automation Dashboard

## Overview

This project implements an automated pipeline for generating and updating AI voice agents based on customer service call transcripts. The system simulates how an operations team could onboard new service businesses, extract structured information from conversations, generate agent configurations, and update them after onboarding changes.

The pipeline processes demo call transcripts, extracts key information about service businesses, generates an initial AI agent draft (v1), applies onboarding updates, and produces a refined agent specification (v2).

A web dashboard built with Flask displays the generated agents and allows users to trigger the pipeline directly from the interface.

---

## Problem Statement

Customer service businesses such as plumbing, electrical repair, and HVAC services often rely on phone-based interactions with customers. Deploying AI receptionists requires structured agent configurations that define:

* supported services
* emergency handling logic
* call routing rules
* conversational behavior

Manually creating and updating these configurations for each client is time-consuming. This project demonstrates an automation workflow that converts call transcripts into structured AI agent specifications.

---

## System Architecture

The system follows a multi-step automation pipeline:

```
Demo Call Transcripts
        ↓
Account Information Extraction
        ↓
Account Memo JSON Generation
        ↓
Agent Draft Generation (v1)
        ↓
Onboarding Update Processing
        ↓
Agent Specification Update (v2)
        ↓
Tracking and Visualization
```

---

## Key Features

### Automated Transcript Processing

Processes demo call transcripts and extracts:

* company name
* services offered
* emergency cases
* business hours

### Structured Account Memo Generation

Creates structured JSON files containing business details.

Example:

```json
{
  "company_name": "Sharma Plumbing Services",
  "services_supported": [
    "pipe repair",
    "water leakage repair"
  ],
  "emergency_definition": [
    "burst water pipe",
    "sewer backup"
  ]
}
```

### Agent Draft Generation (v1)

Automatically generates the first version of an AI receptionist agent specification based on the extracted information.

### Onboarding Update Processing

Simulates onboarding updates where additional details about the business are added or corrected.

### Agent Specification Update (v2)

Creates an improved agent configuration including:

* refined system prompt
* improved routing logic
* updated emergency definitions
* enhanced call handling flow

### Automation Dashboard

A Flask-based dashboard provides:

* list of generated AI agents
* pipeline execution control
* system statistics
* visualization of the automation workflow

---

## Project Structure

```
clara-agent-automation
│
├── dataset
│   └── demo_calls
│       ├── demo1.txt
│       ├── demo2.txt
│       ├── demo3.txt
│       ├── demo4.txt
│       └── demo5.txt
│
├── scripts
│   ├── extract_account_info.py
│   ├── generate_agent_spec.py
│   ├── apply_onboarding_updates.py
│   └── task_tracker.py
│
├── outputs
│   └── accounts
│       └── <account_id>
│           ├── v1
│           └── v2
│
├── frontend
│   └── index.html
│
├── server.py
├── run_pipeline.py
└── README.md
```

---

## Automation Pipeline

The pipeline orchestrates the following steps:

### 1. Extract Account Information

Reads demo call transcripts and extracts business information.

### 2. Generate Account Memo

Creates a structured JSON memo for each business.

### 3. Generate Agent Draft (v1)

Creates an initial AI receptionist configuration.

### 4. Apply Onboarding Updates

Simulates additional information provided during onboarding.

### 5. Generate Agent Draft (v2)

Produces the final agent configuration with improved routing logic.

### 6. Track Updates

Records agent generation updates in a tracking system.

---

## Running the Project Locally

### 1. Clone the repository

```
git clone https://github.com/AbhishekkASR/clara-agent-automation.git
cd clara-agent-automation
```

### 2. Install dependencies

```
pip install flask flask-cors gspread oauth2client
```

### 3. Run the server

```
python server.py
```

### 4. Open the dashboard

```
http://127.0.0.1:5000
```

---

## Running the Automation Pipeline

The pipeline can be triggered either from the dashboard or manually.

### From terminal

```
python run_pipeline.py
```

### From dashboard

Click the **Run Pipeline** button to execute the automation process.

---

## Example Generated Agent

Example AI receptionist configuration:

```
Agent Name: Sharma Plumbing Services AI Receptionist

Business Hours Flow:
1. Greet the caller professionally
2. Ask the reason for the call
3. Collect caller name and phone number
4. Determine if the request is an emergency
5. Transfer the call if necessary
6. Provide follow-up instructions
7. Close the call politely
```

---

## Technologies Used

Python
Flask
HTML / CSS / JavaScript
JSON Data Processing
Automation Scripts

---

## Future Improvements

Potential enhancements include:

* integration with real speech-to-text systems
* automatic intent detection
* improved agent version comparison
* deployment of the dashboard as a public web service
* integration with production voice platforms

---

## Author

Abhishek Singh
B.Tech Computer & Communication Engineering
Manipal University Jaipur

GitHub:
https://github.com/AbhishekkASR
