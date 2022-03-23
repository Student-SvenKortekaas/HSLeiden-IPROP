from typing import List

from app.database import get_data


def filter_game_genres(cursor, games: List[int], genres: List[int]) -> List[int]:
    """
    Limit the list of games to only the games with a genre chosen by the user..
    """

    games_ = []

    for _, game_id, genre_id in get_data(cursor, table="genre_games"):
        if game_id in games and genre_id in genres:
            games_.append(game_id)

    return games_
