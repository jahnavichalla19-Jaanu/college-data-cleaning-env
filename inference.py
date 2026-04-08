import os
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")
HF_TOKEN = os.getenv("HF_TOKEN", "none")

TASK_NAME = "college-cleaning"
ENV_NAME = "college-data-env"

actions = ["remove_duplicates", "fill_missing", "fix_format"]

# START LOG
print(f"[START] task={TASK_NAME} env={ENV_NAME} model={MODEL_NAME}")

# RESET
res = requests.post(f"{BASE_URL}/reset")
data = res.json()

total_rewards = []
step_count = 0

for act in actions:
    step_count += 1

    try:
        res = requests.post(f"{BASE_URL}/step", json={"action_type": act})
        result = res.json()

        reward = float(result.get("reward", 0))
        done = result.get("done", False)

        total_rewards.append(reward)

        print(f"[STEP] step={step_count} action={act} reward={reward:.2f} done={str(done).lower()} error=null")

        if done:
            break

    except Exception as e:
        print(f"[STEP] step={step_count} action={act} reward=0.00 done=false error={str(e)}")

# FINAL SCORE
score = result.get("info", {}).get("score", 0)

success = "true" if score > 0 else "false"

reward_str = ",".join([f"{r:.2f}" for r in total_rewards])

print(f"[END] success={success} steps={step_count} score={score:.2f} rewards={reward_str}")