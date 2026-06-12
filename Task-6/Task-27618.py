from turtle import *
screensize(5000, 5000)
tracer(False)

m = 15

for i in range(2):
    fd(3 * m)
    lt(90)
    bk(10 * m)
    lt(90)
up()
bk(10 * m)
rt(90)
fd(8 * m)
lt(90)

down()
for i in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)

up()
for x in range(-10, 10):
    for y in range(-30, 10):
        goto(x * m, y * m)
        dot(5, 'white')
