#!/usr/bin/python3
from genericpath import exists
import json
import pickle
from grpc_client import  GRPCClient

class user():
    
    def create_user(self, user_name, password):
        try :
            exists = GRPCClient.exists(user_name)   
            if exists == "0":
                user_id = GRPCClient.get("User_ID")
                data = {'user_id' : user_id, 'password' :password}
                GRPCClient.set(user_name,data)
                GRPCClient.set("User_ID",user_id+1)
                return ("user ID "+ str(user_id))
            else :
                return ("Username already exists")
        except Exception as e:
            return ("Error has occured "+str(e))
        
    def login_user(self, user_name, password):
        try :
            exists = GRPCClient.exists(user_name)
            if exists == "0":
                return "No such user"
            else :
                val = GRPCClient.get(user_name)
                if val['password'] == password:
                    GRPCClient.set(val['user_id'],1)
                    return ("Logged in"+str(val['user_id']))
                else :
                    return "Incorrect Password"
        except Exception as e:
            return ("Error has occured" +str(e))
        
    def logout(self,user_id):
        try:
            exists = GRPCClient.exists(user_id)
            if exists == "1":
                GRPCClient.delete(user_id)
        except Exception as e:
            return ("Error has occured" +str(e))
        
                    