# XOR Gate 만들기
'''
1,1 -> 0
1,0 -> 1
0,1 -> 1
0,0 -> 0
'''
'''
def fun_xor(x1, x2):
    if x1 == x2:
        return 0
    elif x1 != x2:
        return 1

print(fun_xor(1, 0), fun_xor(0, 0), fun_xor(0, 1), fun_xor(1, 1))
'''
def xor_fun(x1, x2):
    tmp = xor_fun(xor_fun(not x1, x2), xor_fun(x1, not x2))
    return tmp

print(xor_fun(1, 0), xor_fun(0, 0), xor_fun(0, 1),xor_fun(1, 1))