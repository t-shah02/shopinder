from flask import Flask, send_from_directory
import json

STATIC_PATH = "../frontend/public"

app = Flask(__name__)


@app.route("/")
def base():
    return send_from_directory(STATIC_PATH, 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory(STATIC_PATH, path)

@app.route("/sample")
def sample():
    return {"status":"ok","desc":"sample"}


if __name__ == "__main__":
    app.run(debug=True)
