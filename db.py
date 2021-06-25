import sqlite3

tables = ('''CREATE TABLE IF NOT EXISTS links(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        url_id INTEGER,
                                        short_url_id INTEGER,
                                        FOREIGN KEY (url_id) REFERENCES urls(id),
                                        FOREIGN KEY (short_url_id) REFERENCES urls(id));
                                        ''',
          '''CREATE TABLE IF NOT EXISTS urls(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      is_short BOOLEAN NOT NULL,
                                      url VARCHAR(255) NOT NULL);''')


def do_query(queryes, select=False):
    try:
        queryid = []
        sqlite_connection = sqlite3.connect('links.db')
        #print('Connection to links.db successful')
        cursor = sqlite_connection.cursor()

        for query in queryes:
            if query != '':
                cursor.execute(query)

                if not select:
                    queryid.append(cursor.lastrowid)
                else:
                    results = cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        print("Connection error!", error)
    else:
        sqlite_connection.commit()
        #print('Database query completed successfully')

        if select:
            return results
        else:
            return queryid
    finally:
        sqlite_connection.close()
        #print("Connection with links.db closed")


def insert_to_db(short_link, long_link):
    query = (f'INSERT INTO urls (is_short, url) VALUES (TRUE ,"{short_link}");',
             f'INSERT INTO urls (is_short, url) VALUES (FALSE , "{long_link}");')
    id_to_save = do_query(query)
    print(id_to_save)
    query = (f'INSERT INTO links (short_url_id, url_id) VALUES ("{id_to_save[0]}" ,"{id_to_save[1]}");', '')
    do_query(query)


def get_short_url_id_from_db(short_link):
    query = (f'SELECT id FROM urls WHERE url="{short_link}" AND is_short=TRUE;', '')
    results = do_query(query, select=True)
    return results


def get_long_url_id_from_db(id):
    query = (f'SELECT url_id FROM links WHERE short_url_id="{id}";', '')
    results = do_query(query, select=True)
    return results


def get_url_from_db(id):
    query = (f'SELECT url FROM urls WHERE id="{id}" AND is_short=FALSE;', '')
    results = do_query(query, select=True)
    return results


def print_links():
    query = ('SELECT * FROM links;', '')
    results = do_query(query, select=True)
    # [print(result) for result in results]


def print_urls():
    query = ('SELECT * FROM urls;', '')
    results = do_query(query, select=True)
    # [print(result) for result in results]
