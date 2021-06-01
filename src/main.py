import os

from flask import Flask
from multiprocessing import Process

from src.utils.heavy import heavy_func

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/heavy")
def heavy():
    heavy_process = Process(
        target=heavy_func,
        daemon=True
    )
    heavy_process.start()
    return "heavy"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))