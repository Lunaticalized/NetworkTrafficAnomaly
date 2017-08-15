import csv
import random
def sampling(num, filename="./data/output.csv"):
	csvfile = open(filename, "r")
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	newname = filename.split(".csv")[0] + "_sampled.csv"
	fileStandard = open(newname, "w+", newline="")
	i = 0
	standard_writer = csv.writer(fileStandard, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for rows in csvreader:
		if (i <= 100000 + num and i >= 100000):
			standard_writer.writerow(rows)
		elif i < 100000:
			i += 1
			continue
		else:
			break
		print(i)
		i += 1
	csvfile.close()	
	return newname
	
def main():
	print("Begin taking sample")
	newname = sampling(10000, "./data/output.csv")
	print("Finished. Result stored at", newname)
if __name__ == "__main__":
	main()