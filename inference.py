import os
from openai import OpenAI
import requests

BASE_URL = "http://127.0.0.1:8000"

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

actions = ["remove_duplicates", "fill_missing", "fix_format"]

print(f"[START] task=college-clean env=college-env model={MODEL_NAME}")

res = requests.post(f"{BASE_URL}/reset")
data = res.json()

total_rewards = []
steps = 0
done = False

for i, act in enumerate(actions):
    steps += 1

    res = requests.post(f"{BASE_URL}/step", json={"action_type": act})
    result = res.json()

    reward = float(result.get("reward", 0))
    done = result.get("done", False)

    total_rewards.append(f"{reward:.2f}")

    print(f"[STEP] step={steps} action={act} reward={reward:.2f} done={str(done).lower()} error=null")

    if done:
        break

score = float(result.get("info", {}).get("score", 0))
success = "true" if score > 0 else "false"

print(f"[END] success={success} steps={steps} score={score:.2f} rewards={','.join(total_rewards)}")