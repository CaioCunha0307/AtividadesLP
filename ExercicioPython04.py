N = int(input())
contador_in = 0
contador_out = 0
for i in range(N):
    X = int(input())
    if X >= 10 and X <= 20:
        contador_in += 1
    else:
        contador_out += 1
print(f'{contador_in} in')
print(f'{contador_out} out')