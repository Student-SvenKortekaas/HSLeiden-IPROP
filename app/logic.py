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

    publishers_ = query_database(cursor, "SELECT DISTINCT uitgever FROM game")

    for game in get_table_data(cursor, table="game"):
        for publisher in publishers_:
            if game[0] in games and game[3] == publisher[0] and (publishers_.index(publisher) + 1) in publishers:
                games_.append(game[0])

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
        dimensions_games.append(all_dimensions[i - 1][0])

    for game_id_dimensions in query_database(cursor, "SELECT id FROM game WHERE dimensie = ANY(%s)",
                                             (dimensions_games,)):
        for game_id in games:
            if game_id == game_id_dimensions[0]:
                games_.append(game_id)

    return games_


def filter_player_types(cursor, games: List[int], player: List[int]) -> List[int]:
    """
    Limit the list of games to the games with a year chosen by the user.
    """
    print(games)
    games_ = []
    if len(player) == 2 and player[0] == 1 and player[1] == 2 or player[0] == 2 and player[1] == 1:
        for game_id in query_database(cursor,
                                      "SELECT id FROM game WHERE is_singleplayer = true and is_multiplayer = true"):
            print(game_id)
            for game in games:
                if game == game_id[0]:
                    games_.append(game)
    else:
        if player[0] == 1:
            for game_id in query_database(cursor, "SELECT id FROM game WHERE is_singleplayer = true and is_multiplayer = false "):
                print(game_id)
                for game in games:
                    if game == game_id[0]:
                        games_.append(game)

        if player[0] == 2:
            for game_id in query_database(cursor, "SELECT id FROM game WHERE is_multiplayer = true and is_singleplayer = false"):
                for game in games:
                    if game == game_id[0]:
                        games_.append(game)

    return games_
