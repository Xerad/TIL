# OR Gate 만들기

def fun_or(x1, x2):
    w1, w2, threshold = 1, 1,0.5
    tmp = x1*w1 + x2*w2
    if tmp <= threshold:
        return 0
    elif tmp > threshold:
        return 1
    
print(fun_or(1, 0), fun_or(0, 0), fun_or(0, 1), fun_or(1, 1))