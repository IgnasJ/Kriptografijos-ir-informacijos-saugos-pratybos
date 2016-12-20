#  -*- coding: utf-8 -*-

#daryt kaip paskaitoj. 3 Sistemos, pagal kontrolinius bitus sprendi perstumti bita ar ne ir vis pirmus 3 bitus xor 

def stream(c,xp,n):  # the keystream generation, c-coefficients, xp - initial state, n - number of bits
    x=[0,0,0,0,0,0,0,0]
    for i in range(0,8):
        x[i]=xp[i]
    sr=''
    for i in range(0,n):
        bt=0
        sr+=str(x[0])
        for j in range(0,8):
            bt+=c[j]*x[j]
        for j in range(1,8):
            x[8-j]=x[7-j]
        x[0]=bt%2
    return sr

#stream cipher
def str_cipher(t,c,xp): # t - plaintext (ASCII decimal list), c-coefficients, xp - initial state
    cp=[]
    k=len(t)
    sr=stream(c,xp,8*k)
    for i in range (0,k):
        cp.append(t[i]^int(sr[8*i:8*i+8],2))
    return cp
# How to use
	# c=[1,0,1,0,1,1,0,1]
	# t=[10,123]
	# xp=[1,0,1,0,1,1,0,1]
	# cp=str_cipher(t,c,xp)
	# print cp
	# print str_cipher(cp,c,xp)


tekstas = [64, 39, 239, 252, 62, 196, 101, 82, 249, 15, 76, 23, 105, 141, 6, 164, 98, 190, 152, 194, 77, 216, 146, 58, 47, 25, 155, 247, 210, 167, 186, 87, 56, 229, 231, 56, 199, 127, 84, 230, 28, 67, 21, 106, 143, 14, 170, 103, 169, 131, 217, 76, 205, 147, 43, 40, 25, 148, 246, 214, 167, 170, 65, 47, 234, 230, 51, 199, 120, 70, 241, 0, 65, 19, 108, 143, 10, 179, 112, 162, 153, 214, 75, 198, 133, 45, 61, 30, 156, 226, 206, 181, 170, 65, 39, 248, 232, 35, 205, 99, 83, 243, 11]
t = [ord('P'), ord('R')]

pirmi_astuoni = tekstas[0]^t[0]
like_astuoni = tekstas[1]^t[1]

print(bin(pirmi_astuoni))
print(pirmi_astuoni)
print(bin(like_astuoni))
print(like_astuoni)

c1=[0,0,0,1,1,0,1,1]
c2=[1,0,0,1,0,1,1,1]
xp=[0,0,1,1,1,1,1,1]

cp=str_cipher(tekstas,c2,xp)
for i in cp:
        print (chr(i), end="")

#print (str_cipher(cp,c1,xp))
