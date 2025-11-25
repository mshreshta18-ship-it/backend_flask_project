from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return "Backend is running successfully!"

@app.route("/save-text", methods=["POST"])
def save_text():
    body = request.json
    text = body.get("text")
    data = load_data()
    data["saved_text"] = text
    save_data(data)
    return jsonify({"message": "Text saved successfully!"})

@app.route("/get-text", methods=["GET"])
def get_text():
    data = load_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
