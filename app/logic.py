from typing import List

from app.database import get_table_data, query_database


def filter_game_genres(cursor, games: List[int], genres: List[int]) -> List[int]:
    """
    Limit the list of games to only the games with a genre chosen by the user..
    """

    games_ = []

    for _, game_id, genre_id in get_table_data(cursor, table="genre_games"):
        if game_id in games and genre_id in genres:
            games_.append(game_id)

    return games_


def filter_publishers(cursor, games: List[int], publishers: List[int]) -> List[int]:
    """
    Limit the list of games to the games with a publisher chosen by the user.
    """

    games_ = []

    publishers_games = []

    all_publishers = query_database(cursor, "SELECT DISTINCT uitgever FROM game")

    for i in range(len(publishers)):
        publishers_games.append(all_publishers[i - 1])

    for game_id_publishers in query_database(cursor, "SELECT id FROM game WHERE uitgever = ANY(%s)", (publishers_games,)):
        for game_id in games:
            if game_id == game_id_publishers:
                games_.append(game_id)

    print(games_)
    return games_


def filter_years(cursor, games: List[int], years: List[int]) -> List[int]:
    """
    Limit the list of games to the games with a year chosen by the user.
    """

    games_ = []

    years_games = []

    all_years = query_database(cursor, "SELECT DISTINCT jaartal FROM game")

    for i in range(len(years)):
        years_games.append(all_years[i - 1])

    for game_id_years in query_database(cursor, "SELECT id FROM game WHERE jaartal IN %s", (years_games,)):
        for game_id in games:
            if game_id == game_id_years:
                games_.append(game_id)

    return games_


def filter_dimension(cursor, games: List[int], dimensions: List[int]) -> List[int]:
    """
    Limit the list of games to the games with a year chosen by the user.
    """

    games_ = []

    dimensions_games = []

    all_dimensions = query_database(cursor, "SELECT DISTINCT dimensie FROM game")

    for i in range(len(dimensions)):
        dimensions_games.append(all_dimensions[i - 1])

    for game_id_dimensions in query_database(cursor, "SELECT id FROM game WHERE dimensie = ANY(%s)", (dimensions_games,)):
        for game_id in games:
            if game_id == game_id_dimensions:
                games_.append(game_id)

    return games_


def filter_player(cursor, games: List[int], player: List[int]) -> List[int]:
    """
    Limit the list of games to the games with a year chosen by the user.
    """

    games_ = []

    player_games = []

    for i in range(len(player)):
        if player[i] == 1:
            for game_id in query_database(cursor, "SELECT id FROM game WHERE is_singleplayer = %s", True):
                player_games.append(game_id)
        else:
            for game_id in query_database(cursor, "SELECT id FROM game WHERE is_multiplayer = %s", True):
                player_games.append(game_id)

    for game_id_player in player_games:
        for game_id in games:
            if game_id == game_id_player:
                games_.append(game_id)

    return games_
