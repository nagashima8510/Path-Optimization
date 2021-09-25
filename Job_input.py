import numpy as np
from Constants import *
from A320 import *

###�i�q�ݒ�

#X����
Delta_x=20.0 #[km]�@�ړ_�Ԋu
xmin=0.0 #[km] �n�_
xmax=800.0 #[km]�@�I�_
imin=0
imax=int(imin+(xmax-xmin)/Delta_x)

#Y����
#Delta_Theta=2.0 #[deg]
#Delta_y=Delta_x*np.sin(Delta_Theta*deg2rad) #[km]
ymin=0.0 #[km/deg]
ymax=0.0 #[km/deg]
jmin=0
jmax=0

#Z����
Delta_z_=500.0 #[ft]
zmin_=12000.0 #[ft]
zmax_=40000.0 #[ft]
kmin=0
kmax=int(kmin+(zmax_-zmin_)/Delta_z_)
Delta_z=Delta_z_*ft2m #[m]
zmin=zmin_*ft2m #[m]
zmax=zmax_*ft2m #[m]

#V����
Delta_v=1.0 #[m/s_CAS]
vmin=150.0 #[m/s_CAS]
vmax=180.0 #[m/s_CAS]
lmin=0
lmax=int(lmin+(vmax-vmin)/Delta_v)

###�n�_�I�_�ݒ�

#�n�_
i_start=imin
j_start=jmin
k_start=0
l_start=10
m_start=mmax*0.95

#�I�_
i_end=imax
j_end=jmax
k_end=0
l_end=10