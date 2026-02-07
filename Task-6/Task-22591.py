from turtle import *

lt(90)

screensize(5000, 5000)
tracer(False)

m = 15

for i in range(4):
    fd(50*m)
    lt(90)
up()

fd(50*m)
lt(135)
down()

for i in range(2):
    fd(102*m)
    lt(120)
    fd(182*m)
    lt(60)

up()

for x in range(-50, 1):
    for y in range(0, 80):
        goto(x*m, y*m)
        dot(8, 'white')

print(50*50/2) # 1250