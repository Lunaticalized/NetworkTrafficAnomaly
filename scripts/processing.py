"""
Code written for 2017 MIT summer research internship - big data security project

Contributors: Xiating Ouyang, Lumin Xu, Andrew Bing An Chang 
"""
import csv


"""
flow type
first packet time
storage time
source IP
source port
dest IP
dest port
source Byte
dest byte 
total byte
soure packet
dest packet
total packet
protocol
ICMP type
source flag
dest flag
"""	
#add duration, nice/evil flag, 
def process(rows):
	
	return rows;
	
	

def separate_data():
	csvfile = open("./../data/output.csv", "r")
	csvreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
	fileStandard = open("output_standard.csv", "w+", newline="")
	fileA = open("output_typeA.csv", "w+", newline="")
	fileB = open("output_typeB.csv", "w+", newline="")
	fileC = open("output_typeC.csv", "w+", newline="")
	i = 0
	standard_writer = csv.writer(fileStandard, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	typeA_writer = csv.writer(fileA, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	typeB_writer = csv.writer(fileB, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	typeC_writer = csv.writer(fileC, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for rows in csvreader:
		rows = process(rows)
		if "Standard" in rows[0]:
			standard_writer.writerow(rows)
		elif "A" in rows[1]:
			typeA_writer.writerow(rows)
		elif "B" in rows[1]:
			typeB_writer.writerow(rows)
		elif "C" in rows[1]:
			typeC_writer.writerow(rows)
		else:
			# then it has to be the header
			standard_writer.writerow(rows)
			typeA_writer.writerow(rows)
			typeB_writer.writerow(rows)
			typeC_writer.writerow(rows)
		i += 1
		if (i % 10000 == 0):
			print(str(i) + " done.")
	
	csvfile.close()	
	fileA.close()
	fileB.close()
	fileC.close()