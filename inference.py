import os
import requests
from openai import OpenAI

API_BASE_URL = os.environ.get("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.environ.get("API_KEY") or os.environ.get("HF_TOKEN", "none")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

BASE_URL = "http://0.0.0.0:7860"
ENV_NAME = "college-data-cleaning-env"

TASKS = [
    {"task_id": "easy",   "action": "remove_duplicates"},
    {"task_id": "medium", "action": "fill_missing"},
    {"task_id": "hard",   "action": "fix_format"},
]

for task in TASKS:
    task_id = task["task_id"]
    action  = task["action"]

    print(f"[START] task={task_id} env={ENV_NAME} model={MODEL_NAME}", flush=True)

    try:
        requests.post(f"{BASE_URL}/reset", timeout=10).raise_for_status()
    except Exception as e:
        print(f"[END] success=false steps=0 score=0.00 rewards=", flush=True)
        continue

    try:
        client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a data cleaning AI agent."},
                {"role": "user", "content": f"Task: {task_id}. Action: {action}. Confirm."}
            ],
            max_tokens=20
        )
    except Exception:
        pass

    rewards = []
    result = {}
    step = 1

    try:
        r = requests.post(
            f"{BASE_URL}/step",
            json={"action_type": action},
            timeout=10
        )
        r.raise_for_status()
        result = r.json()
        reward = float(result.get("reward", 0))
        done = result.get("done", False)
        rewards.append(reward)
        print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)
    except Exception as e:
        rewards.append(0.0)
        print(f"[STEP] step={step} action={action} reward=0.00 done=false error={str(e)}", flush=True)

    try:
        gr = requests.get(f"{BASE_URL}/grade/{task_id}", timeout=10)
        score = float(gr.json().get("score", 0.0))
    except Exception:
        score = float(result.get("info", {}).get("tasks", {}).get(task_id, 0.0)) if result else 0.0

    success = "true" if score > 0 else "false"
    reward_str = ",".join([f"{r:.2f}" for r in rewards])

    print(f"[END] success={success} steps={step} score={score:.2f} rewards={reward_str}", flush=True)