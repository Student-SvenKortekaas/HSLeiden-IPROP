from configparser import ConfigParser
from typing import Dict

import psycopg2


def get_config(filename="database.ini", section="postgresql") -> Dict[str, str]:
    """
    Read the database configuration from a file.
    
    :param filename: The name of the configuration file.
    :param section: The section in the configuration file to search for.
    :return: The database configuration variables.
    :rtype: Dict[str, str]
    """

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


def get_cursor(host: str, database: str, user: str, password: str):
    """
    Create a connection with an existing PostgreSQL database.
    
    :param host: The host name.
    :param database: The name of the database.
    :param user: The name of the user.
    :param password: The password of the user.
    :return: A database cursor to interact with the database.
    """

    # Connect to an existing database
    connection = psycopg2.connect(host=host, database=database, user=user, password=password)
    
    # Database cursor
    cursor = connection.cursor()

    return cursor


def get_table_data(cursor, table):
    """
    Retrieve data from a database table.

    :param cursor: The database cursor.
    :param table: The database table from which the data is retrieved.
    """

    cursor.execute(f"SELECT * FROM {table};")
    return cursor.fetchall()


def query_database(cursor, query: str):
    cursor.execute(query)
    return cursor.fetchall()
