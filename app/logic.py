from typing import List

from app.constants import QUERY_DIMENSIONS, QUERY_GENRES, QUERY_PLAYER_TYPE_ALL, QUERY_PLAYER_TYPE_MULTI_PLAYER, QUERY_PLAYER_TYPE_SINGLE_PLAYER, QUERY_PUBLISHERS
from app.database import get_table_data, query_database


def filter_genres(cursor, games: List[int], genres: List[int]) -> List[int]:
    """
    Limit the list of games to only the games with a genre chosen by the user..
    """

    games_ = []
    genres_ = query_database(cursor, QUERY_GENRES, (games,))

    for game in get_table_data(cursor, table="game"):
        for genre in genres_:
            if game[0] in games and (genres_.index(genre) + 1) in genres:
                games_.append(game[0])

    return list(set(games_))


def filter_publishers(cursor, games: List[int], publishers: List[int]) -> List[int]:
    """
    Limit the list of games to the games with the publishers chosen by the user.
    """

    games_ = []

    publishers_ = query_database(cursor, QUERY_PUBLISHERS, (games,))

    for game in get_table_data(cursor, table="game"):
        for publisher in publishers_:
            if game[0] in games and game[3] == publisher[0] and (publishers_.index(publisher) + 1) in publishers:
                games_.append(game[0])

    return games_


def filter_dimensions(cursor, games: List[int], dimensions: List[int]) -> List[int]:
    """
    Limit the list of games to the games with the dimensions chosen by the user.
    """

    games_ = []

    dimensions_ = query_database(cursor, QUERY_DIMENSIONS, (games,))

    for game in get_table_data(cursor, table="game"):
        for dimension in dimensions_:
            if game[0] in games and game[7] == dimension[0] and (dimensions_.index(dimension) + 1) in dimensions:
                games_.append(game[0])

    return games_


def filter_player_types(cursor, games: List[int], player_types: List[int]) -> List[int]:
    """
    Limit the list of games to the games with the player types chosen by the user.
    """

    games_ = []

    if len(player_types) == 2:
        if player_types[0] == 1 and player_types[1] == 2 or player_types[0] == 2 and player_types[1] == 1:
            for game_id in query_database(cursor, QUERY_PLAYER_TYPE_ALL, (games,)):
                games_.append(game_id[0])

    elif len(player_types) == 1:
        if player_types[0] == 1:
            for game_id in query_database(cursor, QUERY_PLAYER_TYPE_SINGLE_PLAYER, (games,)):
                games_.append(game_id[0])

        if player_types[0] == 2:
            for game_id in query_database(cursor, QUERY_PLAYER_TYPE_MULTI_PLAYER, (games,)):
                games_.append(game_id[0])

    return games_
