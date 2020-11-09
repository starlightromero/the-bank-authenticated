"""Import libraries."""
from the_bank import db


class Account(db.Model):
    """Account database model class."""

    id = db.Column(db.Integer, primary_key=True)
    holder = db.Column(db.String(100), nullable=False, unique=True)
    balance = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        """Return account holder."""
        return f"Account('{self.holder}')"
