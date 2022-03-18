import numpy as np
import matplotlib.pylab as plt

def step_function_1(x):
    y = x >0
    return y.astype(np.int)
x_2=np.array([-1.0,1.0,-2.0])
y_2=step_function_1(x_2)

x_3 = np.arange(-5.0,5.0,0.1) #-5.0에서 5.0 전까지 0.1 간격의 넘파이 배열을 생성
y_3 = step_function_1(x_3)

def sigmoid(x):
    return 1/(1+np.exp(-x))# 브로드 캐스트 기능을 이용해 모두에게 적용
x_4=x_3
y_4=sigmoid(x_4)
plt.plot(x_4,y_4)
plt.ylim(-0.1,1.1)
plt.show()