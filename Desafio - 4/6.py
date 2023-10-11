n = int(input("Digite um número inteiro: "))

if n <= 0:
    print("O número deve ser maior que 0.")
else:
    for i in range(1, n + 1, 2):
        print(i)
