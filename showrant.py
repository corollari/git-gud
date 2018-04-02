import sys
import re
import pickle
AVG_MAX_SHITTINESS=100

input2parse=sys.stdin.read()
m = re.match(r"Summary: TotalFiles=[0-9]* FilesWithViolations=[0-9]* P1=(\d+) P2=(\d+) P3=(\d+)", input2parse)
p1=int(m.group(1))
p2=int(m.group(2))
p3=int(m.group(3))
gravity=100*p1+10*p2+1*p3
shitRatio=1 if gravity>AVG_MAX_SHITTINESS else float(gravity)/AVG_MAX_SHITTINESS
rants=pickle.loads(open("linusrants/data.pkl", 'r').read())
curr=len(rants)//2
floor=0
ceil=len(rants)
while not (curr <= 0 or curr >= (len(rants)-1) or abs(rants[curr-1]["hate"]-shitRatio)>=abs(rants[curr]["hate"]-shitRatio)<=abs(rants[curr+1]["hate"]-shitRatio)): 
    if shitRatio>rants[curr]["hate"]:
        floor=curr
    else:
        ceil=curr
    curr=(ceil+floor)//2
print(rants[curr]["text"])

