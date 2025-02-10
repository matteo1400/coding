import libreria_funzioni

number = int(input("dimmi un numero: "))

lista = []

for i in range(1 , number + 1):
    lista.append(libreria_funzioni.fibonacci(i))


print(f"i primi n termini della successione di fibonacci sono {lista}")