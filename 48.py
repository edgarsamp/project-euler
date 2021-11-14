MOD = 10000000000
def soma(n):
    soma = 0
    for i in range(1, n+1):
        soma += i**i
        soma %= MOD
    
    return soma

print(str(soma(1000))[-10:])