# app/calculadora.py
"""Módulo de funciones aritméticas básicas.

Contiene funciones para realizar suma, resta, multiplicación y división
de dos números reales.
"""

def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de a + b.
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de a - b.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de a * b.
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): Numerador.
        b (float): Denominador.

    Returns:
        float: Resultado de a / b.

    Raises:
        ZeroDivisionError: Si b es igual a cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
