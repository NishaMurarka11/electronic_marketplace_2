#!/usr/bin/python3
from re import S
import requests
import json
from subprocess import call
from unicodedata import category 
import pickle
import time



HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1500      # The port used by the server
addr = f"http://{HOST}:{PORT}"

def search_item(category_id,keywords):
    print("\nBuyer Client :: /Search Items")
    data = {'category_id':category_id,'keywords':keywords}
    url = addr+"/api/searchItem"
    response = call_buyer_sever(data,"get",url)
    print("\nSearch Item RESPONSE",response)
    return response
    
def add_item(buyer_id,item_id,quantity):
    data = {'buyer_id':buyer_id,'item_id':item_id,'quantity':quantity}
    url = addr+"/api/addItem"
    return call_buyer_sever(data,"post",url)
    
    
def remove_item(buyer_id,item_id,quantity): 
    data = {'buyer_id':buyer_id,'item_id':item_id,'quantity':quantity} 
    url = addr+"/api/removeItem"
    return call_buyer_sever(data,"post",url)
    
def clear_cart(buyer_id):
    data = {'buyer_id':buyer_id}
    url = addr+"/api/clearCart"
    return call_buyer_sever(data,"get",url)
    
    
def display_cart(buyer_id):
    print("\nDisplay Cart for Buyer Id {}".format(buyer_id))
    data = {'operation':'display_cart','buyer_id':buyer_id}
    url = addr+"/api/displayCart"
    return call_buyer_sever(data,"get",url)

def display_all_items():
    data = {'operation':'display_all_items'}
    url = addr+"/api/printDB"
    return call_buyer_sever(data,"get",url)

def call_buyer_sever(data,operation,url):
    data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    if operation == "post":
        response = requests.post(url, data=data,headers=headers)
        return json.loads(data)
    else:
        response = requests.get(url, data=data,headers=headers)
        return json.loads(data)

def main():
    # display_all_items()
    buyer_id = "123"
    items = search_item(0,["stationary","Pen"])
    
    print(add_item(buyer_id,0,"3"))

    print(remove_item(buyer_id,0,"2"))

    print(display_cart(buyer_id))

    print(clear_cart(buyer_id))


if __name__=="__main__":
    main()
