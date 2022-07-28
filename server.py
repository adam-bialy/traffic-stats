from flask import Flask, request, render_template, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from databases import View, Read
import config
from datetime import datetime
import pandas as pd


app = Flask(__name__)
engine = create_engine(config.DATABASE_URL)


@app.route("/")
def home():
    data = "XD"
    return render_template("index.html", data=data)


@app.route("/view", methods=["POST"])
def opened():
    print(request.form)
    with Session(engine) as session:
        new_view = View(timestamp=datetime.now(),
                        timezone=request.form["timezone"],
                        ip=request.remote_addr)
        session.add_all([new_view])
        session.commit()
    return make_response("New view added to database.")


@app.route("/read", methods=["POST"])
def read():
    with Session(engine) as session:
        new_read = Read(timestamp=datetime.now(),
                        timezone=request.form["timezone"],
                        ip=request.remote_addr)
        session.add_all([new_read])
        session.commit()
    return make_response("New read added to database.")


if __name__ == "__main__":
    app.run(debug=True)
