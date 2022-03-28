# SQL Queries
N_GAME_SUGGESTIONS = 5

QUERY_DIMENSIONS = """
    SELECT DISTINCT dimensie 
    FROM game WHERE id = ANY(%s);
"""

QUERY_GENRES = """
    SELECT DISTINCT genre_id, naam
    FROM genre_games JOIN genre
    ON genre_games.genre_id = genre.id
    WHERE game_id = ANY(%s)
    ORDER BY genre_id;
"""

QUERY_PLAYER_TYPE_ALL = """
    SELECT id 
    FROM game 
    WHERE is_singleplayer = true AND is_multiplayer = true AND id = ANY(%s);
"""

QUERY_PLAYER_TYPE_MULTI_PLAYER = """
    SELECT id 
    FROM game 
    WHERE is_multiplayer = true AND id = ANY(%s);
"""

QUERY_PLAYER_TYPE_SINGLE_PLAYER = """
    SELECT id 
    FROM game 
    WHERE is_singleplayer = true AND id = ANY(%s);
"""

QUERY_PUBLISHERS = """
    SELECT DISTINCT uitgever 
    FROM game WHERE id = ANY(%s);
"""