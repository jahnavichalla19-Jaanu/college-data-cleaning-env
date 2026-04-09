from fastapi import FastAPI
from env import CollegeDataEnv
from models import Action

app = FastAPI()
env = CollegeDataEnv()

@app.get("/")
def home():
    return {"message": "College Data Cleaning Environment Running 🚀"}

@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {
                "name": "easy",
                "description": "Remove duplicate student records based on ID",
                "grader": "easy",
                "reward_threshold": 0.5
            },
            {
                "name": "medium",
                "description": "Fill missing marks in student records",
                "grader": "medium",
                "reward_threshold": 0.5
            },
            {
                "name": "hard",
                "description": "Fix inconsistent name formatting in student records",
                "grader": "hard",
                "reward_threshold": 0.5
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