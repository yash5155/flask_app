import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))

# Database
db = client["student_db"]

# Collection
collection = db["students"]


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():

    try:
        name = request.form["name"]
        email = request.form["email"]

        collection.insert_one({"name": name, "email": email})

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("form.html", error=str(e))


@app.route("/success")
def success():
    return render_template("success.html")


# API to get all students
@app.route("/api/students")
def get_students():

    students = []

    for student in collection.find({}, {"_id": 0}):
        students.append(student)

    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)
