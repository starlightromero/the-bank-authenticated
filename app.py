"""Import and run app."""
from the_bank import create_app
from the_bank.models import Account

app = create_app(Account)

if __name__ == "__main__":
    app.run()
