import time


def primos():
    start = time.time()
    lista_primos = []
    lista_div = []
    for x in range(2, int(opcao)+1):
        for n in range(1, x+1):
            if x >= n:
                if x % n == 0:
                    lista_div.append(n)
        if len(lista_div) == 2:
            lista_primos.append(x)
        lista_div = []
    end = time.time()
    execution_time = end - start

    print(f"Os números primos até {opcao}, são: {lista_primos}\n")
    print("Tempo de exucução: %0.2f ms\n\n" % (execution_time))


opcao = 0

while opcao != "sair":
    print("************ Verificando números primos *************\n")
    try:
        opcao = input("Informe um numero, ou digite sair: ")
        print()
        if opcao != "sair":
            primos()
    except ValueError:
        opcao = input("Informe um numero, ou digite sair: ")
        print()
        primos()


print("********************** Sistema encerrado! ************************\n\n")
