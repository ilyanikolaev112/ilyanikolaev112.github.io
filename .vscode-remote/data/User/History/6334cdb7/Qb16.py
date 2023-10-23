r = true
while r == True:
    try:
        frac = input('Дробь:')
        s = frac.split ('/')
        X = int(s[0])
        Y = int(s[1])
        f = X/Y * 100
        f //=1
        r = False
    except ValeError:
        continue
    except ZeroDivisionError:
        continue