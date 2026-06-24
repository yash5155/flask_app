import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "This is flask App"


@app.route("/api")
def get_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    return data


if __name__ == "__main__":
    app.run(debug=True)
