


# Challenge Exercises
# 1
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/Classfiles/zmiller/Esri Press/Python/Data/Exercise06"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    fcdescribe = arcpy.Describe(fc)
    a =  fcdescribe.name + '  '+  'is a'
    b = '  '+ fcdescribe.shapeType +' '+  'feature class'
    print (a+b)


# 2
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/Classfiles/zmiller/Esri Press/Python/Data/Exercise06"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    fcdescribe = arcpy.Describe(fc)
    if fcdescribe.shapeType == "Polygon":
     print fcdescribe
      
