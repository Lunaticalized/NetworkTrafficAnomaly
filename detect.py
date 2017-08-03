import csv
"""
0  flow type
1  first packet time
2  storage time
3  -- conn duration
4  source IP
5  source port
6  dest IP
7  dest port
8  source Byte
9  dest byte 
10 total byte
11 soure packet
12 dest packet
13 total packet
14 protocol
15 ICMP type
16 source flag
17 dest flag

-- flag
"""	
def iterate_data(filename="./data/output_standard.csv"):
	csvfile = open(filename, "r")
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	
	users = dict() # key: dest ip        value: all ips that succ connect to it
	i = 1
	for rows in csvreader:
		if rows[9] == "N/A":
			print(rows)
	csvfile.close()
	
	
	#conn_num_file = open("./data/conn_num_count.csv", "w")
	
	#check_ip(users, "output_typeA")
	#check_ip(users, "output_typeB")
	#check_ip(users, "output_typeC")

def check_ip(users, filename):
	csvfile = open("./data/" + filename+".csv", "r")
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	file = open("./data/checking_falsePositives_"+filename+".csv", "w", newline="")
	file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for rows in csvreader:
		if rows[6] in users:
			if rows[4] in users[rows[6]]:
				file_writer.writerow(rows)
	csvfile.close()
	file.close()
def main():
	print("Starting off...")
	print("You may have a rest now")
	iterate_data()
	print("Finished.")

	
if __name__ == "__main__":
	main()
	#testing()