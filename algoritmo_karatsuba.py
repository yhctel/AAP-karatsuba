#Let

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y  # Caso base para números pequenos

    x_str = str(x)
    y_str = str(y)

    m = max(len(x_str), len(y_str))
    m2 = m // 2  # Divide o número de dígitos pela metade

    # Divide os números em duas partes
    alto1, baixo1 = int(x_str[:-m2] or 0), int(x_str[-m2:] or 0)
    alto2, baixo2 = int(y_str[:-m2] or 0), int(y_str[-m2:] or 0)

    # Chamadas recursivas para calcular os produtos
    z0 = karatsuba(baixo1, baixo2)
    z1 = karatsuba((baixo1 + alto1), (baixo2 + alto2))
    z2 = karatsuba(alto1, alto2)

    # Calcula o resultado final
    resultado = (z2 * 10**(m2 * 2)) + ((z1 - z2 - z0) * 10**m2) + z0

    return resultado

# Exemplo de uso
x = 1234
y = 567
resultado = karatsuba(x, y)
print("Resultado:", resultado)


