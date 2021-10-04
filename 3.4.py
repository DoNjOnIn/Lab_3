import math as m
r=int(input('R='))
x=int(input('x='))
y=int(input('y='))
p=m.sqrt((x+r)**2+(y-r)**2)
print(round(x,2),round(y,2))
if r>p:
    print('CIRCLE')
elif x in range(0,2*r) and y in range(-r,0):
    print('RECTANGULAR')
else:
    print('NOTHING')