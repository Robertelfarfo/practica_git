import pandas as pd 

def contador(frase = str):
    palabras = frase.split(" ")
    return "Numero de palabras: " + str(len(palabras))

def contare_pares(begin = int, saltos = int):
    for x in range(saltos):
        print(begin + x * 2)
    return

def par_impar(numero = int):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("No es par")
    return

def analizis():
    a = pd.DataFrame(data = {"sup": ["Robin","superman","batman","wonderwoman","meave","Raven"],
                             "Poder": [100,900,940,870,901,1000]})
    print(a)
    return

if __name__ =="__main__":
    print("Da una frase")
    contar = input()
    contador(contar)

    par_impar(67)
    analizis()