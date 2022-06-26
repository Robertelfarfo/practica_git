def contador(frase = str):
    palabras = frase.split(" ")
    return "Numero de palabras: " + str(len(palabras))


if __name__ =="__main__":
    print("Da una frase")
    contar = input()
    contador(contar)