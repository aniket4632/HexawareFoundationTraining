# DBConnection.py

import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            config = ConfigParser()
            config.read('config.properties')

            db_url = config.get('DatabaseConfig', 'db_url')
            db_port = config.get('DatabaseConfig', 'db_port')
            db_name = config.get('DatabaseConfig', 'db_name')
            db_username = config.get('DatabaseConfig', 'db_username')
            db_password = config.get('DatabaseConfig', 'db_password')

            try:
                DBConnection.connection = mysql.connector.connect(
                    host=db_url,
                    port=db_port,
                    database=db_name,
                    user=db_username,
                    password=db_password
                )
                if DBConnection.connection.is_connected():
                    print("Connected to the database.")
                else:
                    print("Connection failed.")
            except Error as e:
                print(f"Error: {e}")
        return DBConnection.connection


