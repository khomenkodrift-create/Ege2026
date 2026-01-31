from turtle import *

screensize(5000, 5000)
tracer(False)
lt(90)
m = 20


for i in range(2):
    fd(20 * m)
    lt(270)
    fd(12 * m)
    rt(90)

up()

fd(9 * m)
rt(90)
fd(7 * m)
lt(90)
down()

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
for x in range(7, 13):
    for y in range(9, 21):
        goto(x * m, y * m)
        dot(3, 'red')

update()


print(21 * 13 + 14 * 7 - 6 * 12)