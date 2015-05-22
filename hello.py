from flask import Flask
app = Flask(__name__)

#route: an entry point for an app to return HTML content
#'@' is a decorator: if user hits top-level directory ('/'), will execute fn
@app.route('/')
def hello_world():
    return 'Hello World!'

#only runs if app is run from shell
if __name__ == '__main__':
    app.run()
