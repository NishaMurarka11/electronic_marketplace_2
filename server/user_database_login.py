#!/usr/bin/python3
import json
import pickle
import os
from grpc_client import  GRPCClient
import traceback

error_code = -1
customerdb = os.getenv("customerdb") or "localhost"
class user():
    
    def create_user(user_name, password):
        try :
            exists = GRPCClient.exists(customerdb,user_name)   
            if exists == "0":
                user_id = GRPCClient.get(customerdb,"User_ID")
                print("user_id ", user_id)
                data = {'user_id' : user_id , 'password' :password}
                GRPCClient.set(customerdb,user_name,str(data))
                val = int(user_id) + 1
                GRPCClient.set(customerdb,"User_ID", str(val))
                return (user_id,"Ok")
            else :
                return (error_code,"Username already exists")
        except Exception as e:
            traceback.print_exc()
            return (error_code,"Error has occured "+str(e))
        
    def login_user(user_name, password):
        try :
            exists = GRPCClient.exists(customerdb,user_name)
            if exists == "0":
                return "No such user"
            else :
                val = GRPCClient.get(customerdb,user_name)
                val = val.replace("\'", "\"")
                val = json.loads(val)
                print(val)
                if val['password'] == password:
                    GRPCClient.set(customerdb,val['user_id'],"True")
                    return (val['user_id'],"Ok")
                else :
                    return (error_code,"Incorrect Password")
        except Exception as e:
            traceback.print_exc()
            return (error_code,"Error has occured" +str(e))
        
    def logout(user_id):
        try:
            exists = GRPCClient.exists(customerdb,user_id)
            if exists == "1":
                GRPCClient.delete(customerdb,user_id)
                return (user_id,"Ok")
            else:
                return (error_code,"no such user")
        except Exception as e:
            return (error_code,"Error has occured" +str(e))
    
    def validate_user(user_id):
        try:
            exists = GRPCClient.exists(customerdb,user_id)
            if exists == "0":
                return False
            else :
                return True
        except Exception as e:
            print (str(e))
            return False
        
        
