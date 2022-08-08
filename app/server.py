from flask import Flask, request, render_template, make_response, Markup, redirect, flash, get_flashed_messages
from flask_login import LoginManager, login_user, login_required, logout_user
from sqlalchemy import select, desc
from app.databases import View, Read, User, hash_password, db
from datetime import datetime
import pandas as pd


app = Flask(__name__)
app.secret_key = "some_secret_key"

# Set up connection to your database below:
uri = ""
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


def convert_table(table):
    """
    Method for processing tables with views and reads from the database.
    My example below.
    """
    try:
        table = pd.DataFrame(table)
        table["Date"] = table["timestamp"].apply(lambda x: x.strftime("%d.%m.%Y"))
        table["Time"] = table["timestamp"].apply(lambda x: x.strftime("%H:%M:%S"))
        table = table.rename(columns={"timezone": "Location"})
        return table[["Location", "Date", "Time"]].to_html(index=False)
    except KeyError:
        return "No data"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def root():
    flash("")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        messages = get_flashed_messages()
        return render_template("login.html", message=messages[0] if messages else "")
    if request.method == "POST":
        username = request.form.get("username")
        passwd = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user:
            user.id = user.user_id
            if user.password == hash_password(passwd):
                login_user(user, remember=True)
                return redirect("/stats")
            else:
                return render_template("login.html", message="Incorrect password!")
        else:
            return render_template("login.html", message="Incorrect username!")


@app.route("/stats", methods=["GET", "POST"])
@login_required
def stats():
    if request.method == "GET":
        with db.engine.connect() as conn:
            command = select(View.timestamp, View.timezone). \
                order_by(desc("timestamp"))
            views = conn.execute(command).fetchall()
            command = select(Read.timestamp, Read.timezone). \
                order_by(desc("timestamp"))
            reads = conn.execute(command).fetchall()
        views = convert_table(views)
        reads = convert_table(reads)
        return render_template("stats.html", views=Markup(views), reads=Markup(reads))
    if request.method == "POST":
        logout_user()
        return redirect("/login")


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("You have to be logged in to access stats!")
    return redirect('/login')


@app.route("/view", methods=["POST"])
def opened():
    """
    Call to API to record new website view in the database.
    """
    new_view = View(timestamp=datetime.now(),
                    timezone=request.form["timezone"])
    db.session.add(new_view)
    db.session.commit()
    return make_response("New view added to database.")


@app.route("/read", methods=["POST"])
def read():
    """
    Call to API to record new website read in the database.
    """
    new_read = Read(timestamp=datetime.now(),
                    timezone=request.form["timezone"])
    db.session.add(new_read)
    db.session.commit()
    return make_response("New read added to database.")


if __name__ == "__main__":
    app.run(debug=True)
