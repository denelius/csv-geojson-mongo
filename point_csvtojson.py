import csv
import ast
import pymongo
from geojson import Point, Feature, dump, FeatureCollection

# myclient = pymongo.MongoClient("mongodb://cv:cv_b00gingrip@ds147033.mlab.com:47033/cristian")
myclient = pymongo.MongoClient("mongodb://<user>:<password>@ds152000.mlab.com:52000/<client>")
mydb = myclient["<client>"]
mycol = mydb["<database>"]

pointfeatures = []
with open('pointdemo.csv', 'r') as f:
    next(f) #ignore headers line - start on second line
    reader = csv.reader(f)
    for row in reader:
        coords = ast.literal_eval(row[3])
        point = Point(coords)      
        pointjson = Feature(name="cv"+row[0], geometry=point, style={"color": "#ff46b5"}, properties={"direction":row[1], "status":row[2]})
        # x = mycol.insert_one(pointjson)
        pointfeatures.append(pointjson)

feature_collection = FeatureCollection(pointfeatures)


# # populate file to confirm content 
with open('point.geojson', 'w') as f:
#    dump(pointjson, f)
   dump(feature_collection, f)