import numpy as np
from Constants import *
from A320 import *

###格子設定

#X方向
Delta_x=20.0 #[km]　接点間隔
xmin=0.0 #[km] 始点
xmax=800.0 #[km]　終点
imin=0
imax=int(imin+(xmax-xmin)/Delta_x)

#Y方向
#Delta_Theta=2.0 #[deg]
#Delta_y=Delta_x*np.sin(Delta_Theta*deg2rad) #[km]
ymin=0.0 #[km/deg]
ymax=0.0 #[km/deg]
jmin=0
jmax=0

#Z方向
Delta_z_=500.0 #[ft]
zmin_=12000.0 #[ft]
zmax_=40000.0 #[ft]
kmin=0
kmax=int(kmin+(zmax_-zmin_)/Delta_z_)
Delta_z=Delta_z_*ft2m #[m]
zmin=zmin_*ft2m #[m]
zmax=zmax_*ft2m #[m]

#V方向
Delta_v=1.0 #[m/s_CAS]
vmin=150.0 #[m/s_CAS]
vmax=180.0 #[m/s_CAS]
lmin=0
lmax=int(lmin+(vmax-vmin)/Delta_v)

###始点終点設定

#始点
i_start=imin
j_start=jmin
k_start=0
l_start=10
m_start=mmax*0.95

#終点
i_end=imax
j_end=jmax
k_end=0
l_end=10