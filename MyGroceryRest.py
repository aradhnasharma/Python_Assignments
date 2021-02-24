from flask import Flask, request
from flask_restful import reqparse, Api, Resource, abort

app = Flask(__name__)
api = Api(app)

vegdata = [ {  "vegname" : "Tomato",
				"qty" : "20",
				},
				{
				"vegname" : "Potato",
				"qty" : "10",
				},
				{
				"vegname" : "Onion",
				"qty" : "50",
				},
				{
				"vegname" : "Carrot",
				"qty" : "25",
				},]
         

#First endpoint
class VegList(Resource):
    def get(self):
        #return vegdata    
        return vegdata
        
    def post(self):
        vegdict = {}
        vegdict["vegname"] = request.json["vegname"]
        vegdict["qty"] = request.json["qty"]
        vegdata.append(vegdict)
        return request.json 
		
#Second endpoint
class VegNameList(Resource):
    def get(self, vegname):      
        for x in vegdata:
            if vegname == x['vegname']:
                return x
        else:
            abort(404, message=f"{vegname} does not exist in list ")   

    def delete(self, vegname):
        for x,listItem in enumerate(vegdata):
            if vegname == listItem["vegname"]:
                vegdata.pop(x)
                return vegname + " Deleted"
        else:
            abort(404, message=f"{vegname} does not exist in list ")
    def put(self, vegname):
        for x, listItem in enumerate(vegdata):
            if vegname == listItem['vegname']:
                Itemdict=request.get_json()
                listItem['qty'] = Itemdict.get('qty')
                return vegname + ' got Updated' +' with '+ Itemdict.get('qty')
        else:
            abort(404, message=f"{vegname} does not exist in list")     
            
api.add_resource(VegList, '/vegetables')
api.add_resource(VegNameList, '/vegetables/<string:vegname>')