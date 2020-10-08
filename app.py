from flask import Flask,request,Response
import pymongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

# app.config["MONGO_URI"] = "mongodb+srv://greendeck:gZ1oKEGx2HGdw7u8@cluster0.j6eb6.mongodb.net/myDatabase?retryWrites=true&w=majority"


print("************* SERVER STARTED ******************")

mongo = pymongo.MongoClient("mongodb+srv://greendeck:gZ1oKEGx2HGdw7u8@cluster0.j6eb6.mongodb.net/myDatabase?retryWrites=true&w=majority")
db = mongo.test


# greendeck
# gZ1oKEGx2HGdw7u8

##sending data to server 

# with open('Greendeck SE Assignment Task 1 .json') as file: 
#     file_data = json.load(file)


# if isinstance(file_data, list): 
#     mongo.db.data.insert_many(file_data)   
# else: 
#     mongo.db.data.insert_one(file_data) 

#**********************************************************************************************************************
# get all products
@app.route('/api/v1.0/products/', methods=['GET'])
def get_products():
	try:
		star = mongo.db.data
		output = []
		for s in star.find():
			output.append({'name' : s['name'], 'brand_name' : s['brand_name'],'regular_price_value' : s['regular_price_value'],'offer_price_value' : s['offer_price_value'],'currency' : s['currency'],'classification_l1' : s['classification_l1'],'classification_l2' : s['classification_l2'],'classification_l3' : s['classification_l3'],'classification_l4' : s['classification_l4'],'image_url' : s['image_url'],})
		return Response(response= json.dumps({'result' : output}),
			status=200,
			mimetype="application/json")
	except Exception as ex:
		print("***********")
		print(ex)
		print("***********")
		return Response(response= json.dumps({"message":"Error occured"}),
			status=500,
			mimetype="application/json")

#**********************************************************************************************************************
# get product by id
@app.route('/api/v1.0/product/<id>', methods=['GET'])
def product_by_id(id):
	try:
		s =mongo.db.data.find_one({"_id":ObjectId(id)})
		return Response(
			response=json.dumps(
					{"message":{'name' : s['name'], 'brand_name' : s['brand_name'],'regular_price_value' : s['regular_price_value'],'offer_price_value' : s['offer_price_value'],'currency' : s['currency'],'classification_l1' : s['classification_l1'],'classification_l2' : s['classification_l2'],'classification_l3' : s['classification_l3'],'classification_l4' : s['classification_l4'],'image_url' : s['image_url']}}),
					status=200,
					mimetype="application/json"
					
			)
	except Exception as ex:
		print("***********")
		print(ex)
		print("***********")
		return Response(response= json.dumps({"message":"sorry could not find product"}),
			status=500,
			mimetype="application/json")

#**********************************************************************************************************************
#get products by arguments
@app.route('/api/v1.0/product/', methods=['GET'])
def get_required_products():
	star = mongo.db.data
	arguments={}

	if 'name' in request.args:
		arguments['name'] = request.args['name']

	if 'classification_l1' in request.args:
		arguments['classification_l1'] = request.args['classification_l1']
    
	if 'classification_l2' in request.args:
		arguments['classification_l2'] = request.args['classification_l2']

	if 'classification_l3' in request.args:
		arguments['classification_l3'] = request.args['classification_l3']

	if 'classification_l4' in request.args:
		arguments['classification_l4']  = request.args['classification_l4']

	if 'currency' in request.args:
		arguments['currency']  = request.args['currency']

	if 'brand_name' in request.args:
		arguments['brand_name'] = request.args['brand_name']

	output = []
	try:
		if (len(arguments)!=0):
			for s in star.find(arguments):
				output.append({'name' : s['name'], 'brand_name' : s['brand_name'],'regular_price_value' : s['regular_price_value'],'offer_price_value' : s['offer_price_value'],'currency' : s['currency'],'classification_l1' : s['classification_l1'],'classification_l2' : s['classification_l2'],'classification_l3' : s['classification_l3'],'classification_l4' : s['classification_l4'],'image_url' : s['image_url']})
			print(len(output))
			return Response(
				response =json.dumps({'result' : output}),
				status=200,
				mimetype="application/json")
		else:
			return Response(
				response=json.dumps(
						{"message":"Enter atleast one attribute"}),
						status=500,
						mimetype="application/json")
	except Exception as ex:
		print("***********")
		print(ex)
		print("***********")
		return Response(response= json.dumps({"message":"sorry could not find product"}),
		status=500,
		mimetype="application/json")

#**********************************************************************************************************************
#add products
@app.route('/api/v1.0/product_add/', methods=['POST'])
def add_star():
	try:
		star = mongo.db.data
		star_id = star.insert(request.json)
		s = star.find_one({'_id': star_id })
		output = {'name' : s['name'], 'brand_name' : s['brand_name'],'regular_price_value' : s['regular_price_value'],'offer_price_value' : s['offer_price_value'],'currency' : s['currency'],'classification_l1' : s['classification_l1'],'classification_l2' : s['classification_l2'],'classification_l3' : s['classification_l3'],'classification_l4' : s['classification_l4'],'image_url' : s['image_url']}
		return Response(
			response =json.dumps(
				{'message':'product added',
				'id':f'{star_id}',
				'result' : output}),
			status=200,
			mimetype="application/json"
			)
	except Exception as ex:
		print("***********")
		print(ex)
		print("***********")
		return Response(response= json.dumps({"message":"sorry could not add product"}),
		status=500,
		mimetype="application/json")

#**********************************************************************************************************************
#delete product

@app.route('/api/v1.0/product_delete/<id>', methods=['DELETE'])
def delete_product(id):
	try:
		dbResponse =mongo.db.data.delete_one({"_id":ObjectId(id)})
		if dbResponse.deleted_count == 1:
			return Response(
				response =json.dumps({"message":"product deleted","id":f"{id}"}),
				status=200,
				mimetype="application/json"
				)
		else:
			return Response(
				response =json.dumps({"message":"product not found","id":f"{id}"}),
				status=200,
				mimetype="application/json"
				)

	except Exception as ex:
		print("***********")
		print(ex)
		print("***********")
		return Response(response= json.dumps({"message":"sorry cannot delete product"}),
		status=500,
		mimetype="application/json")


#**********************************************************************************************************************
#update product
@app.route("/api/v1.0/product_update/<id>", methods=["PATCH"])
def update_product(id):

	arguments_1={}

	if 'name' in request.form:
		arguments_1['name'] = request.form['name']

	if 'classification_l1' in request.form:
		arguments_1['classification_l1'] = request.form['classification_l1']
    
	if 'classification_l2' in request.form:
		arguments_1['classification_l2'] = request.args['classification_l2']

	if 'classification_l3' in request.form:
		arguments_1['classification_l3'] = request.form['classification_l3']

	if 'classification_l4' in request.form:
		arguments_1['classification_l4']  = request.form['classification_l4']
	
	if 'regular_price_value' in request.form:
		arguments_1['regular_price_value']  = request.form['regular_price_value']
	
	if 'offer_price_value' in request.form:
		arguments_1['offer_price_value']  = request.form['offer_price_value']
	
	if 'currency' in request.form:
		arguments_1['currency']  = request.form['currency']
	
	if 'brand_name' in request.args:
		arguments_1['brand_name'] = request.args['brand_name']

	try:
		if (len(arguments_1)!=0):
			dbResponse = mongo.db.data.update_one(
				{"_id":ObjectId(id)},
				{"$set":arguments_1}
			)
			if dbResponse.modified_count == 1:
				return Response(
					response=json.dumps({"message":"product updated"}),
					status=200,
					mimetype="application/json"
				)
			else:
				return Response(
					response=json.dumps({"message":"nothing to update"}),
					status=200,
					mimetype="application/json"
				)
		else:
			return Response(
				response=json.dumps(
						{"message":"Enter atleast one attribute"}),
						status=500,
						mimetype="application/json"
						
				)
			
	except Exception as ex:
		print("*********************")
		print(ex)
		print("*********************")
		return Response(
			response=json.dumps(
					{"message":"sorry cannot update product"}),
					status=500,
					mimetype="application/json"
					
			)
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5000, debug = True)