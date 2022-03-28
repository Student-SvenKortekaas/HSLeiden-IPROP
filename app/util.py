import re
from typing import List

from app.constants import QUERY_DIMENSIONS, QUERY_GENRES, QUERY_PLAYER_TYPE_MULTI_PLAYER, QUERY_PLAYER_TYPE_SINGLE_PLAYER, QUERY_PUBLISHERS
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
    publishers = query_database(cursor, QUERY_PUBLISHERS, (games,))
    
    for i, publisher in enumerate(publishers):
        print(f"{i + 1}\t{publisher[0]}")


def print_dimensions(cursor, games) -> None:
    dimensions = query_database(cursor, QUERY_DIMENSIONS, (games,))

    for i, dimension in enumerate(dimensions):
        print(f"{i + 1}\t{dimension[0]}")


def print_player_types(cursor, games) -> None:
    single_player = query_database(cursor, QUERY_PLAYER_TYPE_SINGLE_PLAYER, (games,))
    multi_player = query_database(cursor, QUERY_PLAYER_TYPE_MULTI_PLAYER, (games,))

    print(multi_player)

    if single_player:
        print("1\tSingle Player")

    if multi_player:
        print("2\tMulti Player")


def format_input(input: str) -> List[int]:
    # Extract the digits from the input
    input_ = re.findall(r"\d+", input)
    input_ = [int(s) for s in input_]

    return input_
