# -*- coding: utf-8 -*-
from fractions import gcd
A='abcdefghijklmnopqrstuvwxyz0123456789'
def hash(text,n):
    t=''
    for r in text:
        if r in A:
            ind=A.index(r)+1
            if ind<10: t=t+'0'+str(ind)
            else: t=t+str(ind)
    return int(t,10)%n  

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None
	
def hash1(m):
    return pow((n - m), 2) + m % n

def hash2(m1, m2):
    return hash1(m1 + m2)
#DSA
print('-------DSA--------')
p = find_next_prime(pow(11,7))
q = 649573 #is factor(p-1) per sage
g = 6 #primitive_root(p)
a = p-151
alpha = pow(g,(p-1)//q,p)
beta = pow(alpha,a,p)
kviesas = [p,alpha,beta,q]
print('K_viesas')
print(kviesas)
k = p-152
x = hash("Ignas Jatulis",100000)
gama = pow(alpha, k,p) % q
delta = ((x + a*gama)*modinv(k,q)) %q
xparasas = [gama, delta]
print('Pranesimas')
print(x)
print('X_parasas')
print(xparasas)

print('TIKRINIMAS')
e1 = (x * modinv(xparasas[1],q)) %q
e2 = (xparasas[0] * modinv(xparasas[1],q)) %q
print((pow(alpha,e1,p)*pow(beta,e2,p))%p%q == gama)

#Gouillou-Quisquater digital signature
print('------Gouillou-Quisquater------')
p = find_next_prime(pow(11,7))
q = find_next_prime(pow(12,6))
n = p*q
fi = (p-1)*(q-1)

e = 51173
i = 12345

d = modinv(e,fi)
a = modinv(pow(i,d,n),n)
kviesas = [n,e,i]
print('K_viesas')
print(kviesas)
k = p-152
r = pow(k,e,n)
x = hash("Ignas Jatulis",100000)
l = hash2(x,r)
s = (k*pow(a,l,n))%n
sig = [s,l]
print('Parasas')
print(sig)
print('Pranesimas')
print(x)
print('TIKRINIMAS')
u = (pow(s,e,n) * pow(i,l,n))%n
l1 = hash1(x+u)
print(l == l1)


