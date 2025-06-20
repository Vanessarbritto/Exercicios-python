# 6- Entrar via teclado com o valor da cotação do dólar
# e uma certa quantidade de dólares. Calcular e exibir o valor 
# correspondente em Reais (R$).

cotacao = float(input("digite a cotacao do dolar:"))

quantidade = float(input("digite a quantidade de dolares:"))

valor_em_reais = cotacao * quantidade

print(f"Valor em reais: R${valor_em_reais:.2f}")
