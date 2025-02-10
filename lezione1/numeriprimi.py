import libreria_funzioni

number = int(input("dimmi un numero "))

numeri_primi = []

#for i in range(2,  number + 1):
    #is_prime = True
    #for j in range(2, i):
        #if i % j == 0:
            #is_prime = False
    #if is_prime:
        #numeri_primi.append(i)

for i in range(2, number + 1):
    if libreria_funzioni.is_n_prime(i):
        numeri_primi.append(i)

print(numeri_primi)




