from app.database import get_config, get_cursor
from app.interface import main


if __name__ == "__main__":
    # Connect to database
    config = get_config()
    cursor = get_cursor(**config)

    # Interact with the user
    main(cursor)