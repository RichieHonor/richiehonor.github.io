#!/Users/richardhonor/anaconda3/bin/python
	
import os 
import argparse


def GetDate(x):
    Elements=x.split("/") 
    name=Elements[8]
    return(name)
    


def main(raw_args=None):


	
	parser=argparse.ArgumentParser(description="Organize data systematically into a csv file")
	parser.add_argument("-RD", "--RawData", help="Raw read data (txt file) to be organized")
	parser.add_argument("-GFM", "--GFMap", help="CSV file (Glucosinolate flavonoid) containing the plate data")
	parser.add_argument("-CHM", "--CHMap", help="CSV file (Chlorophyll) containing the plate data")
	parser.add_argument("-OF", "--outfile", help="CSV file containing the data and ID output")
	parser.add_argument("-H", "--Header", help="Should the program write a header for the data file?")
	args=parser.parse_args(raw_args)

	#return(args)



	#args=options()

	counter=0

	Start=False
	Start2=False

	internalcounter=0
	internalinternalcounter=0


	#Glucosinolate flavonoid map 

	inmap=open(args.GFMap, 'r')

	GFMapElements=[]
	GFType=[]
	GFCol=[]
	count=0
	for x in inmap:
		x=x.strip('\n')
		Focal=x.split("\t")

		#Extracting glucosinolate and flavonoid column information. 
		if count==0:
			GFType.extend(Focal[1:])
		if count==1:
			GFCol.extend(Focal[1:])

		#extracting data names. 
		if count>1:
			GFMapElements.extend(Focal[1:])

		count+=1

	inmap.close()


	#Chlorophyll map 

	inmap=open(args.CHMap, 'r')

	CHMapElements=[]
	CHType=[]
	CHCol=[]
	count=0
	for x in inmap:
		x=x.strip('\n')
		Focal=x.split("\t")

		#Extracting glucosinolate and flavonoid column information. 
		if count==0:
			CHType.extend(Focal[1:])
		if count==1:
			CHCol.extend(Focal[1:])

		#extracting data names. 
		if count>1:
			CHMapElements.extend(Focal[1:])

		count+=1

	inmap.close()





	with open(args.RawData,"r", encoding="utf-16") as f:


		for line in f: 
			#Prep
			line=line.strip("\n")
			ElementList=line.split('\t')


			#Start of a plate ... extract plate name
			if ElementList[0]=="Plate:":
				Plate=ElementList[1]
				Start=True
				
			if Start:
				internalcounter+=1




			
				#Extract Well info. 
				if internalcounter==2:
					Well=ElementList[2:-1]

				#Extract Data info
				if internalcounter==3:
					Data=ElementList[2:-1]

				#Save it all
					outfile=open(args.outfile,'a')			
					for i, j in zip(Well,Data):

						#Remove characters from the well data
						ColName=i.translate({ord(z):None for z in 'ABCDEFGHabcdefgh'})

						#Use a different plate depending on the type of 
						if (Plate.find("Chlor") != -1):
							Col=CHCol
							Type=CHType
							MapElements=CHMapElements
							
						else:
							Col=GFCol
							Type=GFType
							MapElements=GFMapElements

						#Find which column it is 
						ind=Col.index(ColName)
						#Find what compound it is (based on the column name above the well number)
						outfile.write(Plate+','+i+','+j+','+MapElements[internalinternalcounter]+','+Col[ind]+','+Type[ind]+ ','+GetDate(args.RawData)+','+GetDate(args.GFMap)+','+GetDate(args.CHMap)+'\n')
						internalinternalcounter+=1

					outfile.close()
					internalcounter=0
					Start=False
					internalinternalcounter=0


			#Add Header
			if counter==0 and args.Header=="True":
				outfile=open(args.outfile,'a')
				outfile.write("Plate,Well,Data,Sample,Column,Compound,DataFile,GFMapFile,CHMapFile\n")
				outfile.close()

			counter+=1


			#UV_Plate_Organize.py -RD ~/Documents/R/masters_thesis/UVSpec/SpecData/Dat-Dec-6-2019.txt -O ~/Documents/R/masters_thesis/UVSpec/UVData.txt -CHM ~/Documents/R/masters_thesis/UVSpec/SpecMaps/Ch_Map_Dec_6_2019.txt -GFM ~/Documents/R/masters_thesis/UVSpec/SpecMaps/GF_Map_Dec_6_2019.txt


	
if __name__ =="__main__":
	main()

#UV_Plate_Organize.py -RD ~/Documents/R/masters_thesis/UVSpec/SpecData/Dat-Dec-8-2019.txt -O ~/Documents/R/masters_thesis/UVSpec/Out-Dec-8.txt -CHM ~/Documents/R/masters_thesis/UVSpec/SpecMaps/Ch_Map_Dec_8_2019.txt -GFM ~/Documents/R/masters_thesis/UVSpec/SpecMaps/GF_Map_Dec_8_2019.txt
