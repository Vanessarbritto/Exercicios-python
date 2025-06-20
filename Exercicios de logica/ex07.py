# 7. Entrar via teclado com o valor de cinco produtos. Após as entradas, 
# digitar um valor referente ao pagamento da somatória destes valores. 
# Calcular e exibir o troco que deverá ser devolvido.


soma = 0

n1 = float(input(" valor do primeiro produto: R$ "))
n2 = float(input(" valor do segundo produto: R$ "))
n3 = float(input(" valor do terceiro produto: R$ "))
n4 = float(input(" valor do quarto produto: R$ "))
n5 = float(input(" valor do quinto produto: R$ "))

soma = n1+n2+n3+n4+n5
print(f"total da compra: R$ {soma:.2f}")

valor_pago = float(input("digite o valor pago: R$ "))

troco = valor_pago - soma

print (f" o troco do cliente é: R${troco:.2f}")
