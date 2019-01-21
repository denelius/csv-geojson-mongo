import csv
import ast
import pymongo
from geojson import LineString, Feature, dump

# myclient = pymongo.MongoClient("mongodb://cv:cv_b00gingrip@ds147033.mlab.com:47033/cristian")
myclient = pymongo.MongoClient("mongodb://denelius:mlab_b00gingrip@ds151008.mlab.com:51008/node_build")
mydb = myclient["node_build"]
mycol = mydb["crud_demo"]

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