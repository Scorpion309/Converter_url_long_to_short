import main
from flask import Flask, render_template, request

app = Flask(__name__)
server = 'http://127.0.0.1:5000/'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = server + main.get_short_link(long_url)
        return short_url
        main.insert_short_link(short_url)

    return render_template('index.html')


@app.route('/<string:short_link>')
def short_url(short_link):
    long_link = main.get_long_link(short_link)
    return long_link


if __name__ == '__main__':
    app.run(debug=True)