from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/stats", methods=["POST"])
def stats():
    if request.method == "POST":
        print(request)
        return render_template("landing.html")
    if request.method == "GET":
        print(request)


if __name__ == "__main__":
    app.run(debug=True)
