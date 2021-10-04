import math as m
x=float(input('x='))
d=x*x*m.sin(x/2)
#1st
if x<=-5:
    y=d+m.atan(m.e**x)
elif x > -5 and x<=0:
    y=d+1+x**3/4
elif x > 0:
    y=d+m.log10(x)-x/5
print('1)y=' + str(y+d))

#2nd
if x<=-5:
    y1 = d + m.atan(m.e ** x)
else:
    if x > -5 and x <=0:
        y1 = d + 1 + x ** 3 / 4
    else:
        y1 = d + m.log10(x) - x / 5
print('2)y=' + str(y1+d))