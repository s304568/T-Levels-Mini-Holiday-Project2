from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

names = {
    'Alex': {'first-name': 'Alex', 'surname': 'Bowker', 'age': 22}
    
}

animals = {
    "Joe": [{"name": "Joe", "age": 1, "type": "dog"}],
    "Sam": [
        {"name": "Sam", "age": 2, "type": "fish"},
        {"name": "Sam", "age": 4, "type": "apple"},
    ],
    "Dub": [{"name": "Dub", "age": 3, "type": "horse"}],
    "Andrew": [{"name": "Andrew", "age": 5, "type": "shark"}],
}

staff = {
    'staff': [
        {'firstName': 'Alex', 'surname': 'Bowker', 'age': 22},
        {'firstName': 'Nic', 'surname': 'Grigore', 'age': 23},
        {'firstName': 'Barry', 'surname': 'Brown', 'age': 26},
        {'firstName': 'Allan', 'surname': 'Duggan', 'age': 72},
        {'firstName': 'Mo', 'surname': 'Abdul', 'age': 35}
    ]
}

@app.route("/members")
def members():
    return{"members": ["Member1", "Member2", "Member3"]}

@app.route('/names', methods = ["GET"])
def get_name():
    return jsonify(names)


@app.route('/animals', methods=["GET"])
def get_animals():
    requested_animal = request.args.get("animal")
    result = []

    if requested_animal in animals:
        result = animals[requested_animal]

    if not result:
        return jsonify([]), 400

    return jsonify(result)

@app.route('/staff', methods=['GET'])
def get_staff():
    return jsonify(staff)

if __name__ == "__main__":
    app.run(debug=True)