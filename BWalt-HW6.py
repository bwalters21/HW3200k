#Exercise 7
# Challenge 1
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise07"
fc = "airports.shp"
seaplane = 'Seaplane Base'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" =\'Seaplane Base\'')
for row in cursor:
    arcpy.Buffer_analysis(cursor, r'U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise07/airports.shp", "15000 meters")
    
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise07"
fc = "airports.shp"
airport = 'airports'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" =\'airports\'')
for row in cursor:
    arcpy.Buffer_analysis(cursor, r"U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise07/airports.shp", "7500 meters")


#Challenge 2
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1]= "NO"
    cursor.updateRow(row)
