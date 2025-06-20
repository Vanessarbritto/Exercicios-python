# 7. Entrar via teclado com o valor de cinco produtos. Após as entradas, 
# digitar um valor referente ao pagamento da somatória destes valores. 
# Calcular e exibir o troco que deverá ser devolvido.


soma = 0

n1 = float(input(" valor do primeiro produto: R$ "))
n2 = float(input(" valor do segundo produto: R$ "))
n3 = float(input(" valor do terceiro produto: R$ "))
n4 = float(input(" valor do quarto produto: R$ "))
n5 = float(input(" valor do quinto produto: R$ "))

def somar (n1,n2,n3,n4,n5):
    soma = n1+n2+n3+n4+n5
    return soma

soma_total = somar(n1,n2,n3,n4,n5)

pagamento = float(input("valor do pagamento: R$"))

troco = pagamento - soma_total

print (f" o troco do cliente é: R${troco}")
