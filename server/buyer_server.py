#!/usr/bin/python3
from unittest import result
from flask import Flask, request, Response
from product import inventory
from shopping_cart import shopping_cart
import socket 
import json
import pickle
import jsonpickle

app = Flask(__name__)
class client_server():


# Validate buyer ID before cart api calls. 
    
    def __init__(self):
        host='127.0.0.1'
        port=1500
        app.run(host=host, port=port, debug=True)
        
    @app.route('/api/createLogin', methods=['POST'])
    def create_login():
        data = request.get_json()
        username = data['user_name']
        password = data['password']
        response = {'response' : 123}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")
    
    @app.route('/api/Login',methods=['POST'])
    def login():
        data = request.get_json()
        username = data['user_name']
        password = data['password']
        # Check if username and password exists 
        response = {'response' : "logged in"}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")
    
    @app.route('/api/searchItem', methods=['GET'])
    def search_item():
        data = request.get_json()
        category_id = data['category_id']
        keywords = data['keywords']
        product_db = inventory.get_db_instance()
        result = product_db.search_item(category_id,keywords)
        response = {'response' : result}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")
    
    @app.route('/api/addItem', methods=['POST'])
    def add_item():
        data = request.get_json()
        buyer_id = data['buyer_id']
        item_id = data['item_id']
        quantity = data['quantity']
        cart = shopping_cart.get_db_instance()
        result =  cart.add_item(buyer_id,item_id,quantity)
        response = {'response' : result}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")
        
    
    @app.route('/api/removeItem', methods=['POST'])
    def remove_item():
        data = request.get_json()
        buyer_id = data['buyer_id']
        item_id = data['item_id']
        quantity = data['quantity']
        cart = shopping_cart.get_db_instance()
        result = cart.remove_item(buyer_id,item_id,quantity)
        response = {'response' : result}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")
    
    @app.route('/api/clearCart', methods=['GET'])
    def clear_cart():
        data = request.get_json()
        buyer_id = data['buyer_id']
        cart = shopping_cart.get_db_instance()
        result =  cart.clear_cart(buyer_id)
        response = {'response' : result}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")
    
    @app.route('/api/displayCart', methods=['GET'])
    def display_cart():
        data = request.get_json()
        buyer_id = data['buyer_id']
        cart = shopping_cart.get_db_instance()
        result = cart.display_cart(buyer_id)
        response = {'response' : result}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")    
    
    @app.route('/api/printDB', methods=['GET'])
    def printDB():
        product_db = inventory.get_db_instance()
        redisDB = product_db.redisDB
        result = pickle.loads(product_db.redisDB.get("productDB"))
        response = {'response' : result}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")  
        
    @app.route('/api/logout', methods=['GET'])
    def logout():
        response = { 'response' : "OK"}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")

  
  
if __name__=="__main__":
    print("Starting Buyer Server !!")
    c = client_server()
    print("Buyer Server is UP !!")

                