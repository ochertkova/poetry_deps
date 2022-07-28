from distutils.log import error
import os
from flask import *

import store

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", deps=store.get_dep_names())

@app.route("/<name>")
def dep_info(name):
    try:
        dep_in_store = store.find_dep_by_name(name)
        print("dep in store found")
        print(dep_in_store)
        #print(dep_in_store.keys())
        return render_template("dependency.html", dep_to_render=dep_in_store)
    except:
        abort(404)
    
    #return render_template("dependency.html", dep=store.find_dep_by_name(name))

    #return "The product is " + ", ".join(store.find_dep_by_name(name).keys())

if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,port=port)
