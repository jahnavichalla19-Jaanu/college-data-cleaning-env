from fastapi import FastAPI, Request
from env import CollegeDataEnv
from models import Action
from tasks import easy, medium, hard

app = FastAPI()
env = CollegeDataEnv()

@app.get("/")
def home():
    return {"message": "College Data Cleaning Environment Running 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "college-data-cleaning-env"}

@app.get("/state")
def state():
    return {
        "episode_id": "episode-001",
        "step_count": env.step_count,
        "data": env.data,
        "done": env.done
    }

@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {
                "id": "easy",
                "name": "easy",
                "description": "Remove duplicate student records based on ID",
                "difficulty": "easy",
                "grader": "easy",
                "grader_endpoint": "/grade/easy",
                "score": easy(env.data)
            },
            {
                "id": "medium",
                "name": "medium",
                "description": "Fill missing marks in student records",
                "difficulty": "medium",
                "grader": "medium",
                "grader_endpoint": "/grade/medium",
                "score": medium(env.data)
            },
            {
                "id": "hard",
                "name": "hard",
                "description": "Fix inconsistent name formatting",
                "difficulty": "hard",
                "grader": "hard",
                "grader_endpoint": "/grade/hard",
                "score": hard(env.data)
            }
        ]
    }

@app.post("/reset")
async def reset(request: Request):
    try:
        body = await request.json()
        task_id = body.get("task_id", "easy")
        episode_id = body.get("episode_id", "episode-001")
    except Exception:
        task_id = "easy"
        episode_id = "episode-001"
    
    obs = env.reset()
    return {
        "observation": {
            "data": obs.data,
            "message": obs.message,
            "task_id": task_id
        },
        "reward": None,
        "done": False,
        "episode_id": episode_id
    }

@app.post("/step")
async def step(request: Request):
    try:
        body = await request.json()
        action_type = body.get("action_type", body.get("action", {}).get("action_type", ""))
    except Exception:
        action_type = ""

    action = Action(action_type=action_type)
    obs, reward, done, info = env.step(action)
    return {
        "observation": {
            "data": obs.data,
            "message": obs.message
        },
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/grade/easy")
def grade_easy():
    return {"task_id": "easy", "score": easy(env.data)}

@app.get("/grade/medium")
def grade_medium():
    return {"task_id": "medium", "score": medium(env.data)}

@app.get("/grade/hard")
def grade_hard():
    return {"task_id": "hard", "score": hard(env.data)}

@app.post("/grade/easy")
def grade_easy_post():
    return {"task_id": "easy", "score": easy(env.data)}

@app.post("/grade/medium")
def grade_medium_post():
    return {"task_id": "medium", "score": medium(env.data)}

@app.post("/grade/hard")
def grade_hard_post():
    return {"task_id": "hard", "score": hard(env.data)}

@app.api_route("/grade/{task_name}", methods=["GET", "POST"])
def grade(task_name: str):
    graders = {"easy": easy, "medium": medium, "hard": hard}
    if task_name not in graders:
        return {"error": "task not found", "score": 0.1}
    return {"task_id": task_name, "score": graders[task_name](env.data)}

@app.post("/grader")
async def grader(request: Request):
    try:
        body = await request.json()
        task_id = body.get("task_id", "")
    except Exception:
        task_id = ""
    graders = {"easy": easy, "medium": medium, "hard": hard}
    if task_id not in graders:
        return {"error": "task not found", "score": 0.1}
    return {"task_id": task_id, "score": graders[task_id](env.data)}