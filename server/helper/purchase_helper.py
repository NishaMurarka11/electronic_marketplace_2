#!/usr/bin/python3
import imp
from product import inventory
from unittest import result

"""
This class acts as a helper class for

- Making the payment
- Updating the inventory on successfull purchase
- Storing the transaction in the DB
- Get purchases for Feedback
- Post Feedback per item

"""

class PurchaseHelper():

	def __init__(self):
		pass
    
	def getTotalPurchaseAmount(data):
		amount=0
		print("Cart Data",data)

		for k,v in data.items():
			print("K: {} v: {}".format(k,v))
			item_id = k
			qty  = v
			price_item = 10
			price = price_item*int(qty)
			amount+= price
		return amount


	def make_payment(data):
		print("Data",data)
		return "TRUE"


	def updateInventory(data):
		print("Update Inventory  by decreasing the qty as : ",data)
		for k,v in data.items():
			print("K: {} v: {}".format(k,v))
			item_id = k
			qty  = int(v)
			product_db = inventory()
			response = product_db.decrement_item_qty_by_itemId(item_id,qty)
			print("Response : {}".format(response))
		db_state = product_db.diplayDB()	
		print("Updated DB - {}".format(db_state))

	def createTransaction(buyer_id,data):
		print("Creating Transaction for buyer_id {} for Items : {}".format(buyer_id,data))
		trxns = []
		product_db = inventory()
		for k,v in data.items():
			trxn = {}
			print("K: {} v: {}".format(k,v))
			item_id = k
			qty  = v
			code, item = product_db.get_item_by_id(item_id)
			print("Item found ",item)
			trxn["buyer_id"] = buyer_id
			trxn["item_id"] = item["item_id"]
			trxn["seller_id"] = item["seller_id"]
			trxn["quantity"] = item["quantity"]
			trxn["feedback"] ="-1" 
			trxns.append(trxn)
		product_db.save_trxn(trxns)
		return trxns


	def getItemsForFeedback(buyer_id):
		product_db = inventory()
		code,data = product_db.getItemsForFeedback(buyer_id)
		print("Items With feedback pending ", data)
		return code,data

	def postFeedback(buyer_id, item_id, feedback):
		product_db = inventory()
		code,trxns = product_db.postFeedback(buyer_id,item_id,feedback)
		print("Feedback Succesfully Submitted")
		return code,trxns











