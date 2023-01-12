import os
import os.path
import json


def parse_json(file, ix):
    with open(file, "r") as f:
        index = json.load(f)
    print(index)
    lab_title = index.get("title", "❌")
    lab_type = index.get("type", "❌")
    lab_time = index.get("time", "❌")
    lab_difficulty = index.get("difficulty", "❌")
    lab_steps = len(index.get("details").get("steps"))
    lab_backend = index.get("backend").get("imageid", "❌")
    data = {
        "<sup>Index</sup>": f"<sup>{ix}</sup>",
        "<sup>Title</sup>": f"<sup>{lab_title}</sup>",
        "<sup>Type</sup>": f"<sup><code>{lab_type}</code></sup>",
        "<sup>Time</sup>": f"<sup>{lab_time}</sup>",
        "<sup>Difficulty</sup>": f"<sup><code>{lab_difficulty}</code></sup>",
        "<sup>Steps</sup>": f"<sup>{lab_steps}</sup>",
        "<sup>Backend</sup>": f"<sup><code>{lab_backend}</code></sup>",
    }
    return data


all_data = []
i = 1
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f == "index.json"]:
        filepath = os.path.join(dirpath, filename)
        data = parse_json(filepath, i)
        all_data.append(data)
        i += 1

with open("labs.json", "w") as f:
    json.dump(all_data, f, indent=4)
