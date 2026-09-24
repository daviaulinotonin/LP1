def conversor(celsius):
    fahrenheit = 0
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
celsius=int(input('Informe a temperatura em graus Celsius: '))
print(f'{celsius}ºC convertido fica {conversor(celsius)}ºF')