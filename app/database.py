from configparser import ConfigParser
from typing import Dict

import psycopg2


def get_config(filename="database.ini", section="postgresql") -> Dict[str, str]:
    """Read the database configuration from a file."""

    db_config = {}

    # Create parser
    parser = ConfigParser()

    # Read the configuration file
    parser.read(filename)

    if parser.has_section(section):
        params = parser.items(section)
        
        for key, value in params:
            db_config[key] = value
    else:
        raise Exception(f"Section {section} not found in the {filename} file")

    return db_config


def get_db(host: str, database: str, user: str, password: str):
    """Create a connection with an existing PostgreSQL database."""

    # Connect to an existing database
    connection = psycopg2.connect(host=host, database=database, user=user, password=password)
    
    # Database cursor
    cursor = connection.cursor()

    return cursor
