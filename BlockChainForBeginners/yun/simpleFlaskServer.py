from flask import Flask
from flask import request

#code which helps initialize our server
app = flask.Flask(__name__)

#defining a /hello route for only post requests
@app.route('/hello', methods=['POST'])
def index():
    #grabs the data tagged as 'name'
    name = request.get_json()['name']
    
    #sending a hello back to the requester
return "Hello " + name
