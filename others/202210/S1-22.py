L = 2
M = 1
N = L + M
i = 0
limite = N/M
while i < 1000:
    #print(L, end=', ')
    L = M 
    M = N 
    N = L + M
    limite = N/M
    i = i + 1

print(limite)