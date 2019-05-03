def countdown(n):
    print('{},'.format(n), end = '')
    if n > 0: # condición salida recursividad
        countdown(n-1)

countdown(10)