import argparse


def get_command():
    parser = argparse.ArgumentParser(description='Convert long url to short')
    parser.add_argument('url', type=str, help='Input url!')
    parser.add_argument('--generate', action='store_const', const=True, default=False,
                        help='Input "--generate" if you want to generate short url!')
    parser.add_argument('--short_url', type=str, default=False,
                        help='Input "--short_url" or if you want print and save short url!')
    argsfromline = parser.parse_args()
    return argsfromline
