#!/usr/bin/python
import time, math, sys, numpy as np, matplotlib.pyplot as pyplot
print '***Risanje realnega dela Poytingovega vektorja-01.11.2017**'
h=0.1		     #velolikost tice
f=5 000 000      #frekvenca sevanja 5Mhz
c=300 000 000	 #hitrost svetlobe 300 000 km/s
k=2*f/c 	     #velikost valovnega vektorja

#polozaj sprejemnika
x0=0
y0=20
z0=0

#izberem T(x,y,z)
x=5
y=5
z=5

#izracunam polozaj opazovalca glede na koordinatno sistem sprejemnika
x1=x-x0
y1=y-y0
z1=y-y1

#pretvorim kartezicne koordinate opazovalca v koordinatnem sistemu oddajnika v krogelne koordinate
r=math.sqrt(x*x+y*y+z*z)
theta=z/math.arccos(sqrt(x*x+y*y+z*z))
fi=math.atan(y/x)

#pretvorim kartežične koordinate opazovalca v koordinatnem sistem oddajnika v krogelne koordinate
r1=math.sqrt(x1*x1+y1*y1+z1*z1)
theta1=z1/math.arccos(sqrt(x1*x1+y1*y1+z1*z1))
fi1=math.atan(y1/x1)
E1=np.zeros([3],dtype=float) 
H1=np.zeros([3],dtype=float)
