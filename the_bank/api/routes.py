"""Import libraries."""
from flask import Blueprint, request, jsonify
from the_bank import db
from the_bank.models import Account

api = Blueprint("api", __name__)


@api.route("/account", methods=["GET"])
def get_all_accounts():
    """Get all open accounts."""
    accounts = Account.query.all()
    print(accounts)
    return ""


@api.route("/account", methods=["POST"])
def open_account():
    """Open a new account."""
    holder = request.json.get("holder")
    account = Account.query.filter_by(holder=holder).first()
    if account:
        return jsonify({"error": "Account already exists"})
    account = Account(holder=holder)
    db.session.add(account)
    db.session.commit()
    return (
        jsonify(
            {"message": f"An account for {account.holder} has been created"}
        ),
        201,
    )


@api.route("/account/<holder>", methods=["GET"])
def view_account(holder):
    """View an account."""
    account = Account.query.filter_by(holder=holder).first()
    if account:
        return (
            jsonify({"holder": account.holder, "balance": account.balance}),
            200,
        )
    return jsonify({"error": "Account does not exist"})


@api.route("/account/<holder>", methods=["DELETE"])
def close_account(holder):
    """Close an account."""
    account = Account.query.filter_by(holder=holder).first()
    if not account:
        return jsonify({"error": "Account does not exist"})
    if account.balance > 0:
        return jsonify({"error": "Remove balance before closing account"})
    db.session.delete(account)
    db.session.commit()
    return jsonify({"message": "The account has been closed"})


@api.route("/account/<holder>/deposit", methods=["POST"])
def deposit(holder):
    """Deposit to account of a given holder."""
    account = Account.query.filter_by(holder=holder).first()
    if not account:
        return jsonify({"error": "Account does not exist"})
    amount = request.json.get("amount")
    account.balance += amount
    db.session.commit()
    return jsonify(
        {
            "holder": account.holder,
            "balance": account.balance,
            "message": "The deposit has been processed",
        }
    )


@api.route("/account/<holder>/withdraw", methods=["POST"])
def withdraw(holder):
    """Withdraw from account of a given holder."""
    account = Account.query.filter_by(holder=holder).first()
    amount = request.json.get("amount")
    if not account:
        return jsonify({"error": "Account does not exist"})
    if account.balance >= amount:
        account.balance -= amount
        db.session.commit()
        return jsonify(
            {
                "holder": account.holder,
                "balance": account.balance,
                "message": "The withdraw has been processed",
            }
        )
    return jsonify({"error": "The account balance is insufficient"})
