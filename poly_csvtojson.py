import csv
import ast
import pymongo
from geojson import Polygon, Feature, dump

myclient = pymongo.MongoClient("mongodb://<user>:<password>@ds152000.mlab.com:52000/<client>")
mydb = myclient["<client>"]
mycol = mydb["<database>"]

polyjson = ""
with open('polydemo.csv', 'r') as f:
    next(f) #ignore headers line - start on second line
    reader = csv.reader(f)
    for row in reader:
        coords = ast.literal_eval(row[3])
        poly = Polygon(coords)    
        polyjson = Feature(name="cv"+row[0], geometry=poly, style={"color": "#ff46b5", "weight": 10,"opacity": 0.85}, properties={"direction":row[1], "status":row[2]})
        # x = mycol.insert_one(polyjson)

# populate file to confirm content 
with open('poly.geojson', 'w') as f:
   dump(polyjson, f)