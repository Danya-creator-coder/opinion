from flask import Flask, render_template, request

app = Flask(__name__)


votes = {
    "Flask": 0,
    "Django": 0,
    "FastAPI": 0
}

@app.route("/", methods=["GET", "POST"])
def index():
    global votes
    if request.method == "POST":
        framework = request.form.get("framework")
        if framework in votes:
            votes[framework] += 1


    return render_template("index.html", votes=votes)

if __name__ == "__main__":
    app.run(debug=True)