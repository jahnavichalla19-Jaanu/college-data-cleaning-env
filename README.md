# College Data Cleaning OpenEnv Environment

##  Overview
This project simulates a real-world college data cleaning system where an AI agent learns to clean messy student records.

The environment follows the OpenEnv standard with step(), reset(), and state() APIs.

---

##  Problem Description
In real-world college systems, student data is often:
- Duplicated
- Incomplete (missing marks)
- Inconsistent (different name formats)

This environment helps train AI agents to automatically clean such data.

---

##  Environment Design

### Observation
Returns:
- Student dataset (list of records)
- Message describing current state

### Actions
The AI agent can perform:

1. `remove_duplicates`
2. `fill_missing`
3. `fix_format`

---

##  Tasks

###  Easy Task
Remove duplicate student entries based on ID.

###  Medium Task
Fill missing marks in student records.

###  Hard Task
Fix inconsistent name formatting.

---

##  Reward Function

- remove_duplicates → +0.4  
- fill_missing → +0.3  
- fix_format → +0.3  

Rewards are given based on progress toward clean data.

---

##  Scoring

Final score is calculated as:

(score_easy + score_medium + score_hard) / 3

Range: 0.0 to 1.0

---

##  How to Run Locally

Start server:

```bash
uvicorn server:app --reload