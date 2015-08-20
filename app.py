from flask import Flask

app = Flask(__name__)


@app.route('/<adds>')
def main(adds):
    return '<h1>Hello User, %s!</h1>' % adds


if __name__=='__main__':
    app.run()
