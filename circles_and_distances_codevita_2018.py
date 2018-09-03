import math
ta=int(input())
ra=int(input())
tb=int(input())
rb=int(input())
t=int(input())
ta=ta%360
xa,ya=int(ra*math.cos((ta*math.pi)/(180))),int(ra*math.sin((ta*math.pi)/180))
tb=tb%360
xb,yb=int(rb*math.cos((tb*math.pi)/(180))),int(rb*math.sin((tb*math.pi)/180))
distance=(((xb-xa)**2)+((yb-ya)**2))**0.5
print("%.2f"%distance)
