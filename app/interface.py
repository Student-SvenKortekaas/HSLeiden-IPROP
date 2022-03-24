from colorama import (
    init,
    Fore,
    Style
)
import pyfiglet

from app.database import get_table_data
from app.logic import (
    filter_dimensions,
    filter_genres,
    filter_player_types,
    filter_publishers
)
from app.util import (
    format_input,
    print_dimensions,
    print_games,
    print_genres,
    print_player_types,
    print_publishers
)

# Initialize colorma
init()

entries = [
    {
        "question": "Welke games heb je al gespeeld?",
        "print_func": print_games,
        "filter_func": None
    },
    {
        "question": "Welke genres vindt je leuk?",
        "print_func": print_genres,
        "filter_func": filter_genres
    },
    {
        "question": "Van welke uitgever(s) zijn de games?",
        "print_func": print_publishers,
        "filter_func": filter_publishers,
    },
    {
        "question": "Uit hoeveel dimensies bestaan de game?",
        "print_func": print_dimensions,
        "filter_func": filter_dimensions
    },
    {
        "question": "Moeten de games Single-Player of Multi-Player zijn?",
        "print_func": print_player_types,
        "filter_func": filter_player_types
    }
]


def print_help_text() -> None:
    banner = pyfiglet.figlet_format("DE AANRADER!")
    usage = "Om opties te selecteren kan je de getallen, gescheiden door spaties, invoeren.\n> 1 2 3\n"

    print(Fore.BLUE + banner)
    print(Style.RESET_ALL + usage)


def main(cursor) -> None:
    try:
        # Print additional help text
        print_help_text()

        input("Klik op ENTER om door te gaan...")

        # Use a List Comprehension to create a list of the game IDs
        games = [game[0] for game in get_table_data(cursor, table="game")]

        for entry in entries:
            user_input = []

            # If there is not more than 1 game left, break out of the for-loop
            if len(games) <= 1:
                break

            # Print question + available answers
            print(entry["question"])
            entry["print_func"](cursor, games)

            while not user_input:
                user_input = format_input(input("> "))

                if entry.get("filter_func", None):
                    games = entry["filter_func"](cursor, games, user_input)
                else:
                    games = user_input

        print("\nDit zijn jouw aanbevolen games:")

        for i, game_id in enumerate(games):
            for game in get_table_data(cursor, table="game"):
                if game_id == game[0]:
                    id, name, release_year, publisher, rating, is_singleplayer, is_multiplayer, dimensions = game

                    print(Fore.GREEN + f"{i + 1}\t{name} - {release_year} - {publisher} - {rating}")

    except KeyboardInterrupt: pass
