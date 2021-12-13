from flask import Flask, render_template
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showroom')
def Showroom():
    return render_template('showroom.html')



if __name__ == '__main__':
    app.run()