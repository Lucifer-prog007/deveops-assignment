from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import json
import certifi

app = Flask(__name__)

# MongoDB Connection
client = MongoClient(
    "mongodb+srv://Ayush:ideal909@cluster0.sg4hsku.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=certifi.where()
)

db = client["studentdb"]
collection = db["students"]

# API Route
@app.route('/api')
def api():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

# Form Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return "Todo Item Saved Successfully"

# Submit Form
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        result = collection.insert_one({
            "name": name,
            "email": email
        })

        print("Inserted ID:", result.inserted_id)

        return redirect(url_for('success'))

    except Exception as e:
        return str(e)

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)