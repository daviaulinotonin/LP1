def conversor(fahrenheit):
    celsius = 0
    celsius = (fahrenheit-32) * 5/9
    return celsius
fahrenheit=int(input('Informe a temperatura em graus Fahrenheit: '))
print(f'{fahrenheit}ºF convertido fica {conversor(fahrenheit)}ºC')