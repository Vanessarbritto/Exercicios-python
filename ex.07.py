# dados dois números inteiros p (>=0) e q (>0) exibir o quociente
#de divisão inteira de p por q sem usar operadores de divisão e multiplicação#

p = int(input("p: "))
q = int(input("q: "))

contador = 0

while p >= q:
    p = p - q
    contador += 1

print(f' o quociente da divisão é {contador}')
