# P3b permute-by-cyclic()

from random import randint
s = list(range(10))
#print("Start")
def permute_by_cyclic(a):
    n = len(a)
    z = [0 for i in range(n)]
    oset = randint(1, n)
    for i in range(n):
        dest = (i+oset) % n
        z[dest] = a[i]
        #print("mid")
    return z
p = permute_by_cyclic(s)
#print("end")
print (p)

