# 1132 - Múltiplos de 13
# Usando obrigatoriamente 2 IFs e 1 WHILE

x = int(input())
y = int(input())

if x > y:
    x, y = y, x

soma = 0
while x <= y: 
    if x % 13 != 0:
        soma += x
    x += 1

print(soma)