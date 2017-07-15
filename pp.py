#!/usr/bin/python
import time,serial,math,sys,numpy as np,matplotlib.pyplot as plt
print '*** Graf periode pulzarja - 11.05.2017 ***'

povpstolp=20		#stevilo povprecenj stolpcev (integer)
perioda=7145.117	#perioda pulzarja v stevilu vzorcev (float)
odmik=1000		#odmik zacetka (integer) 0<odmik=<perioda
zacetek=8000		#zacetek<konec period povprecenja (integer)
konec=15000		#konec period povprecenja (integer)

print 'Zacetek racunanja ',time.ctime()		#zabelezi zacetek racunanja
k=0.0	#kazalec v polju (float)
v=0	#kazalec vzorcev (integer)
p=0	#kazalec stolpcev (integer)
m=0	#stevec povprecenj (integer)
z=0	#stevilo znakov izvornega zapisa (integer) samo informativno
dolzina=konec-zacetek		#stevilo period dolzine povprecenja
sirina=int(perioda/povpstolp)	#sirina slike kot stevilo stolpcev 
A=np.zeros([sirina],dtype=float)	#naredim prazno polje periode

datoteka=str(sys.argv[1])	#prebere argument programa:program.py spremenljivka
f1=open(datoteka, 'r')		#odpri izvorno datoteko
string=f1.read(odmik)		#precitamo v prazno <odmik> bajtov
z=z+odmik
si=int(perioda)			#precitaj v prazno <zacetek> povprecnih period
i=zacetek			
while i>0:			#celi del periode v prazno
	string=f1.read(si)
	z=z+si
	i=i-1
i=int(zacetek*(perioda-si))	#in se ostanek periode v prazno
string=f1.read(i)
z=z+i

print 'Izvor ',datoteka
print 'Stevilo povprecenj stolpcev ',povpstolp
print 'Perioda pulzarja ',perioda,' vzorcev'
print 'Odmik zacetka ',odmik,' vzorcev'
print 'Povprecenje ',zacetek,' ... ',konec,' period'
print 'Sirina grafa ',sirina,' tock'

while string!="": 		#zanko ponavljam, dokler ne pridem do praznega znaka
	string=f1.read(1)
	z=z+1
	if string!="":		#konec izvornega zapisa?
		if p<sirina:		#odstranim zadnji neuporaben stolpec?
			A[p]=A[p]+float(ord(string))	#dodam vhodno vrednost v povprecje
		v=v+1
		if v>=povpstolp:
			v=0
			p=p+1
		k=k+1
		if k>=perioda:		#ena cela perioda pulzarja?
			v=0
			p=0
			k=k-perioda
			print m,' period ',z/1024, ' kByte',chr(13),
			m=m+1
			if m>=dolzina:	#konec povprecenja?
				string=""

f1.close()					#zapri izvorni zapis
A=(A-(np.sum(A)/float(sirina)))/float(dolzina)	#normalizacija rezultata
print chr(10),'Konec racunanja ',time.ctime()	#konec obdelave datoteke

spik=np.amax(A)		#izracunaj sirino impulza
mspik=np.argmax(A)
meja=spik/2.0		#izbrana meja za sirino
w=0.0
varna=sirina-1		#varna meja racunanja !!!
if mspik>1 and mspik<varna-1:
	p=mspik			#dodaj sirino pred max
	while p>1 and A[p-1]>meja:
		w=w+1.0
		p=p-1
	if p>0:
		w=w+(A[p]-meja)/(A[p]-A[p-1])
	p=mspik			#dodaj sirino za max
	while p<varna-1 and A[p+1]>meja:
		w=w+1.0
		p=p+1
	if p<varna:
		w=w+(A[p]-meja)/(A[p]-A[p+1])
w=w*float(povpstolp)	#preracunaj v stevilo vzorcev
print 'Sirina impulza ',w,' vzorcev'

fig=plt.figure()	#spravimo risanje v slikovni zapis
plt.plot([0,sirina],[meja,meja],'y-')	#narisi polovicno visino spika
plt.plot(A,'b-')	#narisi pulz
plt.title('Izvor: '+datoteka+'\nOdmik: '+str(odmik)+' vzorcev @ Perioda: '+str(perioda)+' vzorcev')
plt.xlabel('Povprecenje: '+str(povpstolp)+' vzorcev/stolpec    Sirina impulza: '+str(w)+' vzorcev')
plt.ylabel('Povprecenje: '+str(zacetek)+'...'+str(konec)+' period')
fig.savefig(datoteka+'-pulz.png')	#narise sliko v datoteko

#konec programa

