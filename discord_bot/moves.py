import json
import re
from typing import Any, List

with open("res.json", "r") as f:
    moves: List[dict[str, Any]] = json.load(f)


def get_moves(message: str):

    global moves

    for move in moves:
        jname: str = move.get("jp_name", "")
        if re.match(jname, message):
            category: str = move.get("damage_class", "")
            priority: int = move.get("priority", 0)
            return (
                True,
                {"jp_name": jname, "damage_class": category, "priority": priority},
            )

    return (False, {})


def isMoveSuccess(priority, damage_class) -> bool:

    if priority >= 2:
        return False

    if not damage_class == "status":
        return False

    return True
