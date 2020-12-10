# 没什么特别好的想法

def factors(n):
    k = 1
    while k * k < n:
        if n%k == 0:
            yield k
            yield n//k
        k += 1
    if k*k == n:
        yield k
    