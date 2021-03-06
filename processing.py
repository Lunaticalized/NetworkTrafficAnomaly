"""
Code written for 2017 MIT summer research project - big data security project
Contributors:  Andrew Bing An Chang, Xiating Ouyang, Lumin Xu 
"""
import csv
from datetime import date
from datetime import datetime
dic = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

MIN_IN_SEC = 60
HOUR_IN_SEC = 60 * MIN_IN_SEC
DAY_IN_SEC = 24 * HOUR_IN_SEC
"""
0  flow type
1  first packet time
2  storage time
3  source IP
4  source port
5  dest IP
6  dest port
7  source Byte
8  dest byte 
9 total byte
10 soure packet
11 dest packet
12 total packet
13 protocol
14 ICMP type
15 source flag
16 dest flag

-- flag
"""	
 
def ipv6AddColon(ipv6):
	segs = []
	i = 0
	for i in range(8):
		segs.append(ipv6[4*i:4*(i+1)])
	return ":".join(segs)
def process(rows):
	for i in range(len(rows) - 4):
		if rows[i] == "N/A":
			rows[i] = "-1"
		if i in [7, 8, 9, 10, 11, 12]:
			rows[i] = "".join(rows[i].split(","))
	rows[3], rows[5] = ipv6AddColon(rows[3]), ipv6AddColon(rows[5])
	return rows;
	
def cal_dif(date1 = "Mar 1, 2016, 9:44:59 PM",
	date2 = "Mar 2, 2016, 10:04:59 AM"):
	
	info1 = date1.split(", ")
	info2 = date2.split(", ")

	date1, year1, time1 = info1[0], int(info1[1]), info1[2]
	mon1, day1 = date1.split()[0], int(date1.split()[1])
	
	date2, year2, time2 = info2[0], int(info2[1]), info2[2]
	mon2, day2 = date2.split()[0], int(date2.split()[1])
	
	d1, d2 = date(year1, dic[mon1], day1), date(year2, dic[mon2], day2) 
	
	diff_days = (d2 - d1).days
	
	seconds = diff_days * DAY_IN_SEC
	t1, p1 = time1.split()[0], time1.split()[1]
	t2, p2 = time2.split()[0], time2.split()[1]
	start_dt = datetime.strptime(t1, '%H:%M:%S')
	end_dt = datetime.strptime(t2, '%H:%M:%S')
	
	diff = (end_dt - start_dt)
	
	# This somehow captures the four cases well.
	if p1 == "AM":
		seconds += 12 * HOUR_IN_SEC
	if p2 == "AM":
		seconds -= 12 * HOUR_IN_SEC
	
	seconds += diff.seconds
	return seconds


	
def separate_data(filename="./data/output.csv"):
	csvfile = open(filename, "r")
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	fileStandard = open("./data/output_standard_sanitized_ipchanged.csv", "w", newline="")
	#fileA = open("./data/output_typeA.csv", "w+", newline="")
	#fileB = open("./data/output_typeB.csv", "w+", newline="")
	#fileC = open("./data/output_typeC.csv", "w+", newline="")
	i = 0
	standard_writer = csv.writer(fileStandard, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	#typeA_writer = csv.writer(fileA, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	#typeB_writer = csv.writer(fileB, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	#typeC_writer = csv.writer(fileC, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for rows in csvreader:
		if "Flow Type" in rows[0]:
			for i in range(len(rows)):
				rows[i] = "_".join(rows[i].split())
			standard_writer.writerow(rows)
			#typeA_writer.writerow(rows)
			#typeB_writer.writerow(rows)
			#typeC_writer.writerow(rows)
		else:
			rows = process(rows)
			try:
				print(rows[6])
				shit = int(rows[6])
				standard_writer.writerow(rows)
			except ValueError:
				pass
			#if "Standard" in rows[0]:
			#	standard_writer.writerow(rows)
			#elif "A" in rows[0]:
			#	typeA_writer.writerow(rows)
			#elif "B" in rows[0]:
			#	typeB_writer.writerow(rows)
			#elif "C" in rows[0]:
			#	typeC_writer.writerow(rows)	
		i += 1
		if (i % 100000 == 0):
			print(str(i) + " entries processed.")
		
	csvfile.close()
	fileStandard.close()	
	#fileA.close()
	#fileB.close()
	#fileC.close()

def main():
	print("Starting off...")
	print("Begin separating data files")
	separate_data()
	print("Finished.")
	
if __name__ == "__main__":
	main()
	#testing()