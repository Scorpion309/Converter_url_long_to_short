from flask import Flask, render_template, request, redirect

import utils

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        if utils.validate_url(long_url):
            if request.form['short_url']:
                short_url = request.form['short_url']
            else:
                short_url = utils.get_short_link(long_url)

            if utils.insert_short_link(short_url, long_url):
                return short_url, 201
            elif request.form['short_url']:
                return f'Error! Short_url {request.form["short_url"]} already exists in db! Please, type another!', 400
            else:
                return short_url, 201
        else:
            return 'Error! You type incorrect url! Please, try again!', 400
    return render_template('index.html')


@app.route('/<string:short_link>')
def short_url(short_link):
    long_link = utils.get_long_link(short_link)
    if long_link:
        return redirect(long_link)
    else:
        return 'Error! This short url is not exists in db! Please, enter correct url!', 404


if __name__ == '__main__':
    app.run(debug=True)
