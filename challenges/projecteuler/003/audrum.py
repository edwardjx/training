"""Calcula los factores primos de un numero"""


def factor_primo(numero):
    """Calcula los factores primos"""
    factor = 2
    while numero != 1:
        if numero % factor == 0:
            print factor, end=' '
            numero = numero / factor
        else:
            factor += 1


def pedir_numero():
    """Solicita el número al usuario"""
    valor = int(input("Ingrese el número para calcular factores primos: "))
    factor_primo(valor)


pedir_numero()
