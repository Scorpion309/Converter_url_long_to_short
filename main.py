import argparse

import requests


def get_command():
    parser = argparse.ArgumentParser(description='Convert long url to short')
    parser.add_argument('url', type=str, help='Input url!')
    parser.add_argument('--generate', action='store_const', const=True, default=False,
                        help='Input "--generate" if you want to generate short url!')
    parser.add_argument('--short_url', type=str, default=False,
                        help='Input "--short_url" or if you want print and save short url!')
    argsfromline = parser.parse_args()
    return argsfromline


def get_short_link(long_url):
    headers = {
        'Authorization': 'Bearer f8207b10679b92278e61b035c374c08e225e351a',
        'Content-Type': 'application/json',
    }
    data = {'long_url': long_url}
    short_link_resp = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)

    if 200 <= short_link_resp.status_code <= 201:
        short_link_json = short_link_resp.json()
        short_link = short_link_json['link']
        print(short_link)
        return short_link
    else:
        print('Error!', short_link_resp)
        print(short_link_resp.json())


if __name__ == '__main__':
    args = get_command()
    get_short_link(args.url)
    print(args)
