import numpy as np
import matplotlib.pyplot as plt
#prvi stopec pomeni dan od 30.4.2017, drugo izracunana perioda
izracunana=np.array([0.714544554071,0.714543634776,0.714542708495,0.714541775504,0.714540836077,0.714539890493,0.714538939031,0.714537981972,0.7145370196,0.71453605219,0.714535080055,0.714534103455,0.714533122689,0.714532138046,0.714531149817,0.71453015829])
#opazovanje=np.array([0,0.714545],[3,0.7145418],[6,0.7145392],[8,0.7145373],[10,0.7145355],[12,0.7145334]) 
opazovanjex=np.array([0,3,6,8,10,12])#dan od 30.aprila naprej
opazovanjey=np.array([0.714545,0.7145418,0.7145392,0.7145373,0.7145355,0.7145334])#opazovana  perioda pulzarja
plt.plot(izracunana,label='Izracunano')
plt.plot(opazovanjex,opazovanjey,'r^',label="Opazovano")
#plt.plot(opazovanje,"ro",label='Opazovano')
plt.xlabel('cas')
plt.ylabel('perioda 1/s')
plt.title('Opazovanje pulzarjev')
plt.legend()
plt.show()
