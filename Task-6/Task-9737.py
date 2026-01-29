from turtle import *

screensize(5000, 5000)
tracer(False)
m = 25

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(5, 11):
    for y in range(-14, -6):
        goto(x * m, y * m)
        dot(8,'white')



update()
done()