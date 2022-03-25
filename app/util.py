import re
from typing import List

from app.constants import QUERY_GENRES
from app.database import query_database


def print_games(cursor, games) -> None:
    games = query_database(cursor, "SELECT * FROM game ORDER BY id")

    for game in games:
        print(f"{game[0]}\t{game[1]}")


def print_genres(cursor, games) -> None:
    genres = query_database(cursor, QUERY_GENRES, (games,))
    
    for i, genre in enumerate(genres):
        print(f"{i + 1}\t{genre[1]}")


def print_publishers(cursor, games) -> None:
    publishers = query_database(cursor, "SELECT DISTINCT uitgever FROM game WHERE id = ANY(%s);", (games,))
    
    for i, publisher in enumerate(publishers):
        print(f"{i + 1}\t{publisher[0]}")


def print_dimensions(cursor, games) -> None:
    dimensions = query_database(cursor, "SELECT DISTINCT dimensie FROM game WHERE id = ANY(%s);", (games,))

    for i, dimension in enumerate(dimensions):
        print(f"{i + 1}\t{dimension[0]}")


def print_player_types(cursor, games) -> None:
    single_player = query_database(cursor, "SELECT id FROM game WHERE is_singleplayer = true AND id = ANY(%s);", (games,))
    multi_player = query_database(cursor, "SELECT id FROM game WHERE is_multiplayer = true AND id = ANY(%s);", (games,))

    if single_player:
        print("1\tSingle Player")

    if multi_player:
        print("2\tMulti Player")


def format_input(input: str) -> List[int]:
    # Extract the digits from the input
    input_ = re.findall(r"\d+", input)
    input_ = [int(s) for s in input_]

    return input_
