"""Import libraries."""
from the_bank import db


class Account(db.Model):
    """Account database class."""

    id = db.Column(db.Integer, primary_key=True)
    holder = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text)
    balance = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        """Return Account holder."""
        return f"Account('{self.holder}')"

    @property
    def identity(self):
        """Return Account id."""
        return self.id

    @property
    def rolenames(self):
        """Return an empty list."""
        return []

    @classmethod
    def lookup(cls, holder):
        """Return Account with a given holder."""
        return cls.query.filter_by(holder=holder).one_or_none()

    @classmethod
    def identify(cls, id):
        """Return Account with the given id."""
        return cls.query.get(id)
