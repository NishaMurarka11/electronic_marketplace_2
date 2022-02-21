#!/usr/bin/python3
import json
import pickle
import traceback
import grpc_client
from grpc_client import GRPCClient

SUCCESS_CODE = 1
ERROR_CODE = -1
class inventory():
    item_id = 0
    def __init__(self) -> None:
        pass    

    def initializeDB(self):
        response = GRPCClient.exists("productDB")
        if(response == "0"):
            data_instance = {'items':[]}
            GRPCClient.set("productDB",str(data_instance))
            
    def get_item_id(self):
        print("get item called")
        val = self.item_id
        self.item_id = val + 1
        return val

    def put_item(self, items,seller_id):
        print("\nPut item function called for items {}".format(items))
        self.initializeDB()   
        # check if item is already there. 
        item_ids = []
        data  =  GRPCClient.get("productDB")
        data = data.replace("\'", "\"")
        data = json.loads(data)
        # data = pickle.loads(inventory.__instance.redisDB.get("productDB"))
        print("\nCurrent State of DB {}".format(data))
        try:
            for item in items:
                flag = 0
                item["seller_id"] = seller_id
                item_lst = data["items"]
                print("Item List : ",item_lst)
                #Check if the item already exists. If yes update the item. 
                for db_item in item_lst:
                    if item["name"] == db_item["name"] and \
                        item["category_id"] ==  db_item["category_id"] and \
                        item["seller_id"] == db_item["seller_id"] : 
                            print("Item already exists")
                            item['item_id'] = db_item['item_id']
                            item_lst.remove(db_item)
                            item_lst.append(item)
                            item_ids.append(item['item_id'])
                            flag = 1
                            break
                if flag == 0:
                    item_id = self.get_item_id()
                    item['item_id'] = item_id
                    item_ids.append(item_id)
                    print("Item Id recieved "+str(item_id))
                    item_lst.append(item)
        except Exception as err:
            traceback.print_exc()
            return (ERROR_CODE, str(err))

        data['items'] = item_lst
        GRPCClient.set("productDB",  str(data))
        return (SUCCESS_CODE,item_ids)


    
    def search_item(self,category_id,keyword):
        self.initializeDB()
        data = GRPCClient.get("productDB")
        data = data.replace("\'", "\"")
        data = json.loads(data)
        item_lst = data["items"]
        print("ITEM LIST",item_lst)
        search_items = []
        try:
            for item in item_lst:
                print("Searching for item category Id {} keyword {}".format(category_id,keyword))
                if item["category_id"] == category_id:
                    item_keywords = item["keywords"]
                    for value in keyword:
                        if value in item_keywords:
                            search_items.append(item)
                            break
        except Exception as err:
            traceback.print_exc()
            return (ERROR_CODE, str(err))
        print("Item found {}".format(search_items))
        return search_items


        
    def update_item(self,item_id,key,value):
        self.initializeDB()
        print("Update Item")
        data = json.loads(GRPCClient.get("productDB").replace("\'", "\""))
        print("data",data)
        item_lst = data['items']
        print("*****DB before update", item_lst)
        flag = 0
        for item in item_lst:
            if item["item_id"] == item_id:
                item[key] = value
                flag = 1
                break
        if flag == 1:
            data["items"] = item_lst
            GRPCClient.set("productDB", str(data))
            print("****DB After update", item_lst)
            ret = "Updated "+str(item_id)+" "+str(key)+" to "+str(value)
            return (SUCCESS_CODE,ret)
        else: 
            return "No such item item found."
        
        
    def get_item_by_seller_id(self,seller_id):

        data = json.loads(GRPCClient.get("productDB").replace("\'", "\""))
        item_lst = data["items"]
        item_by_seller = []
        # item_lst = self.inv["items"]
        for item in item_lst:
            if item["seller_id"] == seller_id :
                #print("Item found "+str(item))
                item_by_seller.append(item)
        return (SUCCESS_CODE,item_by_seller)

    