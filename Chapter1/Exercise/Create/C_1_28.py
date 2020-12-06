

import math

def norm(v,p):
    vector_value = 0
    for i in v:
        vector_value += i**p
    v_value = math.sqrt(vector_value)
    return v_value
    
v = (1,1,1)
p = 2
print(norm(v,p))