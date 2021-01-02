import csv
with open("C:/Users/Manorama/Downloads/height-weight.csv",newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
    filedata.pop(0)
    Data = []
    for i in range(len(filedata)):
        number = filedata[i][1]
        Data.append(float(number))


no = len(Data)
sum=0
for i in Data:
    sum =sum+i
mean = sum/no
print("Mean ="+str(mean))    