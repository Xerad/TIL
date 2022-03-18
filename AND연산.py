# AND Gate 만들기

def fun_and(x1, x2):
    w1, w2, threshold = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= threshold:
        return 0
    elif tmp > threshold:
        return 1
    
print(fun_and(1, 0), fun_and(0, 0), fun_and(0, 1), fun_and(1, 1))