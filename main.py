import argparse
import sqlite3

import shortuuid


def new_db():
    try:
        sqlite_connection = sqlite3.connect('links.db')
        cursor = sqlite_connection.cursor()
        print('Connection to links.db successful')

        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS links (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        url_id INTEGER,
                                        FOREIGN KEY (url_id) REFERENCES urls(url_id));
                                        '''
        cursor.execute(sqlite_create_table_query)

        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS urls(
                                        url_id INTEGER PRIMARY KEY AUTOINCREMENT,
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


def get_command():
    parser = argparse.ArgumentParser(description='Convert long url to short')
    parser.add_argument('url', type=str, help='Input url!')
    parser.add_argument('--generate', action='store_const', const=True, default=False,
                        help='Input "--generate" if you want to generate short url!')
    parser.add_argument('--short_url', type=str, default=False,
                        help='Input "--short_url" or if you want print and save short url!')
    argsfromline = parser.parse_args()
    return argsfromline


def get_short_link(long_link):
    short_link = shortuuid.uuid(name=long_link)
    return short_link


if __name__ == '__main__':
    new_db()
    args = get_command()
    get_short_link(args.url)

    if args.generate:
        if args.short_url:
            short_url = args.short_url
            print(f'short_url={short_url}')
            insert_to_db(short_url, args.url)
            # save to DB short and long links. If link exists -> error!
        else:
            short_url = get_short_link(args.url)
            print(f'short_url={short_url}')
            insert_to_db(short_url, args.url)
            # save to DB short and long links. If link exists -> error!

    else:
        long_url = get_from_db(args.url)
        # print long url from DB
        print(f'long_url={long_url}')
