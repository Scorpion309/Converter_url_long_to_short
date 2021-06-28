import shortuuid

import db
import parse


def get_short_link(long_link):
    short_link = shortuuid.uuid(name=long_link)
    return short_link


if __name__ == '__main__':
    db.create_tables()
    args = parse.get_command()
    get_short_link(args.url)

    if args.generate:
        if args.short_url:
            short_url = args.short_url

            short_url_id = db.get_short_url_id_from_db(short_url)
            if short_url_id == []:
                db.insert_to_db(short_url, args.url)
                print(f'short_url={short_url}')
            else:
                print(f'Error! Short_url={short_url} is already exists in db!')

        else:
            short_url = get_short_link(args.url)
            short_url_id = db.get_short_url_id_from_db(short_url)
            if short_url_id == []:
                db.insert_to_db(short_url, args.url)
                print(f'short_url={short_url}')
            else:
                print(f'short_url={short_url}')
    else:
        short_url = args.url
        short_url_id = db.get_short_url_id_from_db(short_url)
        if short_url_id != []:
            long_url_id = db.get_long_url_id_from_db(short_url_id[0][0])
            long_url = db.get_url_from_db(long_url_id[0][0])
            print(f'long_url={long_url[0][0]}')
        else:
            print(f'Error! Long_url for short_url={short_url} is not exists in db!')
