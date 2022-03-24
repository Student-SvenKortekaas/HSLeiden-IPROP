from app.database import get_table_data
from app.logic import (
    filter_game_genres,
    filter_publishers
)
from app.util import (
    format_input,
    print_games,
    print_genres,
    print_publishers,
    validate_input
)

entries = [
    {
        "question": "Welke games heb je al gespeeld?",
        "print_func": print_games,
        "filter_func": None
    },
    {
        "question": "Welke genres vindt je leuk?",
        "print_func": print_genres,
        "filter_func": filter_game_genres
    }
]


def print_help_text() -> None:
    print("Welkom bij de aanrader.")


def main(cursor) -> None:
    # Print additional help text
    print_help_text()

    # Use a List Comprehension to create a list of the game IDs
    games = [game[0] for game in get_table_data(cursor, table="game")]

    for entry in entries:
        user_input = []

        # Print question + available answers
        print(entry["question"])
        entry["print_func"](cursor, games)

        while not user_input:
            user_input = format_input(input("> "))

            if entry.get("filter_func", None):
                games = entry["filter_func"](cursor, games, user_input)
            else:
                games = user_input

    print(games)
