from flask import Flask, render_template, request, jsonify
from lexer import analyze_code

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    code = data.get("code", "")

    tokens = analyze_code(code)

    return jsonify(tokens)


if __name__ == "__main__":
    app.run(debug=True)