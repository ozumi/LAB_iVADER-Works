import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4", "Problem 5"]
group = ["A", "B"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","time","confidence"]

#number = 44
col = 13
with open('for_sum_0122.csv', 'rb')as csvfile:
	with open('sum.csv', 'wb') as csvf2:
        	firstrow = True
		
		spamreader = csv.reader(csvfile, delimiter=',')
		spamwriter = csv.writer(csvf2, delimiter=',')

		sum_list = [None] * col
		for i in range(col):
			sum_list[i] = 0.0
		count = 0
		for row in spamreader:
			if count == 5:
				sum_list[10] /= 5
				sum_list[12] /= 5
				print sum_list
				spamwriter.writerow(sum_list)
				for i in range(col):
					sum_list[i] = 0.0
				count = 0
			if firstrow:
				firstrow = False
			else:
				count += 1
				for j in range(col):
					if j == 0 : sum_list[0] = row[1]
					elif j == 1 : sum_list[1] = row[2]
					else : 
						sum_list[j] += float(row[j+1])

