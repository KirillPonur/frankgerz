import numpy as np
from numpy import array
from matplotlib.pylab import *
from matplotlib import rc
from functions import parsing
from scipy import interpolate
rc('font', size=14)
rc('legend', fontsize=13)
rc('text', usetex=True)
rc('text.latex', preamble = [ r'\usepackage[russian]{babel}',
                              r'\usepackage{amsmath}',
                              r'\usepackage{amssymb}'])

rc('font', family = 'serif')
name='fig2.txt'
x,y=parsing(name,0,1)
g = interpolate.interp1d(x,y, 'cubic')
x=linspace(x[0],x[-1],1000)
y=g(x)
x0=linspace(0.3,0.7,100)
y0=g(x0)
phi_1=x0[argmax(y0)]
# print(phi_1,x[36])
phi_min=x0[argmin(y0)]
x0=linspace(0.85,1.1,100)
y0=g(x0)
phi_2=x0[argmax(y0)]
 # xlabel(r'$\varphi_y$', fontsize = '20'))
ylabel(r'$I_a$', fontsize = '22')
yticks([])
xticks([phi_1,phi_min,phi_2],
	[r'$\varphi_1$',r'$\varphi_{min}$',r'$\varphi_2$'],
	fontsize='22')

grid(which='major', linestyle = ':')
plot(x,y,color='darkblue')
savefig('pic2.pdf')
show()