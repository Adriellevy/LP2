# This is a sample Python script.
import math


def main():
    primos = []

    # Seteo el patron que me interesa y en este caso es los numeros primos y para eso cargo los primeros 4
    primos.append(2)
    primos.append(3)
    primos.append(5)
    primos.append(7)
    # primos = Hallar_un_primo(7,primos)
    # Imprimir_Lista(primos)
    primos = Reconocer_Primos_Hasta_n(10000, primos)
    Numeros_de_carmiel(primos, 10000)
    # Maximo Comun Divisor de la Librería Math
    # Maximo comun divisior responde a la ¿pregunta cual
    # es el numero que divide a ambos numeros con resto 0?


def Numeros_de_carmiel(Lista_num_Prim, Aux, indice=0):
    #pedir ayuda a francisco en relacion a como hacia el tema del perlocation
    if Aux == 1:
        print("Se encontro un numero")
        return 1
    if Aux % Lista_num_Prim[indice] == 0:
        print("Se divide por: " + str(Lista_num_Prim[indice]))
        Numeros_de_carmiel(Lista_num_Prim, Aux / Lista_num_Prim[indice],indice+1)
    else:
        Numeros_de_carmiel(Lista_num_Prim, Aux, indice + 1)

    """
        if math.gcd(Num,pow(i,Lista_num_Prim[i]-1))==1:
            Posible_lista_Num_primos_a_fin.append(i)
            #print("Numero de carmichael es: "+str(i))

                #significa que el numero tiene que ser divisible por 3 numeros primos
        #sigo en el bucle hasta que encuentre los numeros que factorizan el
    
    Flag_resulto=False
    contador=2
    while Flag_resulto == False:
        if math.gcd(Aux/Lista_num_Prim[contador],pow(contador,Lista_num_Prim[contador]) ==1"""


def Imprimir_Lista(Lista):
    for i in range(0, len(Lista)):
        print(str(Lista[i]))


def Reconocer_Primos_Hasta_n(n, Lista_primos):
    # esta funcion devuelve los numeros primos hasta la n que no se habían considerado
    for i in range(2, n):
        Lista_aux = Hallar_un_primo(i, Lista_primos)
        Lista_primos = Lista_aux
    return Lista_primos


def Hallar_un_primo(n, lista_primos):
    flag_resto_distinto_0 = False
    for i in range(0, len(lista_primos)):
        if n % lista_primos[i] == 0 and i != lista_primos[i]:
            flag_resto_distinto_0 = True
    if not flag_resto_distinto_0 and n != 1:
        print("Se agrego el numero primo: "+str(n))
        lista_primos.append(n)
    return lista_primos


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
