#import Flask class from flask
from flask import Flask
#instantiate a class from Flask called app
app = Flask(__name__)

#route: an entry point for an app to return HTML content
#'@' is a decorator: if user hits top-level directory ('/'), will execute fn
#If top-level directory used, function will handle request
def hello_world():
    return 'Hello World!'

#only runs if app is run from shell
# if name of file is __main__ , being run from terminal .: start server
if __name__ == '__main__':
    app.run()
