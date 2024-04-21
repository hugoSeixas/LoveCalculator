import random 

# valor conterá digitos de 0 até 9
st = '0123456789'

# resultado sera em dois digitos 
digitos = 2 

# variavel que contem o resultado 
resultado = "".join(random.sample(st, digitos))
print(resultado)