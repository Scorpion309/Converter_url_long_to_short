import shortuuid

import db
import parse


def get_short_link(long_link):
    short_link = shortuuid.uuid(name=long_link)
    return short_link


def insert_short_link(short_link):
    short_url_id = db.get_short_url_id_from_db(short_link)
    if not short_url_id:
        db.insert_to_db(short_link, args.url)
        print(f'short_url={short_link}')
    else:
        if not args.generate:
            print(f'Error! Short_url={short_link} is already exists in db!')
        else:
            print(f'short_url={short_link}')

def get_long_link(short_link):
    short_url_id = db.get_short_url_id_from_db(short_link)
    if short_url_id:
        long_url_id = db.get_long_url_id_from_db(short_url_id)
        long_url = db.get_url_from_db(long_url_id)
        print(f'long_url={long_url}')
        return long_url
    else:
        print(f'Error! Long_url for short_url={short_link} is not exists in db!')
        return f'Error! Long_url for short_url={short_link} is not exists in db!'


if __name__ == '__main__':
    db.create_tables()
    args = parse.get_command()
    get_short_link(args.url)

    if args.generate:
        if args.short_url:
            insert_short_link(args.short_url)
        else:
            insert_short_link(get_short_link(args.url))
    else:
        get_long_link(args.url)
