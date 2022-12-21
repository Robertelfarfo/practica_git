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
    print("Ahora solo los superheroes con poder mayor a 870")

    b = a[a["Poder"] >= 870]
    print(b)
    return

if __name__ =="__main__":
    print("Da una frase")
    contar = input()
    print(contador(contar))

    print("El numero 81: ", par_impar(81))
    analizis()
    print("Aqui impirmo un Hola 2.0")
