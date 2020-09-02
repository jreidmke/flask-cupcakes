"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False, default="https://tinyurl.com/demo-cupcake")

    def serialize_cupcake(self):
        """Returns dict for json response"""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

def connect_db(app):
    db.app = app
    db.init_app(app)
