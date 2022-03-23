from app.database import get_data

games_ids = []

def main(cursor) -> None:
    games = get_data(cursor, "game")
    for game in games:
        print(str(game[0]) + " " + game[1])
    while True:
        games_played = input("Welke games heb je al gespeeld, geef een nummer").split(" ")

    print("Kies één of meer van de volgende genres:")
    games = get_data(cursor, "genre")
    for game in games:
        print(str(game[0]) + " " + game[1])

    print("Van welke uitgever(s) zijn de games?")

    print("Uit welke periode moeten de games komen?")

    print("Uit hoeveel dimensies bestaan de game?:")

    print("Moeten de games Single-Player of Multi-Player zijn?")
