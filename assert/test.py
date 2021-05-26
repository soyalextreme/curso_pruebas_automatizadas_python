from algoritmos import fibonacci, palindromo, factorial

# la funcion debe de iniciar con la palabra test

def test_fibonacci_cinco():
    assert fibonacci(5) == 5, "No es 5"


def test_palindromo_anita():
    assert palindromo("anita lava la tina"), "No es un palindromo"


def test_factorial_cinco():
    assert factorial(5) == 120, "Es 120 el factorial de 5"


# usando el modulo pytest corre el archivo
# pytest assert/test.py
# Listo!! de esta manera logras correr el archivo

