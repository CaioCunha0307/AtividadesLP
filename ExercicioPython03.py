contador_pares = 0
for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        contador_pares += 1
print(f'{contador_pares} valores pares')