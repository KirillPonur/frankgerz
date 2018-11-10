print(2+2)
import sys
print(sys.executable)

import numpy as np 
from numpy import array
from matplotlib import pyplot as plt 
phi_y=array([41,47,50,51,53,54,55,56,56.5,57,57.5,58,58.5,59,59.5,60,60.3,60.5,61,61.5,62])/2 # 150 дел=75 В
i_o = array([2, 5, 10,15,20,25,30,35,40,45,50,55,60,  65,70,75,80,85,  90,95,100])/100 #100 дел= 1 мкА
plt.plot(phi_y,i_o)
plt.show()