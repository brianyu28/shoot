import os

from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "foo"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
