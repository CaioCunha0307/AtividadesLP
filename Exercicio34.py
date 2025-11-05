combustivel = 1
alcool = 0
gasolina = 0
diesel = 0

while(combustivel!=4):
    combustivel = int(input())
    if(combustivel==1):
        alcool += 1
    elif(combustivel==2):
        gasolina += 1
    elif(combustivel==3):
        diesel += 1
        
print(f"MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")        