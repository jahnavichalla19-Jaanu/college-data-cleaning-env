from models import Observation, Action
from tasks import easy, medium, hard
import copy

class CollegeDataEnv:

    def __init__(self):
        self.original_data = [
            {"id": "101", "name": "jahnavi", "marks": None},
            {"id": "101", "name": "JAHNAVI", "marks": 90},
            {"id": "102", "name": "Ravi", "marks": None}
        ]
        self.data = []
        self.done = False
        self.step_count = 0

    def reset(self):
        self.data = copy.deepcopy(self.original_data)
        self.done = False
        self.step_count = 0
        return Observation(data=self.data, message="Reset done. Clean the data.")

   def step(self, action: Action):
    reward = 0.0

    if action.action_type == "remove_duplicates":
        seen = set()
        new_data = []
        for d in self.data:
            if d["id"] not in seen:
                seen.add(d["id"])
                new_data.append(d)
        self.data = new_data
        reward += 0.4

    elif action.action_type == "fill_missing":
        for d in self.data:
            if d["marks"] is None:
                d["marks"] = 0
                reward += 0.3

    elif action.action_type == "fix_format":
        for d in self.data:
            d["name"] = d["name"].capitalize()
        reward += 0.3

    if all(d["marks"] is not None for d in self.data):
        self.done = True

    score_easy = easy(self.data)
    score_medium = medium(self.data)
    score_hard = hard(self.data)

    final_score = (score_easy + score_medium + score_hard) / 3

    return Observation(
        data=self.data,
        message="Step done"
    ), reward, self.done, {
        "score": final_score,
        "tasks": {
            "easy": score_easy,
            "medium": score_medium,
            "hard": score_hard
        }
    }