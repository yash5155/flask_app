# Import os module
import os

# Load environment variables
from dotenv import load_dotenv

# Import Flask utilities
from flask import Flask, jsonify, redirect, render_template, request, url_for

# Import MongoDB client
from pymongo import MongoClient

# Load .env file
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))

# Select database
db = client["student_db"]

# Select collection
collection = db["students"]


# Home page
@app.route("/")
def home():
    return render_template("form.html")


# Form submission
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]  # Read name
        email = request.form["email"]  # Read email
        collection.insert_one({"name": name, "email": email})  # Insert record
        return redirect(url_for("success"))  # Redirect on success
    except Exception as e:
        return render_template("form.html", error=str(e))  # Show error


# Success page
@app.route("/success")
def success():
    return render_template("success.html")


# API to return all students
@app.route("/api/students")
def get_students():
    students = []
    for student in collection.find({}, {"_id": 0}):
        students.append(student)
    return jsonify(students)


# Start server
if __name__ == "__main__":
    app.run(debug=True)
