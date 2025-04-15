def calculadora(a, b, operador=None, c=None, d=None, e=None, f=None):
    try:
        a = float(a)
        if b is not None:
            b = float(b)
        if c is not None:
            c = float(c)
        if d is not None:
            d = float(d)
        if e is not None:
            e = float(e)
        if f is not None:
            f = float(f)
    except ValueError:
        return 'Entrada inválida. Digite números válidos.'

    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        if b == 0:
            return 'Divisão por zero'
        else:
            return a / b

    elif operador == 'delta':
        if b is None or c is None:
            return 'Para calcular Bhaskara, informe os coeficientes corretamente.'
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
            return 'Para resolver equações algébricas, informe os coeficientes corretamente.'
        for x in range(-100, 101):
            x = x / 10
            for y in range(-100, 101):
                y = y / 10
                if (a * x) + (b * y) == c:
                    return f'Solução aproximada: x = {x}, y = {y}'
        return 'Nenhuma solução encontrada no intervalo de teste.'

    elif operador == 'regra de 3':
        if a == 0:
            return 'Erro: Divisão por zero na regra de 3.'
        return f'Resultado da regra de 3: {(b * c) / a}'

    elif operador == 'porcentagem':
        return f'{b}% de {a} é {(a * b) / 100}'

    elif operador == 'sistema':
        mult1 = e
        mult2 = b
        A1 = a * mult1
        B1 = b * mult1
        C1 = c * mult1
        A2 = d * mult2
        B2 = e * mult2
        C2 = f * mult2
        A = A1 - A2
        C = C1 - C2
        if A == 0:
            return 'Erro: não foi possível resolver por adição, tentativa de divisão por 0.'
        x = C / A
        if b != 0:
            y = (c - a * x) / b
        else:
            y = (f - d * x) / e
        return f'Solução pelo método de adição: x = {x}, y = {y}'

    elif operador == 'conjuntos':
        def obter_conjunto(nome):
            conjunto = set(map(int, input(f"Digite os números do {nome} separados por espaço: ").split()))
            return conjunto

        def menu_Con():
            print("\nEscolha uma opção:")
            print("1 - Comparar conjuntos (interseção, subconjunto ou o contrário)")
            print("2 - Juntar os conjuntos")
            print("3 - Diferença entre os conjuntos")
            print("4 - Sair")
            escolha = int(input("Digite o número da opção desejada: "))
            return escolha

        def comparar_conjuntos(conjunto1, conjunto2):
            print("\nEscolha o tipo de comparação:")
            print("1 - Verificar interseção")
            print("2 - Verificar se conjunto1 é subconjunto de conjunto2")
            print("3 - Verificar se conjunto2 é subconjunto de conjunto1")
            escolha_comparacao = int(input("Digite o número da opção desejada: "))
            if escolha_comparacao == 1:
                intersecao = conjunto1 & conjunto2
                print(f"A interseção entre os conjuntos é: {intersecao}")
            elif escolha_comparacao == 2:
                print("O conjunto1 é subconjunto de conjunto2." if conjunto1.issubset(conjunto2) else "O conjunto1 não é subconjunto de conjunto2.")
            elif escolha_comparacao == 3:
                print("O conjunto2 é subconjunto de conjunto1." if conjunto2.issubset(conjunto1) else "O conjunto2 não é subconjunto de conjunto1.")
            else:
                print("Opção inválida!")

        def juntar_conjuntos(conjunto1, conjunto2):
            uniao = conjunto1 | conjunto2
            print(f"A união dos conjuntos é: {uniao}")

        def diferenca_conjuntos(conjunto1, conjunto2):
            diferenca1 = conjunto1 - conjunto2
            diferenca2 = conjunto2 - conjunto1
            print(f"A diferença entre conjunto1 e conjunto2 é: {diferenca1}")
            print(f"A diferença entre conjunto2 e conjunto1 é: {diferenca2}")

        def executar_conjuntos():
            conjunto1 = obter_conjunto("conjunto 1")
            conjunto2 = obter_conjunto("conjunto 2")
            while True:
                escolha = menu_Con()
                if escolha == 1:
                    comparar_conjuntos(conjunto1, conjunto2)
                elif escolha == 2:
                    juntar_conjuntos(conjunto1, conjunto2)
                elif escolha == 3:
                    diferenca_conjuntos(conjunto1, conjunto2)
                elif escolha == 4:
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida!")

        executar_conjuntos()
        return ''

    else:
        return 'Erro: Operador inválido.'

def ler_valores(qtd):
    return [input(f'Digite o {i+1}º valor: ') for i in range(qtd)]

while True:
    print("0 - Sair")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Bhaskara (delta)")
    print("6 - Equação Algébrica")
    print("7 - Regra de 3")
    print("8 - Porcentagem")
    print("9 - Sistema")
    print("10 - Conjuntos")

    opcao = input("Digite o número da operação desejada: ").strip()

    if opcao == "0":
        print("Saindo... Obrigado por usar a calculadora!")
        break

    operadores_map = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "delta",
        "6": "equacao algebrica",
        "7": "regra de 3",
        "8": "porcentagem",
        "9": "sistema",
        "10": "conjuntos"
    }

    operador = operadores_map.get(opcao, None)

    if operador is None:
        print("Erro: Opção inválida.")
        continue

    if operador == 'delta':
        a, b, c = ler_valores(3)
        resultado = calculadora(a, b, 'delta', c)
    elif operador == 'equacao algebrica':
        a, b, c, d = ler_valores(4)
        resultado = calculadora(a, b, 'equacao algebrica', c, d)
    elif operador == 'regra de 3':
        a, b, c = ler_valores(3)
        resultado = calculadora(a, b, 'regra de 3', c)
    elif operador == 'porcentagem':
        a, b = ler_valores(2)
        resultado = calculadora(a, b, 'porcentagem')
    elif operador == 'sistema':
        a, b, c, d, e, f = ler_valores(6)
        resultado = calculadora(a, b, 'sistema', c, d, e, f)
    elif operador == 'conjuntos':
        resultado = calculadora(0, 0, 'conjuntos')
    else:
        a, b = ler_valores(2)
        resultado = calculadora(a, b, operador)

    if resultado != '':
        print(f'Resultado: {resultado}')
