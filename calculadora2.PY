print("Escolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
print("5 - Bhaskara (delta)")
print("6 - Equação Algébrica")

opcao = input("Digite o número da operação desejada: ").strip()

operadores_map = {"1": "+","2": "-","3": "*","4": "/", "5": "delta","6": "equacao algebrica"}

operador = operadores_map.get(opcao, None)

def calculadora(a, b, operador=None, c=None, d=None):
    try:
        a = float(a)
        if b is not None:
            b = float(b)
        if c is not None:
            c = float(c)
        if d is not None:
            d = float(d)
    except ValueError:
        return 'Erro: Entrada inválida. Digite números válidos.'

    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b if b != 0 else 'Erro: Divisão por zero'
    
    elif operador == 'delta':  
        if b is None or c is None:
            return 'Erro: Para calcular Bhaskara, informe os coeficientes corretamente.'
        delta = (b ** 2) - (4 * a * c)
        if delta < 0:
            return 'Sem raízes reais'
        elif delta == 0:
            x1 = -b / (2 * a)
            return f'Uma raiz real: {x1}'
        else:
            raiz_delta = delta ** 0.5
            x1 = (-b + raiz_delta) / (2 * a)
            x2 = (-b - raiz_delta) / (2 * a)
            return f'Duas raízes reais: {x1}, {x2}'
    
    elif operador == 'equacao algebrica':  
        if b is None or c is None or d is None:
            return 'Erro: Para resolver equações algébricas, informe os coeficientes corretamente.'
        
        for x in range(-100, 101):
            x = x / 10  
            for y in range(-100, 101):
                y = y / 10  
                if (a * x) + (b * y) == c:
                    return f'Solução aproximada: x = {x}, y = {y}'
        
        return 'Nenhuma solução encontrada no intervalo de teste.'

    else:
        return 'Erro: Operador inválido.'

if operador is None:
    print("Erro: Opção inválida.")
else:
    a = input('Digite o primeiro numero: ')
    b = input('Digite o segundo numero: ')
    
    if operador == 'delta':
        c = input('Digite o coeficiente C: ')
        resultado = calculadora(a, b, 'delta', c)
    elif operador == 'equacao algebrica':
        c = input('Digite o terceiro numero: ')
        d = input('Digite o quarto numero: ')
        resultado = calculadora(a, b, 'equacao algebrica', c, d)
    else:
        resultado = calculadora(a, b, operador)
    
    print(f'Resultado: {resultado}')
llll