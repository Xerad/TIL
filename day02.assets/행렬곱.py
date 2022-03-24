'''
행렬의 곱(백터의 내적)을 나타내는 연산은 np.dot() 함수이다.
다차원 배열을 곱하려면 두 행렬의 대응하는 차원의 원소 수를 일치시켜야 한다.
A는 2차원 행렬 B가 1차원 배열일때도 "대응하는 차원의 원소수를 일치"시켜야 한다.
'''
import numpy as np

A_1 = np.array([[1,2],[3,4]])
B_1 = np.array([[5,6],[7,8]])
np.dot(A_1, B_1)

a_1 = np.array([1,2])
b_1 = np.array([3,4])
np.dot(a_1, b_1)

x = np.array([1,2])
w = np.array([[1,3,5], [2,4,6]])
np.dot(x, w)