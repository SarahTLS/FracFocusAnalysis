## Import the modules we will useAdvancedEffects
## Upload CSVs
## WGS84 = EPSG:4326 , NAD83 = ESPG:4269, NAD27 = EPSG:4267
#
#from qgis.core import QgsProject #QGIS3
#import processing # import the processing algorithm
#
#### Change the WGS 84 to NAD 1983
#
#uri = "file:///C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/FracDataWGS84.csv?delimiter=,&crs=epsg:4326&xField=bgLongitude&yField=bgLatitude"
#vlayer = QgsVectorLayer(uri,'CSVDataWGS84','delimitedtext')
#
#dest_crs = QgsCoordinateReferenceSystem("ESPG:4326") # create a variable to assign the datum to the CSV
#shapefile_path = r"C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/ShpFracDataWGS84.shp"
#writer = QgsVectorFileWriter.writeAsVectorFormat(vlayer, shapefile_path, "utf-8", dest_crs, "ESRI Shapefile") 
#vlayer2 = QgsVectorLayer(shapefile_path, "WGS84data", "ogr")
## QgsProject.instance().addMapLayer(vlayer2) 
#
#shapefilepath_split = shapefile_path.split('/Sh')
#projshapepath = shapefilepath_split [0] + '/FracDataWGS84toNAD83.shp' 
#processing.run("native:reprojectlayer", {'INPUT': vlayer2,'TARGET_CRS': 'EPSG:4269','OUTPUT':projshapepath}) 
#reprojlayer = QgsVectorLayer(projshapepath, "FracWGS84toNAD83", "ogr")  
#QgsProject.instance().addMapLayer(reprojlayer) # add fixed shapefile coord system to map 
#
#### Change the NAD 1927 to NAD 1983
#
#uri27 = "file:///C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/FracDataNAD27.csv?delimiter=,&crs=epsg:4267&xField=bgLongitude&yField=bgLatitude"
#vlayer27 = QgsVectorLayer(uri27,'CSVDataNAD27','delimitedtext')
#
#dest_crs27 = QgsCoordinateReferenceSystem("ESPG:4267") # create a variable to assign the datum to the CSV
#shapefile_path27 = r"C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/ShpFracDataNAD27.shp"
#writer27 = QgsVectorFileWriter.writeAsVectorFormat(vlayer27, shapefile_path27, "utf-8", dest_crs27, "ESRI Shapefile") 
#vlayer27b = QgsVectorLayer(shapefile_path27, "NAD27data", "ogr")
## QgsProject.instance().addMapLayer(vlayer27b) 
#
#shapefilepath_split27 = shapefile_path27.split('/Sh')
#projshapepath27 = shapefilepath_split27 [0] + '/FracDataNAD27toNAD83.shp' 
#processing.run("native:reprojectlayer", {'INPUT': vlayer27b,'TARGET_CRS': 'EPSG:4269','OUTPUT':projshapepath27}) 
#reprojlayer27 = QgsVectorLayer(projshapepath27, "FracNAD27toNAD83", "ogr")  
#QgsProject.instance().addMapLayer(reprojlayer27) # add fixed shapefile coord system to map 
#
#### Convert NAD 1983 to shsapefile
#
#uri83 = "file:///C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/FracDataNAD83.csv?delimiter=,&crs=epsg:4269&xField=bgLongitude&yField=bgLatitude"
#vlayer83 = QgsVectorLayer(uri83,'CSVDataNAD83','delimitedtext')
#
#dest_crs83 = QgsCoordinateReferenceSystem("ESPG:4269") # create a variable to assign the datum to the CSV
#shapefile_path83 = r"C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/ShpFracDataNAD83.shp"
#writer83 = QgsVectorFileWriter.writeAsVectorFormat(vlayer83, shapefile_path83, "utf-8", dest_crs83, "ESRI Shapefile") 
#vlayer83b = QgsVectorLayer(shapefile_path83, "NAD83data", "ogr")
#QgsProject.instance().addMapLayer(vlayer83b) 
#

### Merge the threedatasets into one!

##Restating file path vvariables, in case we don't want to re-run the code above
#shapefile_path = r"C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/ShpFracDataWGS84.shp"
#projshapepath = shapefilepath_split [0] + '/FracDataWGS84toNAD83.shp' 
#shapefile_path27 = r"C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/ShpFracDataNAD27.shp"
#projshapepath27 = shapefilepath_split27 [0] + '/FracDataNAD27toNAD83.shp' 
#shapefile_path83 = r"C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/ShpFracDataNAD83.shp"
#
#ThreeLayers = [projshapepath, projshapepath27, shapefile_path83]
TLoutputpath = r"C:/Users/Sarah/Desktop/Learning_python_CSVs/FracData/AllProjMerged.shp"
#processing.run("native:mergevectorlayers",{'LAYERS':ThreeLayers,'OUTPUT':TLoutputpath})
#
allfracdatareproj = QgsVectorLayer(TLoutputpath, "All Frac Data Re-Projected", "ogr")

#Exporting to CSV with new coordinates read more here: https://gis.stackexchange.com/questions/168081/how-to-reproject-500-csv-files-efficiently-and-easily-using-qgis
