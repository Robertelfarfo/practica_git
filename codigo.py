def contador(frase = str):
    palabras = frase.split(" ")
    return "Numero de palabras: " + str(len(palabras))

def contare_pares(begin = int, saltos = int):
    for x in range(saltos):
        print(begin + x * 2)
    return

if __name__ =="__main__":
    print("Da una frase")
    contar = input()
    contador(contar)