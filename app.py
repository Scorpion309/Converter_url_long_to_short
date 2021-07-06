from flask import Flask, render_template, request

import utils

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = utils.get_short_link(long_url)
        if utils.insert_short_link(short_url, long_url):
            return short_url

    return render_template('index.html')


@app.route('/<string:short_link>')
def short_url(short_link):
    long_link = utils.get_long_link(short_link)
    return long_link


if __name__ == '__main__':
    app.run(debug=True)
