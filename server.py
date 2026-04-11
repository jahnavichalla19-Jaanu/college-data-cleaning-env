from fastapi import FastAPI
from env import CollegeDataEnv
from models import Action

app = FastAPI()

env = CollegeDataEnv()

@app.get("/")
def home():
    return {"message": "College Data Cleaning Environment Running 🚀"}

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
