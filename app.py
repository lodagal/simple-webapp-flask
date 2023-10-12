import os
from flask import Flask
app = Flask(__name__)
...
...
APP_COLOR = "pink"

@app.route("/")
def main():
    print(APP_COLOR)
    return render_templated('hello.html', APP_COLOR= "PINK" )

@app.route('/hii')
def hello():
    return 'how are u'

@app.route('/hello')
def hello2():
    return 'This is sravani'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
