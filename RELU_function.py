import numpy as np
import matplotlib.pylab as plt

def step_function_1(x):
    y = x >0
    return y.astype(np.int)
x_2=np.array([-1.0,1.0,-2.0])
y_2=step_function_1(x_2)

x_3 = np.arange(-5.0,5.0,0.1) #-5.0에서 5.0 전까지 0.1 간격의 넘파이 배열을 생성
y_3 = step_function_1(x_3)

def relu(x):
    return np.maximum(0,x)
 
x_7=x_3
y_7=relu(x_7)
plt.plot(x_7,y_7)
plt.show()