#Exercise 5
#Challenge 1
#1.Tools: 
#   Add XY coordinates-
#      -required parameters are in_cover. The coverage containing points or polygon labels
#       whose x,y coordinates will become attributes in the PAT, or in the coverage containing nodes, to the NAT.
#      -Optional parameters- none
#   Dissolve-
#      -required parameters- input feature-The features to be aggregated.
#                           -out feature class-The feature class to be created that
#                           will contain the aggregated features.
#      -Optional parameters -dissolve_field-The field or fields on which to aggregate features.
#                       -statistics_fields- Value Table
#                       -multi_part- boolean
#                       -unsplit_lines- boolean-Controls how line features are dissolved.




#Challenge 2
import arcpy
from arcpy import env
env.workspace = "UU:/Shared/GIS/StuData/BPWALT9934/Python/Data/Python/Data/Exercise05"
arcpy.AddXY_management("hospitals.shp")

#Challenge 3
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/BPWALT9934/Python/Data/Python/Data/Exercise05"
arcpy.Dissolve_management("parks.shp", "parks_dissolved.shp", "PARK_TYPE", "", "FALSE")



#Challenge 4
import arcpy
default = "no extensions"
if arcpy.CheckExtension("3D") == "Available":
    ext_3D = "3D Analyst "
else:
    ext_3D = ""
if arcpy.CheckExtension("Network") == "Available":
    ext_network = "Network Analyst "
else:
    ext_network = ""
if arcpy.CheckExtension("Spatial") == "Available":
    ext_spatial = "Spatial Analyst "
else:
    ext_spatial = ""
print "The following extensions are available: " + ext_3D + ext_spatial + ext_network + default
