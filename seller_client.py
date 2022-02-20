#!/usr/bin/python3
import requests
import json
import time


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1200      # The port used by the server
addr = f"http://{HOST}:{PORT}"

def put_item(seller_id,item):
    data = {'item':item,'seller_id':seller_id}
    url = addr+"/api/putItem"
    response = call_seller_sever(data,"post",url)
    return response

def update_price(seller_id,item_id,price):
    data = {'seller_id':seller_id,'item_id':item_id,'price':price}
    url = addr+"/api/updatePrice"
    call_seller_sever(data,"post",url)

def remove_item(seller_id,item_id,quantity):
    data = {'seller_id':seller_id,'item_id':item_id,'quantity':quantity}
    url = addr+"/api/removeItem"
    call_seller_sever(data,"post",url)
    
def display_item(seller_id): 
    data = {'seller_id':seller_id}
    url = addr+"/api/displayItem"
    response = call_seller_sever(data,"get",url)

def printProductDB():
    data = {'operation':'printDB'}
    url = addr+"/api/printDB"
    call_seller_sever(data,"get",url)


def call_seller_sever(data,operation,url):
    data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    if operation == "post":
        response = requests.post(url, data=data,headers=headers)
        print(str(response))
        #data = data.decode('utf-8')
        return json.loads(data)
    else:
        response = requests.get(url, data=data,headers=headers)
        #data = data.decode('utf-8')
        return json.loads(data)
    
def main():
    # item = [{"name":"Pen","category_id":0,"keywords":["pen","stationary","ink","pencil","school supplies"],"condition":"new","sale_price":2.5,'quantity':5},\
    #     {"name":"Pencil","category_id":0,"keywords":["pencil","stationary","ink","pencil","school supplies"],"condition":"new","sale_price":1,'quantity':10}]
    # # # During login api caller seller client will recieve seller_id
    seller_id = 123
    #item_ids = put_item(seller_id,item)

    # if (item_ids[0] == -1):
    #     print("Error")
    #     return 
    #update_price(seller_id,1,2)

    #remove_item(seller_id,0,3)

    printProductDB()

    display_item(seller_id)

  
if __name__=="__main__":
    main()

   



