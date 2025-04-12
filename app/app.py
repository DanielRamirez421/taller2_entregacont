# app/app.py
"""Aplicación Flask para realizar operaciones aritméticas básicas.

Este módulo define una aplicación web que permite a los usuarios
realizar sumas, restas, multiplicaciones y divisiones a través
de un formulario HTML.
"""

from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Ruta principal de la aplicación.

    Muestra un formulario para que el usuario ingrese dos números y seleccione
    una operación aritmética (sumar, restar, multiplicar, dividir). Procesa el
    formulario en caso de envío y muestra el resultado correspondiente.

    Returns:
        str: Renderizado del template HTML `index.html` con el resultado de la operación.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    # Punto de entrada de la aplicación.
    # Ejecuta la aplicación Flask en modo desarrollo.
    app.run(debug=True, port=5000, host="0.0.0.0")
    # Quitar debug=True para producción
