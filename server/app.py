import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
    return env.reset()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "data": obs.data,
        "reward": reward,
        "done": done,
        "info": info
    }

def main():
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
