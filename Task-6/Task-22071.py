from turtle import *
screensize(5000, 5000)
tracer(False)
m = 15

fd(30 * m)
lt(60)
fd(24 * m)
rt(240)
fd(54 * m)
lt(120)
fd(24 * m)
lt(60)
up()
fd(30 * m)
rt(90)
fd(20 * m)
lt(90)
down()
for i in range(17):
    fd(6 * m)
    lt(90)
    fd(80 * m)
    lt(90)
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(5, 'white')
update()
done()