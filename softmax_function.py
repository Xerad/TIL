import numpy as np
a = np.array([0.3, 2.9, 4.0])
exp_a=np.exp(a)
print(exp_a)
## [ 1.34985881 18.17414537 54.59815003]


sum_exp_a=np.sum(exp_a)
y=exp_a/sum_exp_a
print(y)
## [0.01821127 0.24519181 0.73659691]


def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y

#nan은 not a number
a = np.array([1010, 1000, 990])
np.exp(a)/np.sum(np.exp(a))
## array([9.99954600e-01, 4.53978686e-05, 2.06106005e-09])

def softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c) # 오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y

a= np.array([0.3, 2.9, 4.0])
y=softmax(a)
print(y)
np.sum(y)
## [0.01821127 0.24519181 0.73659691]
## 1.0
