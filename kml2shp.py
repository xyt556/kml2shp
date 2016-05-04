# Version: 	1.0.0
# Author: 	Gregory Giuliani
#			University of Geneva 
#			Institute of Environmental Sciences
#			Climatic Change and Climate Impacts/enviroSPACE
#			Site de Battelle/Bat.D
#			7 route de Drize
#			CH - 1227 Carouge
#			http://www.unige.ch/climate/Team/Giuliani.html
#			http://www.unige.ch/envirospace
#
# Python script to convert KML to Shapefile
# Copyright (C) 2011 Gregory Giuliani
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys, os, string

inputFld = "/Users/Greg/Desktop/kml/"
outputFld = "/Users/Greg/Desktop/shp/"
ogrPath = "/Library/Frameworks/GDAL.framework/Versions/1.8/Programs/"

listing = os.listdir(inputFld)
for infile in listing:
	os.system(ogrPath+'ogr2ogr -f "ESRI Shapefile" '+outputFld+' '+inputFld+infile) 