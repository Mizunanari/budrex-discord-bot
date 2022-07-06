import json
from typing import Any, List

import pokebase as pb
from tqdm import tqdm

arlm = pb.APIResourceList("move")

move: List[dict[str, Any]] = []
name = iter(arlm.names)


while True:
    temp: dict[str, Any] = {}
    try:
        temp["name"] = next(name)
    except StopIteration:
        break
    move.append(temp)


for item in tqdm(move):
    res = pb.move(id_or_name=item.get("name", ""))

    item["jp_name"] = res.names[0].name
    item["damage_class"] = res.damage_class.name
    item["priority"] = res.priority


with open("res.json", "w") as f:
    f.write(json.dumps(move))
