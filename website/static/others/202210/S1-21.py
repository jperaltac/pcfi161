
suma = 0
d = 1
i = 0
while i < 1000:
    s = pow(-1,i)
    suma = suma + s*1/d
    d  = d + 2
    i = i + 1

print(suma)
    