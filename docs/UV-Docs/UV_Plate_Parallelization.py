#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:25:20 2019

@author: richardhonor
"""


import os

import glob

import sys

import UV_Plate_Organize as UV


os.chdir("/Users/richardhonor/scripts/DataScripts/UVScripts")





def GetDate(x):
    Elements=x.split("/") 
    name=Elements[8]

    return(name)
    



#Paths to data and maps
SpecData=glob.glob("/Users/richardhonor/Documents/R/masters_thesis/UVSpec/SpecData/*.txt")

SpecMaps=glob.glob("/Users/richardhonor/Documents/R/masters_thesis/UVSpec/SpecMaps/*.txt")


#Isolate gf maps and ch maps

#ChMaps=[f for f in Maps if "Ch" in f] 

#GFMaps=[f for f in Maps if "GF" in f] 

#List of list of files to analyze. 
Analyze=[]

for i in SpecData:
	#Names to search for text files. 
	Name=GetDate(i)
	Name=Name[4:]
	#All maps with the correct date. 
	Maps=[f for f in SpecMaps if Name in f]


	Maps.append(i)

	Analyze.append(Maps)


#Now there is a list of list of files to be analyzed. 



#Run analysis over all data
count=0
for i in Analyze:

	ChMap=[f for f in i if "Ch" in f][0] 

	GFMap=[f for f in i if "GF" in f][0] 

	Dat=[f for f in i if "Dat" in f][0] 

	if count==0:
		H="True"

	else:
		H="False"

	UV.main(["-RD", Dat, "-O", "/Users/richardhonor/Documents/R/masters_thesis/Synthesis/Data_Moities/All_UV_Data.txt", "-CHM" ,ChMap, "-GFM", GFMap, "-H", H])

	count+=1



