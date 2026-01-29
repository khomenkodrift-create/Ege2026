from turtle import *

screensize(5000, 5000)
tracer(False)

m = 15

for i in range(2):     # затем умножаем ищем площади из фор
    fd(13 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
fd(8 * m)
rt(90)
bk(3 * m)
lt(90)

down()
for i in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)

up()
for x in range(8, 14):         #по ним ищем точки пересечения (вычисляем по модулю)
    for y in range(-5, 1):
        goto(x * m, y * m)
        dot(3, 'red')



update()
done()


print(14 * 21 + 17 * 9 - 6 * 6)