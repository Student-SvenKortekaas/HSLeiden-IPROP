# SQL Queries
QUERY_GENRES = """
    SELECT DISTINCT genre_id, naam
    FROM genre_games JOIN genre
    ON genre_games.genre_id = genre.id
    WHERE game_id = ANY(%s)
    ORDER BY genre_id;
"""
