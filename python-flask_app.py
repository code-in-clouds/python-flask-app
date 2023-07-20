from flask import Flask
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "welcome to flask application"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=3000)