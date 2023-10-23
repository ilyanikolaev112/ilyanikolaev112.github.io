r = true
while r == True:
    try:
        frac = input('Дробь:')
        s = frac.split ('/')
        X = int(s[0])
        Y = int(s[1])
        f = X/Y 
