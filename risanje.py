from numpy import linalg as LA
import matplotlib.pyplot as plt
import numpy as np
import math

print '***Risanje realnega dela tokovnega elementa(kratka zica)Poytingovega vektorja-01.11.2017**'
print 'tokovni vir v smeri z,  racunalnam v x,z osi ali y,z'
dx,dz=0.036, 0.036 	#korak mreze
h=1		     			#velolikost zice
f=1500000000     			#frekvenca sevanja 50Mhz
c=300000000				 #hitrost svetlobe 300 000 km/s
k=2*f/c 	     		#velikost valovnega vektorja
I=1 			 		#velikost toka v sprejemiku v A
I1=0.5 			 		#velikost toka v A
w=2*math.pi*f
epsilon=8.854*pow(10,-12)#permeabilnost[F/m]
z, x = np.mgrid[slice(-40, 40 + dz, dz),
					slice(-40, 40 + dx, dx)]
#pretvorim kartezicne koordinate opazovalca v koordinatnem sistemu oddajnika v krogelne koordinate	       
r=np.sqrt(x*x+z*z)
theta=np.arccos(z/np.sqrt(x*x+z*z))
fi=np.zeros([len(r),len(r[0])],dtype=float)	#racunam v ravnini xz ali yz=>fi=0
E=np.zeros([3],dtype=float)					#(1_r,1_theta,1_fi), jakost elektricnega polja[V/m=N/As]
H=np.zeros([3],dtype=float)					#(1_r,1_theta,1_fi)), jakost magnetnega  polja [V/m]


E=I/(1j*w*epsilon*4*math.pi)*np.exp(-1j*k*r)*np.array([1j*k/(r*r)+1/(r*r*r)*2*np.cos(theta),(-k*k/r+1j*k/(r*r)+1/(r*r*r))*np.sin(theta),fi])
H=np.array([fi,fi,h*I/(4*math.pi)*np.exp(-1j*k*r)*(1j*k/r+1/(r*r))*np.sin(theta)])
#pretvorba v kartezicni koordinatni sistem oddajnika E(x,y,z)
E_xyz=np.array([np.sin(theta)*np.cos(fi)*E[0]+ np.cos(theta)*np.cos(fi)*E[1]-np.sin(fi)*E[2],np.sin(theta)*np.sin(fi)*E[0]+np.cos(theta)*np.sin(fi)*E[1]+np.cos(fi)*E[2],np.cos(theta)*E[0]-np.sin(theta)*E[1]])
H_xyz=np.array([np.sin(theta)*np.cos(fi)*H[0]+ np.cos(theta)*np.cos(fi)*H[1]-np.sin(fi)*H[2],np.sin(theta)*np.sin(fi)*H[0]+np.cos(theta)*np.sin(fi)*H[1]+np.cos(fi)*H[2],np.cos(theta)*H[0]-np.sin(theta)*H[1]])

H=np.conj(H_xyz)
E=E_xyz
#racunanje Poytingov vektor S=1/2ExH*(E vektorsko H konjugirano)
S=np.array([E[1]*H[2]-E[2]*H[1],E[2]*H[0]-E[0]*H[2],E[0]*H[1]-E[1]*H[0]])
S_vel=np.sqrt(np.real(S[0])*np.real(S[0])+np.real(S[1])*np.real(S[1])+np.real(S[2])*np.real(S[2]))
#velikost realnega dela Poytingovega vektorja(potujoca moc)
S_vel=np.sqrt(np.real(S[0])*np.real(S[0])+np.real(S[1])*np.real(S[1])+np.real(S[2])*np.real(S[2]))
#velikost imaginarnega dela Poytingova vektorja(nihajoca moc)
S_vel_img=np.sqrt(np.imag(S[0])*np.imag(S[0])+np.imag(S[1])*np.imag(S[1])+np.imag(S[2])*np.imag(S[2]))

z_min, z_max = np.log(np.abs(S_vel_img)).min(), np.log(np.abs(S_vel_img)).max()
#plt.pcolor(x, z, np.log(S_vel) ,vmin=z_min, vmax=z_max)
plt.pcolor(x, z, np.log(np.abs(S_vel)) ,vmin=z_min, vmax=z_max)
plt.title('frekvenca: '+ str(f/1000000) +' MHz: realni del Poytingovega vektorja')
plt.ylabel('velikost Poytingovega vektorja')
plt.xlabel('oddaljenost v metrih')
plt.colorbar()
plt.show()