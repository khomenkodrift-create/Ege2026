from turtle import *

screensize(5000, 5000)
tracer(False)

m = 15
rt(315)
for i in range(7):
    fd(12 * m)
    rt(45)
    fd(6 * m)
    rt(135)

up()
for x in range(0, 16):
    for y in range(0, 10):
        goto(x * m, y * m)
        dot(3,'red')

done()
update()

#4 * 8 = 32