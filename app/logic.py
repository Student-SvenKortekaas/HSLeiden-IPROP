from typing import List

from app.constants import QUERY_GENRES
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

    publishers_ = query_database(cursor, "SELECT DISTINCT uitgever FROM game WHERE id = ANY(%s);", (games,))

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

    dimensions_ = query_database(cursor, "SELECT DISTINCT dimensie FROM game WHERE id = ANY(%s);", (games,))

    for game in get_table_data(cursor, table="game"):
        for dimension in dimensions_:
            if game[0] in games and game[7] == dimension[0] and (dimensions_.index(dimension) + 1) in dimensions:
                games_.append(game[0])

    return games_


def filter_player_types(cursor, games: List[int], player: List[int]) -> List[int]:
    """
    Limit the list of games to the games with the player types chosen by the user.
    """
    
    games_ = []

    if len(player) == 2 and player[0] == 1 and player[1] == 2 or player[0] == 2 and player[1] == 1:
        for game_id in query_database(cursor, "SELECT id FROM game WHERE is_singleplayer = true and is_multiplayer = true"):
            for game in games:
                if game == game_id[0]:
                    games_.append(game)
    else:
        if player[0] == 1:
            for game_id in query_database(cursor, "SELECT id FROM game WHERE is_singleplayer = true and is_multiplayer = false "):
                for game in games:
                    if game == game_id[0]:
                        games_.append(game)

        if player[0] == 2:
            for game_id in query_database(cursor, "SELECT id FROM game WHERE is_multiplayer = true and is_singleplayer = false"):
                for game in games:
                    if game == game_id[0]:
                        games_.append(game)

    return games_
