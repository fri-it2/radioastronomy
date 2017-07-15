#!/usr/bin/python
print '*Izracun hitrosti Zemlje proti pulzarju v nekem trenutku 11.5.2017*'
from datetime import datetime,date,time,timedelta
import numpy as np
import math
from numpy import inner
from math import radians,cos, sin
datum=datetime(2017,5,25,15)#datum opazovanja
pomladisce=datetime(2017,3,20,10,28)#datum nasega pomladisca
razlika=(datum-pomladisce).total_seconds()
#razlika med datumom opazovanja in pomladiscem v sekundah
t=timedelta(days=365.242).total_seconds()#leto v sekundah 
w=2*3.14/t #obodna hitrost Zemlje okoli Sonca
R=149597870691 #razdalja Zemlje do Sonca
ra=53.2458#ektascenzija pulzarja B0329+54
dec=54.5786#deklinacija pulzarja B0329+54
ra=radians(53.2458)
dec=radians(54.578768)
p=np.array([math.cos(ra)*math.cos(dec),math.cos(dec)*math.sin(ra),math.sin(dec)])
#vektor 
vs=np.array([-R*w*sin(w*razlika),R*w*cos(w*razlika)*cos(radians(23.5)),R*w*cos(w*razlika)*sin(radians(23.5))])
np.linalg.norm(vs)#hitrost Sonca
t=0.714520#perioda pulzarja, ki jo najdeno v katalogu na spletu
f=1/t #frekvenca pulzarja, ki jo najdemo v katalogu na spletu
vz=inner(p,vs)#komponenta hitrosti proti pulzarju
print vz,'Hitrost Zemlje proti pulzarju'
print f
f1=f*(1-vz/300000000.00)#doplerjev premik frekvence pulzarja, ki jo vidimo z Zemlje
print 1/f1, 'popravljena perioda'
