"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()

class Cupcake(db.Model):

    __tablename__ = 'cupcake'

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False)

    def image(self):
        """defualt image for cupcake"""

        return self.image or DEFAULT_IMG

