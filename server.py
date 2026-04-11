from fastapi import FastAPI
from env import CollegeDataEnv
from models import Action, GraderRequest
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
                "max_attempts": 5,
                "grader": "/grader",
                "grader_endpoint": "/grader",
                "score": easy(env.data)
            },
            {
                "id": "medium",
                "name": "medium",
                "description": "Fill missing marks in student records",
                "difficulty": "medium",
                "max_attempts": 5,
                "grader": "/grader",
                "grader_endpoint": "/grader",
                "score": medium(env.data)
            },
            {
                "id": "hard",
                "name": "hard",
                "description": "Fix inconsistent name formatting in student records",
                "difficulty": "hard",
                "max_attempts": 5,
                "grader": "/grader",
                "grader_endpoint": "/grader",
                "score": hard(env.data)
            }
        ]
    }

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "data": obs.data,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.post("/grader")
def grader(body: dict):
    task_id = body.get("task_id", "")
    graders = {
        "easy": easy,
        "medium": medium,
        "hard": hard
    }
    if task_id not in graders:
        return {"error": "task not found", "score": 0.2}
    score = graders[task_id](env.data)
    return {
        "task_id": task_id,
        "score": round(score, 3)
    }

@app.post("/grade/{task_name}")
def grade(task_name: str):
    graders = {
        "easy": easy,
        "medium": medium,
        "hard": hard
    }
    if task_name not in graders:
        return {"error": "task not found", "score": 0.2}
    score = graders[task_name](env.data)
    return {
        "task_id": task_name,
        "score": round(score, 3)
    }