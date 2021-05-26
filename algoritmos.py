def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number - 1) + fibonacci(number - 2)


def palindromo(sentence):
    """
    Retorna verdadero si el parametro es un palindromo 
    en caso contrario retorna falso.


    sentence -- string o entero

    >>> palindromo("anita lava la tina")
    True 
    >>> palindromo(12321)
    True
    >>> palindromo("Mi mama me mima")
    True
    """
    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]

