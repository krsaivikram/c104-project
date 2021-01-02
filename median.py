
import csv
with open("C:/Users/Manorama/Downloads/height-weight.csv",newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
    filedata.pop(0)
    Data = []
    for i in range(len(filedata)):
        number = filedata[i][1]
        Data.append(float(number))
n=len(Data)
Data.sort()
if n%2==0:
    med1 = float(Data[n//2])
    med2 = float(Data[n//2-1])
    median = (med1+med2)/2
else:
    median = float(Data[n/2])
    print(n)
print(str(median))
        