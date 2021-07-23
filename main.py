import parse
import utils
import db

if __name__ == '__main__':
    args = parse.get_command()
    db.create_tables()
    if utils.validate_url(args.url) and args.generate:
        if args.short_url:
            if utils.insert_short_link(args.short_url, args.url):
                print(f'short_url={args.short_url}')
            else:
                print(f'Error! Short_url={args.short_url} is already exists in db!')
        else:
            utils.insert_short_link(utils.get_short_link(args.url), args.url)
            print(f'short_url={utils.get_short_link(args.url)}')
    elif not args.generate:
        if not utils.get_long_link(args.url):
            print(f'Error! Long_url for short_url={args.url} is not exists in db!')
    else:
        print('Error! Url is not correct! Try again!')
