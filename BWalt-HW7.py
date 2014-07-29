#Exercise 8
#Challenge 1
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise08"
fc = "results/square.shp"
arcpy.CreateFeatureclass_management("U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise08", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
coordlist =[[0, 0], [0, 1000], [1000, 1000], [1000, 0]]
for x, y in coordlist:
    point = arcpy.Point(x,y)
    array.append(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor


# Challenge 2 
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise08"
fc = "Hawaii.shp"
newfc = "Results/Hawaii_2.shp"
arcpy.MultipartToSinglepart_management(fc, newfc)
spatialref = arcpy.Describe(newfc).spatialReference
unit = spatialref.linearUnitName
cursor = arcpy.da.SearchCursor(newfc, ["SHAPE@"])
for row in cursor:
    print ("{0} square {1}".format(row[0].area, unit))


#Challenge 3
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])Exercise 10


#Exercise 10
#challenge 1
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise10/Austin_TX.mxd"
mxd = arcpy.mapping.MapDocument("U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise10/Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Parks")[0]
lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
dflist = arcpy.mapping.ListDataFrames(mxd)
for dframe in dflist:
    if dframe.name <> "Parks":
        arcpy.mapping.AddLayer(dframe, lyr)
mxd.save()
del mxd
