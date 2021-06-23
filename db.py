import sqlite3


def new_db():
    try:
        sqlite_connection = sqlite3.connect('links.db')
        cursor = sqlite_connection.cursor()
        print('Connection to links.db successful')

        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS links(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        url_id INTEGER,
                                        short_url_id INTEGER,
                                        FOREIGN KEY (url_id) REFERENCES urls(id),
                                        FOREIGN KEY (short_url_id) REFERENCES urls(id));
                                        '''
        cursor.execute(sqlite_create_table_query)

        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS urls(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        is_short BOOLEAN NOT NULL,
                                        url VARCHAR(255) NOT NULL);'''
        cursor.execute(sqlite_create_table_query)
        cursor.close()
    except sqlite3.Error as error:
        print("Connection error!", error)
    else:
        sqlite_connection.commit()
        print('Tables "links" and "urls" created successfully')
    finally:
        sqlite_connection.close()
        print("Connection with links.db closed")


def insert_to_db(short_link, long_link):
    pass


def get_from_db(short_link):
    pass
