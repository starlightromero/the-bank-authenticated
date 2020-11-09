"""Import libraries."""
from the_bank import db


class Account(db.Model):
    """Account database model class."""

    id = db.Column(db.Integer, primary_key=True)
    holder = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text)
    balance = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        """Return account holder."""
        return f"Account('{self.holder}')"

    @property
    def identity(self):
        return self.id

    @property
    def rolenames(self):
        return []

    @classmethod
    def lookup(cls, holder):
        return cls.query.filter_by(holder=holder).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)
