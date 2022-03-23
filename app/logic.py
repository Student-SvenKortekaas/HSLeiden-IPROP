from typing import List

from app.database import get_data


def filter_played_games(cursor, choices: List[int]) -> List[int]:
    """
    Limit the list of games to only the games the user has played.
    """

    played_games = []

    games = get_data(cursor, table="game")

    for game in games:
        if game[0] in choices:
            played_games.append(game[0])

    return played_games
