def tmp_celsius_para_fahrenheit(x):
    tmp = x * 1.8 + 32
    return tmp

print("-----TRANSFORMAR CELSIUS PARA FAHRENHAIT-----")
valor = float(input("Digite a temperatura em Celsius: "))
print(F" A temperatura convertidade para Fahrenhait é: {tmp_celsius_para_fahrenheit(valor)} ")