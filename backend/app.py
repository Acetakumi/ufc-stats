from flask import Flask
import requests
import json
from service import *

def fetch(url):
    return json.loads(requests.get(url).content)



app = Flask(__name__)

@app.route("/nigger")
def index():
    rankings = fetch("https://api.octagon-api.com/rankings")
    return buildFighter()
    
                                                                                                                                                                                    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)


"""
[
    {
        "division": "name",
        [
            fighter: {
                "name": 'anme',
                'ranking': 1,
            },
            
            fighter: {
                "name": 'anme',
                'ranking': 1,
            }
        ]
    },
    {
        "division": "name",
        [
            fighter: {
                "name": 'anme',
                'ranking': 1,
            }
        ]
    }
]
"""
    