import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    ## x > 0 조건에 따라 true/false 배열이 (0,1)로 나옴.
    return np.array(x > 0, dtype = np.int)
    
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #y축 범위 지정
plt.show()