

import numpy as np

def strassen_matrix_mult(a, b):
    n = len(a)
    if n == 1:
        return a * b
    
    a11, a12, a21, a22 = a[:n//2, :n//2], a[:n//2, n//2:], a[n//2:, :n//2], a[n//2:, n//2:]
    b11, b12, b21, b22 = b[:n//2, :n//2], b[:n//2, n//2:], b[n//2:, :n//2], b[n//2:, n//2:]

    p = np.zeros((7, n//2, n//2))
    p[0] = strassen_matrix_mult(a11 + a22, b11 + b22)
    p[1] = strassen_matrix_mult(a21 + a22, b11)
    p[2] = strassen_matrix_mult(a11, b12 - b22)
    p[3] = strassen_matrix_mult(a22, b21 - b11)
    p[4] = strassen_matrix_mult(a11 + a12, b22)
    p[5] = strassen_matrix_mult(a21 - a11, b11 + b12)
    p[6] = strassen_matrix_mult(a12 - a22, b21 + b22)

    c11 = p[0] + p[3] - p[4] + p[6]
    c12 = p[2] + p[4]
    c21 = p[1] + p[3]
    c22 = p[0] - p[1] + p[2] + p[5]
    
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c




def nice_string(s):
    size=len(s)
    if size==0:
        return ""
    last=s[size-1]
    if (last.islower() and  (last.upper() not in s)) or (last.isupper() and (last.lower() not in s)):
        return nice_string(s[:(size-1)])
    else:
        return nice_string(s[:(size)])

    
s = "aAb"
result = nice_string(s)
print(result)




