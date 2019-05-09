import os
from datetime import datetime as dt
from random import randrange

from bottle import route, run, static_file, view


@route("/")
def index():
    return "<h1>Success of the page!</h1>"

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)