import os
from flask import Flask
app = Flask(__name__)
...
...
color = "pink"

@app.route("/")
def main():
    print(color)
    return render_templated('hello.html', color=color)

@app.route('/hii')
def hello():
    return 'how are u'

@app.route('/hello')
def hello2():
    return 'This is sravani'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
