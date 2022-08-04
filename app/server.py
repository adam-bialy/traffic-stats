from flask import Flask, request, render_template, make_response, Markup
from sqlalchemy import create_engine, select, desc
from sqlalchemy.orm import Session
from databases import View, Read
import config
from datetime import datetime
import pandas as pd


app = Flask(__name__)
app.secret_key = "key_to_ag_stats"
engine = create_engine(config.DATABASE_URL)


def convert_table(table):
    try:
        table = pd.DataFrame(table)
        table["Date"] = table["timestamp"].apply(lambda x: x.strftime("%d.%m.%Y"))
        table["Time"] = table["timestamp"].apply(lambda x: x.strftime("%H:%M:%S"))
        table = table.rename(columns={"timezone": "Location"})
        return table[["Location", "Date", "Time"]].to_html(index=False)
    except KeyError:
        return "No data"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        with engine.connect() as conn:
            command = select(View.timestamp, View.timezone).\
                order_by(desc("timestamp"))
            views = conn.execute(command).fetchall()
            command = select(Read.timestamp, Read.timezone).\
                order_by(desc("timestamp"))
            reads = conn.execute(command).fetchall()
        views = convert_table(views)
        reads = convert_table(reads)
        return render_template("index.html", views=Markup(views), reads=Markup(reads))
    if request.method == "POST":
        with engine.connect() as conn:
            command = select(View.timestamp, View.timezone).\
                order_by(desc("timestamp"))
            views = conn.execute(command).fetchall()
            command = select(Read.timestamp, Read.timezone).\
                order_by(desc("timestamp"))
            reads = conn.execute(command).fetchall()
        views = convert_table(views)
        reads = convert_table(reads)
        return render_template("index.html", views=Markup(views), reads=Markup(reads))


@app.route("/view", methods=["POST"])
def opened():
    with Session(engine) as session:
        new_view = View(timestamp=datetime.now(),
                        timezone=request.form["timezone"])
        session.add_all([new_view])
        session.commit()
    return make_response("New view added to database.")


@app.route("/read", methods=["POST"])
def read():
    with Session(engine) as session:
        new_read = Read(timestamp=datetime.now(),
                        timezone=request.form["timezone"])
        session.add_all([new_read])
        session.commit()
    return make_response("New read added to database.")


if __name__ == "__main__":
    app.run(debug=True)
