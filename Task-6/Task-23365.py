from turtle import *

lt(90)

screensize(5000, 5000)
tracer(False)

m = 15

for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)

up()

fd(27*m)
rt(90)
fd(24*m)
lt(90)

down()

for i in range(3):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)

up()

for x in range(-10, 10):
    for y in range(-10, 10):