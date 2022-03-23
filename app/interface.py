from app.database import get_table_data
from app.logic import (
    filter_game_genres,
    filter_publishers
)
from app.util import format_input, validate_input

games_ids = []

entries = [
    # {
    #     "question": "Welke games heb je al gespeeld?",
    #     "filter_func": None
    # },
    {
        "question": "Welke genres vindt je leuk?",
        "print_func": filter_game_genres,
        "filter_func": filter_game_genres
    }
]


def print_help_text() -> None:
    print("Welkom bij de aanrader.")


def main(cursor) -> None:
    # Print additional help text
    print_help_text()

    games = get_table_data(cursor, table="game")

    for entry in entries:
        input_ = []

        # Print question + available answers
        print(entry["question"])


        while not input_:
            if not validate_input(cursor, format_input(input(entry["question"]))):
                continue
            else:
                input_ = format_input(input(entry["question"]))

            games = entry["filter_func"](cursor, games, input_)

    print(games)

    exit()
    games = get_table_data(cursor, "game")
    for game in games:
        print(str(game[0]) + " " + game[1])
    while True:
        games_played = input("Welke games heb je al gespeeld, geef een nummer").split(" ")

    print("Kies één of meer van de volgende genres:")
    games = get_table_data(cursor, "genre")
    for game in games:
        print(str(game[0]) + " " + game[1])

    print("Van welke uitgever(s) zijn de games?")

    print("Uit welke periode moeten de games komen?")

    print("Uit hoeveel dimensies bestaan de game?:")

    print("Moeten de games Single-Player of Multi-Player zijn?")
