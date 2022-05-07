from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello World")

if __name__ == "__main__":
    app.run(port=6007, debug=True)