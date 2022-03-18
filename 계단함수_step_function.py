# 계단함수 구현 (step_function)

import numpy as pd
import numpy as np
import matplotlib.pylab as plt

def step_function_1(x):
    y = x > 0
    return y.astype(np.int)

import numpy as np
def step_function_1(x):
    y = x >0
    return y.astype(np.int)
x_2=np.array([-1.0,1.0,-2.0])
y_2=step_function_1(x_2)


x_3 = np.arange(-5.0,5.0,0.1) #-5.0에서 5.0 전까지 0.1 간격의 넘파이 배열을 생성
y_3 = step_function_1(x_3)
plt.plot(x_3,y_3)
plt.ylim(-0.1,1.1)
plt.show()

