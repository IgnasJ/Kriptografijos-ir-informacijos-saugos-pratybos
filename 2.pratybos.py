#!/usr/bin/python3
# coding: utf-8
abc=unicode('A¿BC»DE∆ÀFGHI¡YJKLMNOPRS–TUÿ€VZﬁ','utf-8')
n=len(abc)
def Ceasar(tekst,k1, k2):
    tekstU=tekst.upper()
    t=unicode('','utf-8')
    for r in tekstU:
        if r in abc:
            t+=r
    c=unicode('','utf-8')
    for r in t:
        #m=(abc.index(r)+k)%n
        m=( (abc.index(r)-k2)* (1/k1%32) ) %32
        c+=abc[m]
    return c
print Ceasar(unicode('€Aÿ–¡ OB€RC »¡UBS –∆¡ÿI ÿYÿ–¡','btf-8'),1, 12)
print Ceasar(unicode('€Aÿ–¡ OB€RC »¡UBS –∆¡ÿI ÿYÿ–¡','btf-8'),3, 12)
print Ceasar(unicode('€Aÿ–¡ OB€RC »¡UBS –∆¡ÿI ÿYÿ–¡','btf-8'),5, 12)
print Ceasar(unicode('€Aÿ–¡ OB€RC »¡UBS –∆¡ÿI ÿYÿ–¡','btf-8'),7, 12)
# for a in range(1,32):
    # for b in range(1,32):
        # if ( (a%2) == 1):
            # print a, " ", b
            # print Ceasar(unicode('Y¡–BﬁLYFYﬁYÀBﬁY','utf-8'),a, b)