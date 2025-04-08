from flask import Flask
from flask_cors import CORS, cross_origin
import requests
import json
from service import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return test()
                                                                                                                                                                                    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)