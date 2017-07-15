#!/usr/bin/python
import time,math,sys,numpy as np,matplotlib.pyplot as plt
print '*** Iskanje periode pulzarja - 11.05.2017 ***'

povpstolp=20		#stevilo povprecenj stolpcev (integer)
nperiod=21		#stevilo razlicnih period>2 (integer)
minp=7145.115		#najmanjsa perioda (float)
maxp=7145.135		#najvecja perioda (float)
odmik=1000		#odmik zacetka (integer) 0<odmik=<perioda
zacetek=8000		#zacetek<konec period povprecenja (integer)
konec=15000		#konec period povprecenja (integer)

print 'Zacetek racunanja ',time.ctime()		#zabelezi zacetek racunanja
k=np.zeros([nperiod],dtype=float)	#kazalec v polju (float)
v=np.zeros([nperiod],dtype=int)		#kazalec vzorcev (integer)
p=np.zeros([nperiod],dtype=int)		#kazalec stolpcev (integer)
m=np.zeros([nperiod],dtype=int)		#stevec povprecenj (integer)
z=0		#stevilo znakov izvornega zapisa (integer) samo informativno
dolzina=konec-zacetek		#stevilo period dolzine povprecenja
dp=(maxp-minp)/float(nperiod-1)	#izracunam vmesne periode
perioda=np.zeros([nperiod],dtype=float)
j=0				
while j<nperiod:
	perioda[j]=minp+dp*j
	j=j+1
sirina=int(minp/povpstolp)	#sirina slike
A=np.zeros([nperiod,sirina],dtype=float)	#naredim prazno polje povprecenj
datoteka=str(sys.argv[1])	#prebere argument programa:program.py spremenljivka
f1=open(datoteka, 'r')		#odpri izvorno datoteko
string=f1.read(odmik)		#precitamo v prazno <odmik> bajtov
z=z+odmik
sp=(maxp+minp)/2.0		#srednja perioda
si=int(sp)			#precitaj v prazno <zacetek> povprecnih period
i=zacetek			
while i>0:			#celi del periode
	string=f1.read(si)
	z=z+si
	i=i-1
i=int(zacetek*(sp-si))		#in se ostanek periode
string=f1.read(i)
z=z+i

print 'Izvor ',datoteka
print 'Stevilo povprecenj stolpcev ',povpstolp
print 'Stevilo razlicnih period ',nperiod
print 'Perioda pulzarja ',perioda,' vzorcev'
print 'Odmik zacetka ',odmik,' vzorcev'
print 'Povprecenje ',zacetek,' ... ',konec,' period'
print 'Sirina grafa ',sirina

while string!="": 		#zanko ponavljam, dokler ne pridem do praznega znaka
	string=f1.read(1)
	z=z+1
	if string!="":		#konec izvornega zapisa?
		s=float(ord(string))
		j=0
		while j<nperiod:
			if p[j]<sirina:		#odstranim zadnji neuporaben stolpec?
				A[j,p[j]]=A[j,p[j]]+s	#dodam vhodno vrednost v povprecje
			v[j]=v[j]+1
			if v[j]>=povpstolp:
				v[j]=0
				p[j]=p[j]+1
			k[j]=k[j]+1
			if k[j]>=perioda[j]:	#ena cela perioda pulzarja?
				v[j]=0
				p[j]=0
				k[j]=k[j]-perioda[j]
				print m[j],' period ',z/1024, ' kByte',chr(13),
				m[j]=m[j]+1
				if m[j]>=dolzina:	#konec povprecenja?
					string=""
			j=j+1

f1.close()	#zapri izvorni zapis
A=(A-(np.sum(A)/float(sirina*nperiod)))/float(dolzina)	#normalizacija rezultata
j=0		#poiscem periodo z najvecjim spikom v celotnem polju
spik=0.0
grba=np.zeros([nperiod],dtype=float)
mspik=0
while j<nperiod:
	u=0
	while u<sirina:
		if grba[j]<A[j,u]:	#risanje grbe najvecjih spikov
			grba[j]=A[j,u]
		if spik<A[j,u]:		#perioda s skupnim najvecjim spikom
			spik=A[j,u]
			mspik=j
		u=u+1
	j=j+1
print chr(10),'Spik ',spik,'@ Max-perioda ',perioda[mspik]
print 'Konec racunanja ',time.ctime()	#konec obdelave datoteke

fig=plt.figure()	#spravimo risanje v slikovni zapis
plt.plot(A[0],'r-')
plt.plot(A[nperiod-1],'b-')
plt.plot(A[mspik],'g-')
plt.title('Izvor: '+datoteka+'\nOdmik: '+str(odmik)+' vzorcev @ Max-perioda: '+str(perioda[mspik])+' vzorcev')
plt.xlabel('Povprecenje: '+str(povpstolp)+' vzorcev/stolpec')
plt.ylabel('Povprecenje: '+str(zacetek)+'...'+str(konec)+' period')
#plt.show()			#takojsnji prikaz slike
fig.savefig(datoteka+'-spik.png')	#narise sliko v datoteko

fig=plt.figure()	#spravimo risanje v slikovni zapis
plt.plot(perioda,grba,'b-')
plt.title('Izvor: '+datoteka+'\nOdmik: '+str(odmik)+' vzorcev @ Max-perioda: '+str(perioda[mspik])+' vzorcev')
plt.xticks([minp,sp,maxp])
plt.xlabel('Perioda [vzorcev]')
plt.ylabel('Visina spika '+str(zacetek)+'...'+str(konec)+' period')
fig.savefig(datoteka+'-grba.png')	#narise sliko v datoteko

#konec programa

