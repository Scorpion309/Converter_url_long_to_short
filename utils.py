import shortuuid
import validators

import db


def insert_short_link(short_link, long_link):
    if not db.get_short_url_id_from_db(short_link):
        db.insert_to_db(short_link, long_link)
        return True
    else:
        return False


def validate_url(value):
    return validators.url(value)


def get_short_link(long_link):
    short_link = shortuuid.uuid(name=long_link)
    return short_link


def get_long_link(short_link):
    short_url_id = db.get_short_url_id_from_db(short_link)
    if short_url_id:
        long_url_id = db.get_long_url_id_from_db(short_url_id)
        long_url = db.get_url_from_db(long_url_id)
        return long_url
    else:
        return False
