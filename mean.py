#mean =  the sum of values divided by number of values
#median = stepo one arange in accesding order, the middle most number is the median other wise it will be the average of 2 middle values
#mode = the most occuring value in a data set
import csv
with open("heightWeight.csv", newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))
n = len(new_data)
total = 0
for x in new_data:
    total=total+x
mean = total/n
print(mean)
  



