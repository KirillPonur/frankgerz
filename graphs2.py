import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
V1=40
Va1=[20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27]
Ia1=[0.02,0.03,0.04,0.05,0.08,0.1,0.12,0.18,0.21,0.28,0.41,0.55,0.65,0.81,1]

V2=45
Va2=[18.5,20,21,22,23,24,24.5,25,25.5,26,26.5,27,27.5]
Ia2=[0.01,0.02,0.04,0.07,0.13,0.2,0.29,0.32,0.51,0.52,0.7,0.81,1]

V3=50
Va3=[20,21,22,23,24,25,25.5,26,26.5,27,27.5]
Ia3=[0.02,0.03,0.06,0.1,0.2,0.31,0.36,0.48,0.6,0.81,1]
h=6.6*10**(-34)
Qe=1.6*10**(-19)
xer=0.75
yer=0.01*1
x=np.polyfit(Va1[len(Va1)-5:len(Va1)]+Va2[len(Va2)-5:len(Va2)]+Va3[len(Va3)-5:len(Va3)],Ia1[len(Ia1)-5:len(Ia1)]+Ia2[len(Ia2)-5:len(Ia2)]+Ia3[len(Ia3)-5:len(Ia3)],1)
p=np.poly1d(x)
print(x)
plt.figure(figsize=[15,10])
plt.plot(Va1,Ia1,'--o',markersize=10,color='k')
plt.errorbar(Va1,Ia1,xerr=xer,yerr=yer,linestyle='',color='k')
plt.plot(Va2,Ia2,'--^',markersize=10,color='r')
plt.errorbar(Va2,Ia2,xerr=xer,yerr=yer,linestyle='',color='r')
plt.plot(Va3,Ia3,'--x',markersize=10,color='g')
plt.errorbar(Va2,Ia2,xerr=xer,yerr=yer,linestyle='',color='g')
plt.plot([23,28],[p(23),p(28)],'--k',lw=3)
plt.ylim([0,1.1])
plt.title('Анодно-сеточная характеристика',fontsize=15)
plt.xlabel('Ускоряющий потенциал $ \phi_y$, В',fontsize=15)
plt.ylabel('Анодный ток $ i_a,\ mA$',fontsize=15)
plt.legend(('$\phi_{31}=40$ В','$\phi_{32}=45$ В','$\phi_{33}=50$ В'),fontsize=20)
plt.grid()
plt.savefig('graphs/2.png',dpi=300)
plt.show()