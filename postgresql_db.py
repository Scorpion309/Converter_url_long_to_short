import psycopg2

connect = psycopg2.connect(dbname='postgresql_links', user='test',
                              password='test', host='localhost', port=5432)


def do_query(query, values=None, connection=connect, select=False):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        print(values)
        queryid = cursor.execute(query, values)
        print(queryid)
        if select:
            results = cursor.fetchone()
        print("Query executed successfully")
    except:
        print("The error occurred")
    else:
        if select:
            if results:
                return results[0]
            else:
                return results
        else:
            return queryid
    finally:
        cursor.close()
        connection.close()


def create_tables():
    create_links = '''CREATE TABLE IF NOT EXISTS links(
                        id INT SERIAL PRIMARY KEY,
                        url_id INT REFERENCES urls(id),
                        short_url_id INT REFERENCES urls(id))'''

    create_urls = '''CREATE TABLE IF NOT EXISTS urls(
                       id INT SERIAL PRIMARY KEY,
                       is_short BOOL,
                       url TEXT)'''
    do_query(create_links)
    do_query(create_urls)


def insert_to_db(short_link, long_link):
    query = 'INSERT INTO urls (is_short, url) VALUES (TRUE, %s)) RETURNING id;'
    short_url_id = do_query(query, short_link)
    query = 'INSERT INTO urls (is_short, url) VALUES (FALSE, %s) RETURNING id;'
    long_url_id = do_query(query, long_link)
    query = 'INSERT INTO links (short_url_id, url_id) VALUES (%s, %s);'
    do_query(query, short_url_id, long_url_id)


def get_short_url_id_from_db(short_link):
    query = 'SELECT id FROM urls WHERE url=(%s) AND is_short=TRUE;'
    results = do_query(query, short_link, select=True)
    return results


def get_long_url_id_from_db(id):
    query = 'SELECT url_id FROM links WHERE short_url_id=(%s);'
    results = do_query(query, id, select=True)
    return results


def get_url_from_db(id):
    query = 'SELECT url FROM urls WHERE id=(%s) AND is_short=FALSE;'
    results = do_query(query, id, select=True)
    return results
