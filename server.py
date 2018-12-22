from flask import (Flask, request, render_template, redirect, session)
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "papabear"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    # show homepage
    print("\n\nshow homepage\n\n")
    return render_template("homepage.html")
     

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)

    # connect_to_db(app, 'postgresql:///journals')
    app.run(port=5000, host='0.0.0.0')