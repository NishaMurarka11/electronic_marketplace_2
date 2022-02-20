#!/usr/bin/python3
from ast import Pass
import redis
import json
import pickle
import traceback


# r = redis.Redis(host='localhost', port=6379, db=1)

# r.set('crack', 'code') # True
# value = r.get('crack')
# print(value) # b'world'

class inventory():
    inv = None
    __instance = None
    item_id = 0
    redisDB=None
    
    @staticmethod
    def get_db_instance():
        if inventory.__instance == None:
            inventory()
            print("initializing the inventory")
            
            try:
                inventory.__instance.redisDB = redis.Redis(host='localhost', port=6379)
                if not inventory.__instance.redisDB.exists("productDB"):
                    inventory.__instance.inv = {'items':[]}
                    data = pickle.dumps(inventory.__instance.inv)
                    inventory.__instance.redisDB.set("productDB", data)
                print("initialized DB",pickle.loads(inventory.__instance.redisDB.get("productDB")))
            except Exception as e:
                print("Error in ProductDB",e)
        return inventory.__instance
    
    def __init__(self) -> None:
        if inventory.__instance != None:
            raise Exception("This is a singleton class")
        else:
            inventory.__instance = self
    
    def get_item_id(self):
        print("get item called")
        val = self.item_id
        self.item_id = val + 1
        return val
    
    def put_item(self, items,seller_id):
        print("\nPut item function called for items {}".format(items))
        #generate ID
        #Keep number for each category
        # check if item is already there. 
        item_ids = []
        data = pickle.loads(inventory.__instance.redisDB.get("productDB"))
        print("\nCurrent State of DB {}".format(data))
        try:
            for item in items:
                flag = 0
                item["seller_id"] = seller_id
                # result = self.redisDB.hgetall("productDB")
                # result = json.loads(self.redisDB.hgetall("productDB"))
                # self.inv = result
                item_lst = data["items"]
                print("Item List : ",item_lst)
                # item_lst = self.inv["items"]
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

        data['items'] = item_lst
        self.redisDB.set("productDB",  pickle.dumps(data))
        return (item_ids)
    
    def search_item(self,category_id,keyword):
        data = pickle.loads(inventory.__instance.redisDB.get("productDB"))
        item_lst = data["items"]
        print("Inside Repository")
        # item_lst = self.inv["items"]
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
        except Exception as e:
            traceback.print_exc()
        print("Item found {}".format(search_items))
        return search_items
        
    def update_item(self,item_id,key,value):
        print("Update Item")
        print("REDIS ",inventory.__instance.redisDB.get("productDB"))
        data = pickle.loads(inventory.__instance.redisDB.get("productDB"))
        print("data",data)
        item_lst = data['items']
        print("*****DB before update", item_lst)
        # item_lst = self.inv["items"]
        flag = 0
        for item in item_lst:
            if item["item_id"] == item_id:
                item[key] = value
                flag = 1
                break
        if flag == 1:
            # self.inv["items"] = item_lst
            data["items"] = item_lst
            inventory.__instance.redisDB.set("productDB", pickle.dumps(data))
            print("****DB After update", item_lst)
            return "Updated "+str(item_id)+" "+str(key)+" to "+str(value)
        else: 
            return "No such item item found."
        
        
    def get_item_by_seller_id(self,seller_id):
        data = pickle.loads(inventory.__instance.redisDB.get("productDB"))
        item_lst = data["items"]
        item_by_seller = []
        # item_lst = self.inv["items"]
        for item in item_lst:
            if item["seller_id"] == seller_id :
                item_by_seller.append(item)
        return item_by_seller

    