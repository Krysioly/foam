"""Model for database"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Wood(db.Model):
    """ Create woods in database"""

    __tablename__ = "woods"

    name = db.Column(db.String(100), nullable = False, primary_key= True)
    image = db.Column(db.String(100), nullable = False)


    def __repr__(self):
            """Provide helpful representation when printed."""
            return f"<Wood name={self.name}>"

############################################################################
def connect_to_db(app, db_uri='postgresql:///woods'):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")