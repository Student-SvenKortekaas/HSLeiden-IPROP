import re
from typing import List

from app.database import get_table_data, query_database


QUERY_GENRES = """
    SELECT DISTINCT genre_id, naam
    FROM genre_games JOIN genre
    ON genre_games.genre_id = genre.id
    WHERE game_id = ANY(%s)
    ORDER BY genre_id;
"""

QUERY_PUBLISHERS = """
    SELECT *
    FROM game;
"""


def print_games(cursor, games) -> None:
    games = get_table_data(cursor, "game")

    for game in games:
        print(f"{game[0]}\t{game[1]}")


def print_genres(cursor, games) -> None:
    result = query_database(cursor, QUERY_GENRES, (games,))
    
    for genre_id, genre_name in result:
        print(f"{genre_id}\t{genre_name}")


def print_publishers(cursor, games) -> None:
    publishers = query_database(cursor, "SELECT uitgever FROM game WHERE id = ANY(%s);", (games,))
    
    for i, publisher in enumerate(publishers):
        print(f"{i + 1}\t{publisher[0]}")


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