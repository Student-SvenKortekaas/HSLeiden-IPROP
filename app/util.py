import re
from typing import List

from app.database import get_table_data


def format_input(input: str) -> List[int]:
    # Extract the digits from the input
    input_ = re.findall(r"\d+", input)
    input_ = [int(s) for s in input_]

    return input_


def validate_input(cursor, input: str) -> bool:
    games = get_table_data(cursor, table="game")

    if not (min(input) <= len(games) <= max(input)):
        return False

    return True