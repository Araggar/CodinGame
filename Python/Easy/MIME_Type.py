import sys
import math

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.
MIMETable = {}
FileTable = []
toAppend = []
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    MIMETable[ext.lower()] = mt

for i in xrange(q):
    fname = raw_input()  # One file name per line.
    toAppend = fname.split(".")
    if len(toAppend) > 1:
        FileTable.append(toAppend[-1:])
    else:
        FileTable.append("N/A")

for index in xrange(len(FileTable)):
    if FileTable[index][0].lower() in MIMETable:
        print MIMETable[FileTable[index][0].lower()]
    else:
        print "UNKNOWN"