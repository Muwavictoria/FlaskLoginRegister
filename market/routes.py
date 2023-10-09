from market import app
from flask import render_template
from market.models import Item


@app.route("/home")
@app.route("/homePage")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    # displaying items
    items = Item.query.all()

    # displaying a specific name in the html
    # return render_template("market.html", item_name = "phone")
    return render_template("market.html", items=items)
