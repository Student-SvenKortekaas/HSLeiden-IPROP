from app.database import get_config, get_cursor, get_data


if __name__ == "__main__":
    # Connect to database
    config = get_config()
    cursor = get_cursor(**config)

    print(get_data(cursor, "game"))