import main
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:short_link>')
def short_url(short_link):
    long_link = main.get_long_link(short_link)
    return long_link


if __name__ == '__main__':
    app.run(debug=True)