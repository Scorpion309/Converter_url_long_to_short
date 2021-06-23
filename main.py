import shortuuid

import db
import parse


def get_short_link(long_link):
    short_link = shortuuid.uuid(name=long_link)
    return short_link


if __name__ == '__main__':
    db.new_db()
    args = parse.get_command()
    get_short_link(args.url)

    if args.generate:
        if args.short_url:
            short_url = args.short_url
            print(f'short_url={short_url}')
            db.insert_to_db(short_url, args.url)
            # save to DB short and long links. If link exists -> error!
        else:
            short_url = get_short_link(args.url)
            print(f'short_url={short_url}')
            db.insert_to_db(short_url, args.url)
            # save to DB short and long links. If link exists -> error!

    else:
        long_url = db.get_from_db(args.url)
        # print long url from DB
        print(f'long_url={long_url}')
