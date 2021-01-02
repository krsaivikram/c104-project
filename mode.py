import csv
from collections import Counter
with open("C:/Users/Manorama/Downloads/height-weight.csv",newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
    filedata.pop(0)
    Data = []
    for i in range(len(filedata)):
        number = filedata[i][1]
        Data.append(float(number))
data=Counter(Data)
modedataforrange = {"50-60":0,"60-70":0,"70-80":0}
for height,occurence in data.items() :
    if 50<float(height)<60:
        modedataforrange["50-60"]+=occurence
    elif 60<float(height)<70:
        modedataforrange["60-70"]+=occurence
    elif 70<float(height)<80:
        modedataforrange["70-80"]+=occurence
moderange,modeoccurence = 0,0
for range,occurence in modedataforrange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((moderange[0]+moderange[1])/2)
print(mode)                               
