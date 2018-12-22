"""Model for database"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Props():

    __tablename__ = "props"

    name = db.Column(db.String(100), nullable = False)
    image = db.Column(db.Sting(100), nullable = False)


    def __repr__(self):
            """Provide helpful representation when printed."""
            return f"<Prop name={self.name}>"
