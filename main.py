from app.database import get_config, get_db_cursor


if __name__ == "__main__":
    # Connect to database
    config = get_config()
    cursor = get_db_cursor(**config)