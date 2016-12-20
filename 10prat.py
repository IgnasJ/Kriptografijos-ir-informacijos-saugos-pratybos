# -*- coding: utf-8 -*-
from fractions import gcd

A='abcdefghijklmnopqrstuvwxyz'
def i_skaiciu(text):
    t=''
    for r in text:
        if r in A:
            ind=A.index(r)+1
            if ind<10: t=t+'0'+str(ind)
            else: t=t+str(ind)
    return int(t,10)  

def i_teksta(M):
    n=M
    text=''
    while n>0:
        ind=n%100
        ind=ind-1
        if (ind>=0) & (ind<len(A)):
            text+=A[ind]
            n=(n-ind+1)//100
        else:
            text+='?'
            n=(n-ind+1)//100            
    return text[::-1]     
    

#Jūsų RSA raktai
n = 3116011905994280067612347463657431229976637879915928640181
e = 999503473565
d = 2659395321589779265654788358636680417132943807742306356553

#laiskas
C = 2015962348322811582501710584969112892688195555890608354478

M = pow(C,d,n)
T=i_teksta(M)

print(T)
#naujienosprastos

#Algio RSA raktai
nAlgio = 3116011905994280067612347463657431229976637879915928640181
eAlgio = 235754716993
#Algiui skirtas RSA laiškas:
cAlgio = 2125389766669700601828181440956432110682476788517404337112
#reik rast algio privatu rakta d

N = e*d-1

print(N)

temp = N
t = 0
while (N%2 == 0):
	N = N//2
	t = N

a0 = pow(2,t,n)
a1 = pow(a0,2,n)
print(a1)	

p = gcd(a0+1, n)
q = n//p

f = (p-1)*(q-1)
print(f)


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


dAlgio = modinv(eAlgio, f)

M = pow(cAlgio,dAlgio,n)
T=i_teksta(M)

print(T)	
#darbaatidesime

rabino = 215574027191065222067461298822954977115017150244279349872

c1 = pow(rabino, (p+1)//4, p)
c2 = pow(rabino, (q+1)//4, q)

u = modinv(p, q)
v = modinv(q, p)

M = (c1*v*q + c2*u*p)%n
T=i_teksta(M)
print(T)

M = (-1*c1*v*q + c2*u*p)%n
T=i_teksta(M)
print(T)

M = (c1*v*q - c2*u*p)%n
T=i_teksta(M)
print(T)

M = (-1*c1*v*q - c2*u*p)%n
T=i_teksta(M)
print(T)
