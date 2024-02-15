import math
gcdnum = 1

def gcd(a, b, c):
    global gcdnum
    gcdnum += 1
    return math.gcd(math.gcd(a, b), c)
    

#Testing GCD
a = -144
b = 2058
c = 302526
print('GCD ' +str(gcdnum) + ' = ' + str(gcd(a, b, c)))  #GCD = 6

a = 3674160
b = -243
c = 51030
print('GCD ' +str(gcdnum) + ' = ' + str(gcd(a, b, c)))  #GCD = 243

a = -733
b = -21379
c = 46782
print('GCD ' +str(gcdnum) + ' = ' + str(gcd(a, b, c)))  #GCD = 1

a = 15
b = 17
c = 46782
print('GCD ' +str(gcdnum) + ' = ' + str(gcd(a, b, c)))  #GCD = 1