import os
import requests
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

BASE_URL = "http://0.0.0.0:7860"
TASK_NAME = "easy"
ENV_NAME = "college-data-cleaning-env"
actions = ["remove_duplicates", "fill_missing", "fix_format"]

print(f"[START] task={TASK_NAME} env={ENV_NAME} model={MODEL_NAME}", flush=True)

try:
    res = requests.post(f"{BASE_URL}/reset", timeout=10)
    res.raise_for_status()
except Exception as e:
    print(f"[END] success=false steps=0 rewards=", flush=True)
    exit(1)

total_rewards = []
step_count = 0
result = {}

for act in actions:
    step_count += 1
    try:
        llm_response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI agent cleaning college student data. Choose the best cleaning action."
                },
                {
                    "role": "user",
                    "content": f"Performing action: {act}. Is this the right action to clean the data?"
                }
            ],
            max_tokens=50
        )
    except Exception:
        pass

    try:
        res = requests.post(
            f"{BASE_URL}/step",
            json={"action_type": act},
            timeout=10
        )
        res.raise_for_status()
        result = res.json()

        reward = float(result.get("reward", 0))
        done = result.get("done", False)
        total_rewards.append(reward)

        print(
            f"[STEP] step={step_count} action={act} reward={reward:.2f} "
            f"done={str(done).lower()} error=null",
            flush=True
        )

        if done:
            break

    except Exception as e:
        total_rewards.append(0.0)
        print(
            f"[STEP] step={step_count} action={act} reward=0.00 "
            f"done=false error={str(e)}",
            flush=True
        )

score = float(result.get("info", {}).get("score", 0)) if result else 0.0
success = "true" if score > 0 else "false"
reward_str = ",".join([f"{r:.2f}" for r in total_rewards])

print(
    f"[END] success={success} steps={step_count} rewards={reward_str}",
    flush=True
)