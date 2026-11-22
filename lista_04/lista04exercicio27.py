def maior_valor(a,b,c):
    if a>b:
        if a>c:
            return a
        elif c>a:
            return c
    elif b>a:
        if b>c:
            return b
        elif c>b:
            return c
print(maior_valor(51,2,8))