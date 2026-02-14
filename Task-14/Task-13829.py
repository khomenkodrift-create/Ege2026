from string import printable

for x in printable[:18]:
    num1 = int(f'71{x}264', 18)
    num2 = int(f'4{x}51{x}1', 18)
    num3 = int(f'21{x}637', 18)
    num = num1 + num2 + num3
    if num % 17 == 0:
        print(num // 17) #1548420

