import sqlite3


def create_tables():
    table_links = '''CREATE TABLE IF NOT EXISTS links(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        url_id INTEGER,
                                        short_url_id INTEGER,
                                        FOREIGN KEY (url_id) REFERENCES urls(id),
                                        FOREIGN KEY (short_url_id) REFERENCES urls(id));'''
    table_urls = '''CREATE TABLE IF NOT EXISTS urls(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      is_short BOOLEAN NOT NULL,
                                      url VARCHAR(255) NOT NULL);'''
    do_query(table_links)
    do_query(table_urls)


def do_query(query, *values, select=False):
    try:
        sqlite_connection = sqlite3.connect('links.db')
        # print('Connection to links.db successful')

        cursor = sqlite_connection.cursor()

        cursor.execute(query, values)
        if not select:
            queryid = cursor.lastrowid
        else:
            results = cursor.fetchone()
        cursor.close()

    except sqlite3.Error as error:
        print("Connection error!", error)
    else:
        sqlite_connection.commit()
        # print('Database query completed successfully')
        if select:
            if results:
                return results[0]
            else:
                return results
        else:
            return queryid
    finally:
        sqlite_connection.close()
        # print("Connection with links.db closed")


def insert_to_db(short_link, long_link):
    query = 'INSERT INTO urls (is_short, url) VALUES (TRUE, ?);'
    short_url_id = do_query(query, short_link)
    query = 'INSERT INTO urls (is_short, url) VALUES (FALSE, ?);'
    long_url_id = do_query(query, long_link)
    query = 'INSERT INTO links (short_url_id, url_id) VALUES (?, ?);'
    do_query(query, short_url_id, long_url_id)


def get_short_url_id_from_db(short_link):
    query = 'SELECT id FROM urls WHERE url=? AND is_short=TRUE;'
    results = do_query(query, short_link, select=True)
    return results


def get_long_url_id_from_db(id):
    query = 'SELECT url_id FROM links WHERE short_url_id=?;'
    results = do_query(query, id, select=True)
    return results


def get_url_from_db(id):
    query = 'SELECT url FROM urls WHERE id=? AND is_short=FALSE;'
    results = do_query(query, id, select=True)
    return results


def print_links():
    """query = 'SELECT * FROM links;'
    results = do_query(query, select=True)
    [print(result) for result in results]"""
    pass


def print_urls():
    """query = 'SELECT * FROM urls;'
    results = do_query(query, select=True)
    [print(result) for result in results]"""
    pass
