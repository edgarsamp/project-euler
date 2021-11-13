def multiples3or5(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0:
            sum += i
        if i % 5 == 0:
            sum += i
        if i % 3 == 0 and i % 5 == 0:
            sum -= i
    return(sum)

def multiples3or5faster(n):
    n-=1 #Como tem que ser menor que n
    #soma dos n termos da pa = (a1+an)*n/2
    soma_mult3 = int((3+(n//3)*3)*(n//3)/2) #(n//3)*3 n-esimo termo
    soma_mult5 = int((5+(n//5)*5)*(n//5)/2)
    soma_mult15 = int((15+(n//15)*15)*(n//15)/2)
    
    return soma_mult3+soma_mult5-soma_mult15

print(multiples3or5faster(10))
print(multiples3or5faster(1000))