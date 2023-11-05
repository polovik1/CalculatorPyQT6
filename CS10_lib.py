def from10cs(a: int, b: int) -> str:
    if a >= b:
        d = a % b
        if d > 10:
            match d:
                case 10:
                    d = str('A')
                case 11:
                    d = str('B')
                case 12:
                    d = str('C')
                case 13:
                    d = str('D')
                case 14:
                    d = str('E')
                case 15:
                    d = str('F')
        return from10cs(a // b, b) + str(d)
    else:
        return str(a)


def to10cs(a: int, b: int):
    a = str(a)
    fnum = 0
    d = 0
    for i in range(len(a)):
        if (b > 10) & (i < len(a)):
            match a[len(a) - (i + 1)]:
                case 'A':
                    d = 10*(b**i)
                case 'B':
                    d = 11*(b**i)
                case 'C':
                    d = 12*(b**i)
                case 'D':
                    d = 13*(b**i)
                case 'E':
                    d = 14*(b**i)
                case 'F':
                    d = 15*(b**i)
                case _:
                    d = int(a[len(a) - (i + 1)]) * (b ** i)
            fnum += d
            d = 0
        elif i <= len(a):
            d = int(a[len(a) - (i+1)])*(b**i)
        fnum += d
    return fnum
