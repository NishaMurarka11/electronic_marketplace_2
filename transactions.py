#!/usr/bin/python3

from flask import Flask
from flask import request, jsonify
from flask.ext.cors import CORS
from suds.client import Client
import xmltodict

app = Flask(__name__)
cors = CORS(app)

@app.route("/make_transaction , methods=['POST'])
def make_transaction():
    data = request.get_json()
    name = data["name"]
    card_numeber = data["card_number"]
    expiration = data["expiration"]
	# Get SOAP Service via suds
	url = 'http://localhost/makeTransaction/?WSDL'
	client = Client(url)
	xml = client.service.makeTransaction(name,card_number,expiration))
	# Convert XML to dict
	res_dict = xmltodict.parse(xml)
	result = {}
	result['result'] = res_dict['PTT_DS']['DataAccess']
	# Convert dict to JSON
	return jsonify(**result)
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4000, debug=True)