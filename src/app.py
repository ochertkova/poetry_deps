from distutils.log import error
import os
from flask import Flask, render_template

import store

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", deps=store.get_dep_names())


@app.route("/<name>")
def dep_info(name):
    dep_in_store = store.find_dep_by_name(name)
    return render_template("dependency.html", dep_to_render=dep_in_store)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=port)
