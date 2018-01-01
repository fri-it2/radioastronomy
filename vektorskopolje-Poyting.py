from numpy import linalg as LA
import matplotlib.pyplot as plt
import numpy as np
import math

import plotly.plotly as py
import plotly.figure_factory as ff
import plotly 
plotly.tools.set_credentials_file(username='tadeja', api_key='oFANK7EmuVYkwJLD7iSs')
plotly.tools.set_config_file(world_readable=True,
                             sharing='public')
import numpy as np
print '***Risanje vektorskega polja Poytinkovega vektorja: sprejemnik in oddajnik-1.1.2018**'
print 'tokovni vir v smeri z,  racunalnam v x,z osi ali y,z'
dx,dz=0.21745, 0.21743 	#korak mreze
h=1		     			#velolikost zice
f=10000000  			#frekvenca sevanja 10Mhz
c=300000000				 #hitrost svetlobe 300 000 km/s
k=2*f/c 	     		#velikost valovnega vektorja
I=0.1 			 		#velikost toka v sprejemiku v A
I1=0.01j 			 		#velikost toka v A
w=2*math.pi*f
lam=c/f  				#valovna dolzina [m]
bliznje_polje=float(lam)/6
print 'Bliznje polje do '+str(bliznje_polje)
epsilon=8.854*pow(10,-12)#permeabilnost[F/m]
z, x = np.mgrid[slice(-4, 4 + dz, dz),
					slice(-4, 4 + dx, dx)]
#izberem T(x,y,z):polozaj oddajnika

r=np.sqrt(x*x+z*z)
theta=np.arccos(z/np.sqrt(x*x+z*z))
#fi=np.atan(y/x) 
fi=np.zeros([len(r),len(r[0])],dtype=float)#racunam v ravnini xz ali yz=>fi=0

#tokovni element sprjemnika:da je prenos moci mora biti tokovna elementa v kvadraturi
Tx=2
Tz=0.2	
x1=x-Tx

z1=z-Tz
r=np.sqrt(x*x+z*z)
theta=np.arccos(z/np.sqrt(x*x+z*z))
#fi=np.atan(y/x) 
fi=np.zeros([len(r),len(r[0])],dtype=float)#racunam v ravnini xz ali yz=>fi=0

E=I/(1j*w*epsilon*4*math.pi)*np.exp(-1j*k*r)*np.array([1j*k/(r*r)+1/(r*r*r)*2*np.cos(theta),(-k*k/r+1j*k/(r*r)+1/(r*r*r))*np.sin(theta),fi])
H=np.array([fi,fi,h*I/(4*math.pi)*np.exp(-1j*k*r)*(1j*k/r+1/(r*r))*np.sin(theta)])
#pretvorba v kartezicni koordinatni sistem oddajnika E(x,y,z)
E_xyz=np.array([np.sin(theta)*np.cos(fi)*E[0]+ np.cos(theta)*np.cos(fi)*E[1]-np.sin(fi)*E[2],np.sin(theta)*np.sin(fi)*E[0]+np.cos(theta)*np.sin(fi)*E[1]+np.cos(fi)*E[2],np.cos(theta)*E[0]-np.sin(theta)*E[1]])
H_xyz=np.array([np.sin(theta)*np.cos(fi)*H[0]+ np.cos(theta)*np.cos(fi)*H[1]-np.sin(fi)*H[2],np.sin(theta)*np.sin(fi)*H[0]+np.cos(theta)*np.sin(fi)*H[1]+np.cos(fi)*H[2],np.cos(theta)*H[0]-np.sin(theta)*H[1]])

#pretvorim kartezicne koordinate opazovalca v koordinatnem sistemu oddajnika v krogelne koordinate	       
r1=np.sqrt(x1*x1+z1*z1)
theta1=np.arccos(z1/np.sqrt(x1*x1+z1*z1))
fi1=np.zeros([len(r),len(r[0])],dtype=float)	#racunam v ravnini xz ali yz=>fi=0
E1=np.zeros([3],dtype=float)					#(1_r,1_theta,1_fi), jakost elektricnega polja[V/m=N/As]
H1=np.zeros([3],dtype=float)					#(1_r,1_theta,1_fi)), jakost magnetnega  polja [V/m]


E1=I1/(1j*w*epsilon*4*math.pi)*np.exp(-1j*k*r1)*np.array([1j*k/(r1*r1)+1/(r1*r1*r1)*2*np.cos(theta1),(-k*k/r1+1j*k/(r1*r1)+1/(r1*r1*r1))*np.sin(theta1),fi1])
H1=np.array([fi1,fi1,h*I1/(4*math.pi)*np.exp(-1j*k*r1)*(1j*k/r1+1/(r1*r1))*np.sin(theta1)])
#pretvorba v kartezicni koordinatni sistem oddajnika E(x,y,z)
E_xyz1=np.array([np.sin(theta1)*np.cos(fi1)*E1[0]+ np.cos(theta1)*np.cos(fi1)*E1[1]-np.sin(fi1)*E1[2],np.sin(theta1)*np.sin(fi1)*E1[0]+np.cos(theta1)*np.sin(fi1)*E1[1]+np.cos(fi1)*E1[2],np.cos(theta1)*E1[0]-np.sin(theta1)*E1[1]])
H_xyz1=np.array([np.sin(theta1)*np.cos(fi1)*H1[0]+ np.cos(theta1)*np.cos(fi1)*H1[1]-np.sin(fi1)*H1[2],np.sin(theta1)*np.sin(fi1)*H1[0]+np.cos(theta1)*np.sin(fi1)*H1[1]+np.cos(fi1)*H1[2],np.cos(theta1)*H1[0]-np.sin(theta1)*H1[1]])

H=H_xyz+H_xyz1
E=E_xyz+E_xyz1



#racunanje Poytingov vektor S=1/2ExH*(E vektorsko H konjugirano)
S=np.array([E[1]*H[2]-E[2]*H[1],E[2]*H[0]-E[0]*H[2],E[0]*H[1]-E[1]*H[0]])
S_vel=np.sqrt(np.real(S[0])*np.real(S[0])+np.real(S[1])*np.real(S[1])+np.real(S[2])*np.real(S[2]))
#velikost realnega dela Poytingovega vektorja(potujoca moc)
S_vel=np.sqrt(np.real(S[0])*np.real(S[0])+np.real(S[1])*np.real(S[1])+np.real(S[2])*np.real(S[2]))
#velikost imaginarnega dela Poytingova vektorja(nihajoca moc)
S_vel_img=np.sqrt(np.imag(S[0])*np.imag(S[0])+np.imag(S[1])*np.imag(S[1])+np.imag(S[2])*np.imag(S[2]))
z_min, z_max =  np.log(S_vel_img).min(),  np.log(S_vel_img).max()
#z_min, z_max = np.log(np.abs(np.where(S_vel_img!=0)).min(), np.log(np.abs(np.where(S_vel_img!=0)).max()
#print S
#plt.pcolor(x, z, np.log(S_vel) ,vmin=-5, vmax=5)
#plt.title('frekvenca: '+ str(f/1000000) +' MHz: realni del Poytingovega vektorja')
#plt.ylabel('velikost Poytingovega vektorja')
#plt.xlabel('oddaljenost v metrih')
#plt.colorbar()
#plt.show()


#x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u = np.cos(x)
v = np.sin(x)
print len(x)
print len(z)
print len(S_vel)
print len(S_vel_img)
#risanje vektorskega polja Poytingovega vektorja
plt.quiver(x, z, np.real(S[0]),np.real(S[2]),  pivot='mid',  units='inches')
#plt.quiver(x, z, np.real(S[0]),np.real(S[2]), units='x', pivot='tip', width=0.022,scale=1 / 0.1)
plt.show()
#fig = ff.create_quiver(x, z, S_vel, S_vel_img)
#py.iplot(fig, filename='Quiver Plot Example')

#plt.figure()
#plt.quiver(x, z, 100000*S_vel, 100000*S_vel_img)
#plt.show()
