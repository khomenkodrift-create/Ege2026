# all(val[i] != val[i + 1] for i in range(len(val) - 1)) - никакие две одинаковые
# не стоят рядом

# val[-1] not in '26' - последний символ не может быть 2 или 6

#    if val[0] != '0' and len(val) == len(set(val)): - все цифры различны и никакие две
#        for i in printable[:16:2]:                    чётные или две нечётные цифры не стоят рядом
#           val = val.replace(i, '*')
#        for i in printable[1:16:2]:
#            val = val.replace(i, '_')
#        if '**' not in val and '__' not in val: