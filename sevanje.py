#!/usr/bin/python

from numpy import linalg as LA
print '***Risanje realnega dela Poytingovega vektorja-01.11.2017**'
h=1		     #velolikost tice
f=5000000      #frekvenca sevanja 5Mhz
c=300000000	 #hitrost svetlobe 300 000 km/s
k=2*f/c 	     #velikost valovnega vektorja
I=1 			 #velikost toka v sprejemiku v A
I1=0.5 			 #velikost toka v A
w=2*math.pi*f
#polozaj sprejemnika
x0=0
y0=20
z0=0.
epsilon=8.854*pow(10,-12)#permeabilnost[F/m]
#tokovni vir v smeri z
#izberem T(x,y,z)
x=5
y=5
z=0
 x,y=np.mgrid[0.2:5:complex(0,N), 0.2:5:complex(0,N)]
#izracunam polozaj opazovalca glede na koordinatno sistem sprejemnika
x1=x-x0
y1=y-y0
z1=y-y1

#pretvorim kartezicne koordinate opazovalca v koordinatnem sistemu oddajnika v krogelne koordinate
r=np.sqrt(x*x+z*z)
theta=np.arccos(z/np.sqrt(x*x+z*z))
fi=np.atan(y/x)

#pretvorim kartežične koordinate opazovalca v koordinatnem sistem oddajnika v krogelne koordinate
r1=math.sqrt(x1*x1+y1*y1+z1*z1)
theta1=z1/(np.arccos(sqrt(x1*x1+y1*y1+z1*z1)))
fi1=np.atan(y1/x1)
#izracun prispevka E in H od sprejemnika
E=np.zeros([3],dtype=float)#(1_r,1_theta,1_fi), jakost elektricnega polja[V/m=N/As]
H=np.zeros([3],dtype=float)#(1_r,1_theta,1_fi)), jakost magnetnega  polja [V/m]
E=I/(1j*w*epsilon*4*math.pi)*np.exp(-1j*k*r)*np.array([1j*k/(r*r)+1/(r*r*r)*2*np.cos(theta),(-k*k/r+1j*k/(r*r)+1/(r*r*r))*np.sin(theta)])
H=np.array([fi;fi;*h*I/(4*math.pi)*(np.cos(-k*r*1j)+1j*np.sin(-k**r*1j))*(1j*k/r+1/(r*r))*np.sin(theta)])
E=I/(1j*w*epsilon*4*math.pi)*cmath.exp(-1j*k*r)np.array([1j*k/(r*r)+1/(r*r*r)*2*np.cos(theta);(-k*k/r+1j*k/(r*r)+1/(r*r*r))*np.sin(theta);0])
#izracun prispevka E1 in H1:pripevek oddajnika
H1=np.array([fi;fi;*h*I1/(4*math.pi)*(np.cos(-k*r1*1j)+1j*np.sin(-k*r1*1j))*(1j*k/r1+1/(r1*1r)*np.sin(theta1))])
E1=I1/(1j*w*epsilon*4*math.pi)*cmath.exp(-1j*k*r1)np.array(1j*k/(r1*r1)+1/(r1*r1*r1)*2*math.cos(theta1);(-k*k/r1+1j*k/(r1*r1)+1/(r1*r1*r1))*math.sin(theta1);0)
#pretvorba v kartezični koordinatni sistem oddajnika E(x,y,z)
E_xyz=np.array([math.sin(theta)*mat.cos(fi)*E[0]+ math.cos(theta)*math.cos(fi)*E[1]-math.sin(fi)*E[2],mat.sin(theta)*mat.sin(fi)*E[0]+mat.cos(theta)*mat.sin(fi)*E[1]+mat.cos(fi)*E[2],math.cos(theta)*E[0]-math.sin(theta)*E[1]])
H_xyz=np.array([math.sin(theta)*mat.cos(fi)*H[0]+ math.cos(theta)*math.cos(fi)*H[1]-math.sin(fi)*H[2],mat.sin(theta)*mat.sin(fi)*H[0]+mat.cos(theta)*mat.sin(fi)*H[1]+H.cos(fi)*H[2],math.cos(theta)*H[0]-math.sin(theta)*H[1]])
 E_xyz=np.array([np.sin(theta)*np.cos(fi)*E[0]+ np.cos(theta)*np.cos(fi)*E[1]-np.sin(fi)*E[2],np.sin(theta)*np.sin(fi)*E[0]+np.cos(theta)*np.sin(fi)*E[1]+np.cos(fi)*E[2],np.cos(theta)*E[0]-np.sin(theta)*E[1]])
 H_xyz=np.array([np.sin(theta)*np.cos(fi)*H[0]+ np.cos(theta)*np.cos(fi)*H[1]-np.sin(fi)*H[2],np.sin(theta)*np.sin(fi)*H[0]+np.cos(theta)*np.sin(fi)*H[1]+np.cos(fi)*H[2],np.cos(theta)*H[0]-np.sin(theta)*H[1]])

E1_xyz=np.array([math.sin(theta1)*mat.cos(fi)*E1[0]+ math.cos(theta)*math.cos(fi)*E1[1]-math.sin(fi)*E1[2],mat.sin(theta)*mat.sin(fi)*E1[0]+mat.cos(theta)*mat.sin(fi)*E1[1]+mat.cos(fi)*E1[2],math.cos(theta)*E1[0]-math.sin(theta)*E1[1]])
H1_xyz=np.array([math.sin(theta)*mat.cos(fi)*H1[0]+ math.cos(theta)*math.cos(fi)*H1[1]-math.sin(fi)*H1[2],mat.sin(theta)*mat.sin(fi)*H1[0]+mat.cos(theta)*mat.sin(fi)*H1[1]+mat.cos(fi)*H1[2],math.cos(theta)*H1[0]-math.sin(theta)*H1[1]])

S=1/2*np.cross(E1_xyz+Exyz,np.conj(H_xyz+H1_xyz))
S=np.array([E[1]*B[2]-E[2]*B[1],E[2]*H[0]-E[0]*H[2],E[0]*H[1]-E[1]*H[0]])
LA.norm(S)
