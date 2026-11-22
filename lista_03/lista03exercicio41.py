mult = 0
for i in range (1,11):
    if not i % 2 == 0:
        print(f'{i}\n')
        print('----------\n')
    if i % 2 == 0:
        for j in range(1,11):
            mult = i*j
            print(f'{i} * {j} = {mult}\n')
        print('----------\n')