# Import the built-in json module to read JSON files
import json

# Import the Flask class from the flask package
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define the route for the home page ("/")
@app.route("/")
def home():
    # Return a simple text message when the home page is accessed
    return "This is flask App"


# Define the route for the API endpoint ("/api")
@app.route("/api")
def get_data():

    # Open the data.json file in read ("r") mode
    with open("data.json", "r") as file:
        # Read the JSON data from the file and convert it into a Python object
        # (list of dictionaries in this case)
        data = json.load(file)

    # Return the Python object as a JSON response
    # Flask automatically converts dictionaries/lists into JSON
    return data


# Check whether this file is being run directly
# If true, start the Flask development server
if __name__ == "__main__":
    # Run the Flask application in debug mode
    # debug=True automatically reloads the server when code changes
    # and provides detailed error messages during development
    app.run(debug=True)
