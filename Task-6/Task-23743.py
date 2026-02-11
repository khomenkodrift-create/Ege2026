from turtle import *

screensize(5000, 5000)
tracer(False)

m = 10

for i in range(2):
    fd (14 * m)
    lt (270)
    bk(12 * m)
    rt (90)

up()

fd (9 * m)
rt (90)
bk(7 * m)
lt(90)

down()
for i in range(2):
    fd (13 * m)
    rt (90)
    fd(6 * m)
    rt (90)

up()

for x in range(9, 20):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()

#2
