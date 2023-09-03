import math

"""
    En este archivo se encuentra el ejercicio 6 de la guía de algoritmos 
    
    Entendimiento del problema: 
        Buscar los numeros de carmichael. 
   
    Definicion de los numeros de carmichael: 
        Son numeros factorizables por numeros primos.
        Segun lo que comprendi es que al menos tienen que ser factorizables por 3 numeros primos
     
    Proceso de Divide And Conquer: 
        - Saber si 'n' numero es primo: 
            Dos definiciones de numeros primos: 
                - Numero que solo es divisible por si mismo y 1
                - !!!! Todo numero primo no es divisible por otros numeros primos ¡¡¡
        - Armado de listado de numeros primos: 
        - Factorizacion de numeros: 
            Debido a que no hay un limite de posibles factorizaciones preferí hacerla recursiva
            
    
       
    Problemas a resolver: 
        Primarios: 
            - Considero que un numero no es Carmichaeleano cuando la computadora tira un Exception de recursion: 
                - Error que sucede cuando el Arbol generado es Enorme en serio 
                    quizas es solucionable pero no se me ocurrio alguna solucion
                
                
            - No sabría como decirle al caso base que quiero que me considere solo los numeros 
                charmichaeleanos son los que se factorizan por 3 o mas numeros primos
                
                Se me ocurrieron dos posibles soluciones "basicas" pero no sabría si estarían bien, ya que en caso
                de factorizar un numero y generar una rama que no lleve a nada no sabría como deshacerlo: 
                    La primera es un indice de cuantas veces se factorizo 
                    La segunda sería agregar una lista o puntero a una lista que en el cual puede ir agregando los numeros
                        por los que se factorizo, la cantidad de elementos podría cumplir el rol del indice que mencione
                        en la primera solucion
        Secundarios:             
                - Debido a que la Funcion es recursiva no se cuales fueron los numeros por los que se pudo factorizar, el numero evaluado. 
                
                - No pude hacer que el numero que se imprima en el caso base sea el que se factorizo y no 1: 
                        tiene sentido por como funciona la funcion recursiva y la generacion de bloques de memoria
    
    Mejoras: 
        - En vez de imprimir las factorizaciones ver de como devolverlas
        - No tener que hardcodear los primeros numeros primos
        - Pedir ayuda o debatir en relacion a como podría encararse con un enfoque parecido al perlocation 
            y los diferentes caminos 
"""
def main():
    primos = []
    # Hardcodeo los primeros 4 numeros primos
    primos.append(2)
    primos.append(3)
    primos.append(5)
    primos.append(7)
    # Establesco el limite de mi busqueda de numeros de charmichael
    NumeroLimite=10000
    # Busco los numeros primos hasta ese NumeroLimite
    primos = Reconocer_Primos_Hasta_n(NumeroLimite, primos)

    #Busco la factorizacion de los diferentes numeros hasta el NumeroLimite
    for i in range(NumeroLimite):
        try:
            Numeros_de_carmiel(primos, i)
        except RecursionError as error:
            print("El numero ingresado no es Carmicheleano")


def Numeros_de_carmiel(Lista_num_Prim, Aux, indice=0):
    """ Numeros_de_carmichael funcion recursiva principal

        Args:
            Lista_num_Prim:
                Es la lista de numeros primos necesaria para poder evaluar las diferentes factorizaciones
            Aux:
                Numero a ser Factorizado
            Indice:
                Indice de la Lista_num_Prim
        Returns:
            1 en caso base
            Habría que tener algun return mas

    """
    if Aux == 1:
        print("Se encontro que el numero es Carmicheleano"+str(Aux)+" y es factorizable por los numeros de arriba")
        return 1
    if Aux % Lista_num_Prim[indice] == 0:
        print("Se divide por: " + str(Lista_num_Prim[indice]))
        Numeros_de_carmiel(Lista_num_Prim, Aux / Lista_num_Prim[indice],indice+1)
    else:
        Numeros_de_carmiel(Lista_num_Prim, Aux, indice + 1)


def Imprimir_Lista(Lista):
    """

    :param Lista:
        Lista a imprimir
    :returns:
        Nullo
    """
    for i in range(0, len(Lista)):
        print(str(Lista[i]))

def Reconocer_Primos_Hasta_n(n, Lista_primos):
    """
        Reconocer_Primos_Hasta_n es una funcion vortice para resolver el problema ya que necesito saber cuales son
        los numeros primos
    :param n:
        El limite que tengo para encontrar los numeros primos
    :param Lista_primos:
        Lista de primos encontrados previamente
    :return:
        Lista de primos completa
    """
    # esta funcion devuelve los numeros primos hasta la n que no se habían considerado
    for i in range(2, n):
        Lista_aux = Hallar_un_primo(i, Lista_primos)
        Lista_primos = Lista_aux
    return Lista_primos

def Hallar_un_primo(n, lista_primos):
    """
    Hallar_un_primo es una funcion Vertice que me permite saber si un numero es primo o no
    :param n:
        Elemento a ser evaluado
    :param lista_primos:
        Lista con los numeros primos previos
    :return:
        Si el numero es primos se agrega a la lista y se devuelve esa lista
    """
    flag_resto_distinto_0 = False
    for i in range(0, len(lista_primos)):
        if n % lista_primos[i] == 0 and i != lista_primos[i]:
            flag_resto_distinto_0 = True
    if not flag_resto_distinto_0 and n != 1:
        print("Se agrego el numero primo: "+str(n))
        lista_primos.append(n)
    return lista_primos

if __name__ == '__main__':
    main()

