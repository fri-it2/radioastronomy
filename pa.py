#!/usr/bin/python
import time,math,sys,numpy as np,matplotlib.pyplot as plt
print '*** Avtomatsko risanje slike pulzarja z normalizacijo - 11.05.2017 ***'

povpvrst=80		#stevilo povprecenj vrstic (integer)
povpstolp=20		#stevilo povprecenj stolpcev (integer)
perioda=7145.2		#perioda pulzarja v stevilu vzorcev (float)
odmik=1000		#vodoravni polozaj (integer) 0<odmik=<perioda

k=0.0	#kazalec v polju (float)
v=0	#kazalec vzorcev (integer)
p=0	#kazalec stolpcev (integer)
m=0	#stevec povprecenj v vrstici (integer)
j=0	#stevec vrstic v sliki (integer)
z=0	#stevilo znakov izvornega zapisa (integer) samo informativno

sirina=int(perioda/povpstolp)	#sirina slike kot stevilo stolpcev 
A=np.zeros([sirina],dtype=float)	#naredim prazno vrstico
B=np.zeros([1,sirina],dtype=float)	#naredim prazen zaslon

print 'Zacetek racunanja ',time.ctime()		#zabelezi zacetek racunanja
datoteka=str(sys.argv[1])	#prebere argument programa:program.py spremenljivka
f1=open(datoteka, 'r')		#odpri izvorno datoteko
string=f1.read(odmik)		#precitamo v prazno <odmik> bajtov

print 'Izvor ',datoteka
print 'Stevilo povprecenj vrstic ',povpvrst
print 'Stevilo povprecenj stolpcev ',povpstolp
print 'Perioda pulzarja ',perioda,' vzorcev'
print 'Odmik zacetka ',odmik,' vzorcev'

while string!="": 		#zanko ponavljam, dokler ne pridem do praznega znaka
	string=f1.read(1)
	z=z+1
	if string!="":		#konec izvornega zapisa?
		if p<sirina:		#odstrani zadnji neuporaben stolpec?
			A[p]=A[p]+float(ord(string))	#dodam vhodno vrednost v povprecje
		v=v+1
		if v>=povpstolp:
			v=0
			p=p+1
		k=k+1
		if k>=perioda:			#ena cela perioda pulzarja?
			v=0
			p=0
			k=k-perioda
			print j,' vrstic ',z/1024, ' kByte',chr(13),
			m=m+1
			if m>=povpvrst:		#konec povprecenja ene vrstice?
				A=A-(np.sum(A)/float(sirina))	#normalizacija vrstice
				A=np.sign(A)*np.sqrt(np.abs(A))	#popravi barvno lestvico
				B[j]=A			#vstavi novo vrstico v sliko
				m=0
				j=j+1
				A=np.zeros(sirina,dtype=float)	#naredim prazno vrstico
				B=np.vstack((B,A))		#dodam prazno vrstico v sliko
f1.close()	#zapri izvorni zapis
B=B[0:-1]	#odstrani zadnjo vrstico
print chr(10),'Konec racunanja ',time.ctime()	#konec obdelave datoteke

print B		#poskusni izpis polja (samo informativno)

fig=plt.figure()	#spravimo risanje v slikovni zapis
plt.pcolor(B,cmap='gnuplot2')
plt.colorbar()
plt.title('Izvor: '+datoteka+'\nOdmik: '+str(odmik)+' vzorcev @ Perioda: '+str(perioda)+' vzorcev')
plt.xlabel('Povprecenje: '+str(povpstolp)+' vzorcev/stolpec')
plt.ylabel('Povprecenje: '+str(povpvrst)+' period/vrstica')
#plt.show()			#takojsnji prikaz slike
fig.savefig(datoteka+'.png')	#narise sliko v datoteko

#konec programa

