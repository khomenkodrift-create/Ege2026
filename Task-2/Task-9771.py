print('w x y z')
for w in 0, 1:
    for x in 0,1:
        for y in 0, 1:
            for z in 0,1:
                F = (y <= x) and not z and w
                if F:
                    print(w, x, y, z)
                    #wxyz