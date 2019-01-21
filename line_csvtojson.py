import csv
import ast
import pymongo
from geojson import LineString, Feature, dump

myclient = pymongo.MongoClient("mongodb://<user>:<password>@ds152000.mlab.com:52000/<client>")
mydb = myclient["<client>"]
mycol = mydb["<database>"]

linejson = ""
with open('linedemo.csv', 'r') as f:
    next(f) #ignore headers line - start on second line
    reader = csv.reader(f)
    for row in reader:
        coords = ast.literal_eval(row[3])
        line = LineString(coords)    
        linejson = Feature(name="cv"+row[0], geometry=line, style={"color": "#ff46b5", "weight": 10,"opacity": 0.85}, properties={"direction":row[1], "status":row[2]})
        # x = mycol.insert_one(linejson)

# populate file to confirm content 
with open('line.geojson', 'w') as f:
   dump(linejson, f)