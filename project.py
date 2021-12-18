import math
import re

p = 0.0
d = 0.0
pv = 0.0
pmt = 0.0
i = 0.0
m = 0
n = 0
residual = 0.0

def pv(p,d):
# to calculate pv
    pv = p - (p * d)
    return pv

def pmt(pv, i, n):
# to calculate pmt
    pmt = (pv * i * ((1 + i)**n))/(((1 + i)**n) - 1)
    return pmt

def residual (pv, pmt, i, n):
# to calculate residual mortgage
    m = 0
    for x in range(1, n + 1):
        if x == 1:
            m = (pv * (1 + i)) - pmt
        else:
            m = (m * (1 + i)) - pmt
            if m < 1.0:
                m = 0.0

    residual = m
    return residual

lines = []
with open('input.txt') as f:
    lines = f.readlines()

f = open("output.txt", "a")
for line in lines:
    L = line.split(',')
    if len(L) == 4:
        for x in L:
            if 'p:' in x:
                p = x[2:]
                result = re.match("[-+]?\d+$", p)
                if result is not None:
                    p = int(p)
                else:
                    p = -1
            if 'd:' in x:
                d = x[2:]
                string_lowercase = d.lower()
                if string_lowercase.islower():
                    d = -1
                else:
                    d = float(d)
            if 'i:' in x:
                i = x[2:]
                string_lowercase = i.lower()
                if string_lowercase.islower():
                    i = -1
                else:
                    i = float(i)

            if 'n:' in x:
                n = x[2:]
                result = re.match("[-+]?\d+$", n)
                if result is not None:
                    n = int(n)
                else:
                    n = -1

        if p == -1:
            f.write('TypeError: p is not an int\n')
        elif d == -1:
            f.write('TypeError: d is not an float\n')
        elif i == -1:
            f.write('TypeError: i is not an float\n')
        elif n == -1:
            f.write('TypeError: n is not an int\n')
        elif p < 0:
            f.write('ValueError: p is out of bounds\n')
        elif not(d > 0 and d < 1.0):
            f.write('ValueError: d is out of bounds\n')
        elif not(i > 0 and i < 1.0):
            f.write('ValueError: i is out of bounds\n')
        elif n < 0:
            f.write('ValueError: n is out of bounds\n')
        else:
            f.write('pv: ')
            pvstr = pv(p,d)
            f.write(str(pvstr))
            f.write(', pmt: ')
            pmtstr = pmt(pv(p,d), i, n)
            f.write(str(pmtstr))
            f.write('\n')

            counter = 1
            for y in range (1, n + 1):
                f.write('M(%d) ' % (y))
                x = (residual(pv(p,d),pmt(pv(p,d),i, n),i,y))
                f.write(str(x))
                f.write('\n')


    elif len(L) < 4:
        f.write('MissingInput: Missing Inputs\n')
    else:
        f.write('MissingInput: Too many Inputs for n\n')

f.close()
