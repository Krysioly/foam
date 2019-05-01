from flask import (Flask, request, render_template, redirect, session)
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import connect_to_db, db, Wood

app = Flask(__name__)
app.secret_key = "yes"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    # show homepage
    print("\n\nshow homepage\n\n")
    
    return render_template("homepage.html")
     
@app.route('/woods')
def show_woods():
    """Show woods"""
    findwoods = Wood.query.all()
    return render_template("woods.html", woods = findwoods)
     
@app.route('/tables')
def show_tables():
    """Show tables"""
    return render_template("tables.html")
     
@app.route('/smalls')
def show_smalls():
    """Show smalls"""
    return render_template("smalls.html")
     




if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)

    connect_to_db(app, 'postgresql:///woods')
    app.run(port=5000, host='0.0.0.0')