import csv
def sampling(num, filename="./data/output.csv"):
	csvfile = open(filename, "r")
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	newname = filename.split(".csv")[0] + "_sampled.csv"
	fileStandard = open(newname, "w+", newline="")
	i = 0
	standard_writer = csv.writer(fileStandard, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for rows in csvreader:
		standard_writer.writerow(rows)
		i += 1
		if (i % num == 0):
			break
	csvfile.close()	
	return newname
	
def main():
	print("Begin taking sample")
	newname = sampling(10000, "./data/output_standard_sanitized_ipchanged.csv")
	print("Finished. Result stored at", newname)
if __name__ == "__main__":
	main()