import numpy as np
from numpy import array
from matplotlib import pyplot as plt
# 1 задание
from matplotlib import rc
from scipy import interpolate
rc('font', size=14)
rc('legend', fontsize=13)
rc('text', usetex=True)
rc('text.latex', preamble = [ r'\usepackage[russian]{babel}',
                              r'\usepackage{amsmath}',
                              r'\usepackage{amssymb}'])

rc('font', family = 'serif')
#
phi_y = array([0,5,10,15,20,25,30,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,72,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,])/2 # 150 дел=75 В
i_a  = array([2,2,2,10,24,33,40,45, 46,47,48,49,50,51,52,52,52,52,52,51,50,49,47,46,44,42,41,41,40,40,40,40,40,40,42,44,45,45,46,47,48,52,55,57,60,61,62,63,63,63,64,65,65,64,64,64,63,62,62,62,61,61,60,60,60,61,61,61,61,61,  62,  64, 65, 66, 68, 69, 69, 69, 70, 71, 72, 73, 73, 73])/2 # 100 дел = 50 мкА
z = np.polyfit(phi_y,i_a,17)
f = np.poly1d(z)
x = np.linspace(phi_y[2], phi_y[-1], 1000)


plt.xlabel(r'$\varphi_y,\,\text{В}$', fontsize = '14')
plt.ylabel(r'$I_a,\,\text{мкА}$', fontsize = '14')
plt.minorticks_on()
plt.grid(which='major', linestyle = '-')
plt.grid(which='minor', linestyle=':')
g = interpolate.interp1d(phi_y[0:4],i_a[0:4], 'quadratic')
xx=np.linspace(phi_y[0],phi_y[2],10)
# plt.plot(xx,g(xx), color='darkblue')
# plt.plot(x,f(x), color='darkblue')
# plt.savefig('fig/1.pdf')
# plt.show()

# Ионный ток, запирающий потенциал 40 в
phi_y=array([41,47,50,51,53,54,55,56,56.5,57,57.5,58,58.5,59,59.5,60,60.3,60.5,61,61.5,62])/2 # 150 дел=75 В
i_o = array([2, 5, 10,15,20,25,30,35,40,45,50,55,60,  65,70,75,80,85,  90,95,100])/100 #100 дел= 1 мкА
z=np.polyfit(phi_y,i_o,4)
f=np.poly1d(z)
x=np.linspace(phi_y[0],phi_y[-1],100)
# plt.plot(phi_y,i_o,'r.')

plt.plot(x,f(x))


# # Ионный ток, запирающий потенциал 45 в
phi_y=array([40,21.48*2,48,50,52,53,53.5,54,55,56,56,57,57,58,58,59,59,59,60,60,61,61])/2 # 150 дел=75 В
i_o = array([2, 2, 5, 10,15,20,25,  30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])/100 #100 дел= 1 мкА
z=np.polyfit(phi_y,i_o,4)
f=np.poly1d(z)
x=np.linspace(phi_y[0],phi_y[-1],100)

# plt.plot(phi_y,i_o,'b.')
plt.plot(x,f(x))

# # Ионный ток, запирающий потенциал 50 в
phi_y=array([41,44,48,51,52,53,54,55,55.5,56,57,57.5,58,58.5,59,59.5,60,60.3,60.5,61,61.3,61.5])/2 # 150 дел=75 В
i_o = array([2, 3, 5, 10,15,20,25,30,35,  40,45,50,  55,60,  65,70,  75,80,85,  90,95,100])/100 #100 дел= 1 мкА
z=np.polyfit(phi_y,i_o,4)
f=np.poly1d(z)
x=np.linspace(phi_y[0],phi_y[-1],100)
# plt.plot(phi_y,i_o,'b.')
plt.plot(x,f(x))

plt.legend([r'$40\text{В}$',r'$45\text{В}$',r'$50\text{В}$'])
plt.ylabel(r'$I_{ion},\,\text{мкА}$', fontsize='14')
plt.xlabel(r'$\varphi_y,\,\text{В}$', fontsize='14')
plt.minorticks_on()
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':')
plt.savefig('fig/2.pdf')
plt.show()