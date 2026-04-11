from fastapi import FastAPI
from env import CollegeDataEnv
from models import Action

app = FastAPI()

env = CollegeDataEnv()

@app.get("/")
def root():
    return {"message": "Running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "data": obs.data,
        "message": obs.message,
        "reward": reward,
        "done": done,
        "info": info
    }

def main():
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)
