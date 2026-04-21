from itertools import combinations

def f(x):
    P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    R = {12, 24, 36, 48, 60}
    A = A1 <= x <= A2
    return (not A) <= ((P and Q) <= R)

# (руками) - пересечени P и Q и не входящие в R - 6, 18 => 6 * 18 = 108