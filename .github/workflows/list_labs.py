import os
import os.path
import json
import re


def parse_json(file_path):
    with open(file_path, "r") as f:
        index = json.load(f)
    direction = re.compile(r"\.\/[a-z]+").findall(filepath)
    if len(direction) > 0:
        lab_direction = direction[0].replace("./", "").title()
    else:
        lab_direction = "❌"
    lab_title = index.get("title", "❌")
    lab_type = index.get("type", "❌")
    lab_time = index.get("time", "❌")
    lab_difficulty = index.get("difficulty", "❌")
    lab_backend = index.get("backend").get("imageid", "❌")
    lab_steps = index.get("details").get("steps")
    lab_skills = []
    for step in lab_steps:
        skills = step.get("skills")
        if skills:
            lab_skills.extend(skills)
    data = {
        "<sub><sup>Title</sup></sub>": f"<sub><sup>{lab_title}</sup></sub>",
        "<sub><sup>Direction</sup></sub>": f"<sub><sup>{lab_direction}</sup></sub>",
        "<sub><sup>Type</sup></sub>": f"<sub><sup><code>{lab_type}</code></sup></sub>",
        "<sub><sup>Time</sup></sub>": f"<sub><sup>{lab_time}</sup></sub>",
        "<sub><sup>Difficulty</sup></sub>": f"<sub><sup><code>{lab_difficulty}</code></sup></sub>",
        "<sub><sup>Steps</sup></sub>": f"<sub><sup>{len(lab_steps)}</sup></sub>",
        "<sub><sup>Backend</sup></sub>": f"<sub><sup><code>{lab_backend}</code></sup></sub>",
        "<sub><sup>Skills</sup></sub>": f"<sub><sup>{len(set(lab_skills))}</sup></sub>",
    }
    return data, lab_time, len(lab_steps), len(set(lab_skills))


# Parse all index.json files
all_data = []
all_time = []
all_steps = []
all_skills = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f == "index.json"]:
        filepath = os.path.join(dirpath, filename)
        data, lab_time, lab_steps, lab_skills = parse_json(filepath)
        all_data.append(data)
        all_time.append(lab_time)
        all_steps.append(lab_steps)
        all_skills.append(lab_skills)

# Calculate sum time and steps
sum_time = sum([int(t) for t in all_time])
sum_steps = sum([int(s) for s in all_steps])
sum_labs = len(all_data)
sum_skills = sum(all_skills)
# Sort by direction
data_sorted = sorted(all_data, key=lambda d: d["<sub><sup>Title</sup></sub>"])
# Sort by direction
data_sorted = sorted(data_sorted, key=lambda d: d["<sub><sup>Direction</sup></sub>"])
# Add footer
footer = {
    "<sub><sup>Title</sup></sub>": f"<sub><sup><b>Sum</b></sup></sub>",
    "<sub><sup>Direction</sup></sub>": f"<sub><sup><b>{sum_labs}</b></sup></sub>",
    "<sub><sup>Type</sup></sub>": "",
    "<sub><sup>Time</sup></sub>": f"<sub><sup><b>{sum_time}</b></sup></sub>",
    "<sub><sup>Difficulty</sup></sub>": "",
    "<sub><sup>Steps</sup></sub>": f"<sub><sup><b>{sum_steps}</b></sup></sub>",
    "<sub><sup>Backend</sup></sub>": "",
    "<sub><sup>Skills</sup></sub>": f"<sub><sup><b>{sum_skills}</b></sup></sub>",
}
data_sorted.append(footer)

with open("labs.json", "w") as f:
    json.dump(data_sorted, f, indent=4)