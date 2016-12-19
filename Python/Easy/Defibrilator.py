import sys
import math

lon = raw_input()
lat = raw_input()
lon = float(lon.replace(",","."))
lat = float(lat.replace(",","."))
n = int(raw_input())
defibList = []
for i in xrange(n):
    defib = raw_input()
    defibList.append(defib.split(";"))
dmin = sys.maxint
for i in xrange(len(defibList)):
    x = (float(defibList[i][4].replace(",",".")) - lon)*math.cos((lat + float(defibList[i][5].replace(",",".")))/2)
    y = float(defibList[i][5].replace(",",".")) - lat
    d = math.sqrt(x**2 + y**2)*6371
    if d<dmin:
        dmin = d
        name = defibList[i][1]
print name

