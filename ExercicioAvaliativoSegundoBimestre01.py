#1118 - Várias Notas Com Validação
# Usando obrigatoriamente apenas 'while'

while True:
    # 1. Bloco para ler as duas notas válidas
    soma_notas = 0
    notas_validas = 0
    
    while notas_validas < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            soma_notas += nota
            notas_validas += 1
        else:
            print("nota invalida")
            
    # 2. Calcular e imprimir a média
    media = soma_notas / 2
    print(f"media = {media:.2f}")
    
    # 3. Bloco para validar o "novo calculo"
    x = 0 # Inicializa 'x' com um valor inválido
    
    while x != 1 and x != 2:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
    
    # 4. Condição de saída do loop principal
    if x == 2:
        break