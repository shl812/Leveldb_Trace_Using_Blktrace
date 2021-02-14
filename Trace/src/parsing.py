import os, sys
import csv

#from brokenaxes import brokenaxes
PATH = "/home/lsh/blk/"+str(sys.argv[1]) 
NAME = str(sys.argv[2])
f = open(PATH, 'r')
result2 = []
result3 = []
num1 = []
num2 = []
count=0
result = open(NAME, 'a', encoding='utf-8', newline="")
writer = csv.writer(result)

for line in f:
    if 'db' in line:
        count+=1
        a = line
        b = []
        b=a.split(" ")
        if(b[len(b)-7]!=""):
            print(b[len(b)-9]+"  "+b[len(b)-7]+"  "+b[len(b)-5]+"  "+b[len(b)-4]+"  "+b[len(b)-2])
            writer.writerow([b[len(b)-9], b[len(b)-7], b[len(b)-5], b[len(b)-4], b[len(b)-2],"1"])
        if(b[len(b)-7]==""):
            print(b[len(b)-8]+"  "+b[len(b)-6]+"  "+b[len(b)-5]+"  "+b[len(b)-4]+"  "+b[len(b)-2])
            writer.writerow([b[len(b)-8], b[len(b)-6], b[len(b)-5], b[len(b)-4], b[len(b)-2],"1"])
        continue


result.close()
print(count)
