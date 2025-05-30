from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")  # Get the message from the request

    if not text:
        return jsonify({"error": "Invalid input"}), 400  # Return an error if no message is provided

    response = get_response(text)  # Call the chatbot response function
    message = {"answer": response}  # Create a dictionary with the response
    return jsonify(message)  # Return the response as JSON

if __name__ == "__main__":
    app.run(debug=True)



