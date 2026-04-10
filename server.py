from fastapi import FastAPI
from env import CollegeDataEnv
from models import Action
from tasks import easy, medium, hard

app = FastAPI()
env = CollegeDataEnv()

@app.get("/")
def home():
    return {"message": "College Data Cleaning Environment Running....."}

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
                "name": "easy",
                "description": "Remove duplicate student records based on ID",
                "difficulty": "easy"
            },
            {
                "name": "medium",
                "description": "Fill missing marks in student records",
                "difficulty": "medium"
            },
            {
                "name": "hard",
                "description": "Fix inconsistent name formatting in student records",
                "difficulty": "hard"
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
        "task": task_name,
        "score": round(score, 2)
    }