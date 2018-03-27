import sys
import re

input2parse=sys.stdin.read()
m = re.match(r"Summary: TotalFiles=[0-9]* FilesWithViolations=[0-9]* P1=(\d+) P2=(\d+) P3=(\d+)", input2parse)
p1=int(m.group(1))
p2=int(m.group(2))
p3=int(m.group(3))
gravity=100*p1+10*p2+1*p3
print(gravity)
