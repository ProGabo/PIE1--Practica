from random import uniform, normalvariate, randint
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt



def exposa_esquerra(prob: float) -> bool:
    '''Retorna la decisió aleatòria de si exposa contingut de l'esquerra donada la seva probabilitat, sinó exposa contingut de la dreta. Prec: 0 <= prob <= 1.'''
    num_aleatori = uniform(0, 1)
    if num_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, l'exposa a l'esquerra
        return True
    return False
    ### NO CONTEMPLEM EL CAS QUE SIGUI IGUAL (NO EXISTEIX TEÒRICAMENT)

def mostra_histograma(dades: list[float], regla: str|None) -> None:
    '''Mostra histograma d'un conjunt de dades que indica la quantitat de posicions polítiques entre esquerra-dreta. Si s'ha utilitzat una regla d'exposició, la mostrem per pantalla.'''
    plt.hist(dades, bins=10, color="royalblue", edgecolor="black")
    
    plt.xlabel("Posicionament polític esquerra-dreta")
    plt.ylabel("Freqüència")
    plt.title(f"Histograma de la uniforme després d'utilitzar {regla}.") if regla else plt.title("Histograma de la uniforme inicial.")

    plt.show()

def abandona(prob: float) -> bool:
    '''Decideix si abandona o no un usuari depenent de la prob. d'abandonar.'''
    assert 0 <= prob <= 1
    num_aleatori = uniform(0, 1)
    if num_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, l'exposa a l'esquerra
        return True
    return False

def barres_dicc(data: dict[int, int]) -> None:
    '''Dibuixa línea de barres d'un diccionari'''    
    filtered_data = {k: v for k, v in data.items() if k <= 100}

    # Ordenar por clave
    sorted_items = sorted(filtered_data.items())
    keys, values = zip(*sorted_items)

    # Graficar
    plt.figure(figsize=(12, 5))
    plt.bar(keys, values, color='skyblue')

    # Etiquetas
    plt.xlabel("Clave")
    plt.ylabel("Valor")
    plt.title("Gráfico de barras (claves ≤ 100)")

    # Mostrar
    plt.show()


def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    nombres: list[float] = []
    for i in range(10000):
        num = normalvariate(0, sqrt(1 / 13))
        if num > 1: num = 1
        elif num < -1: num = -1
        nombres.append(num)
    mostra_histograma(nombres, None)
    
    abandonats_R1: dict[int, int] = {}
    abandonats_R2: dict[int, int] = {}
    abandonats_R3: dict[int, int] = {}
    for num in nombres: 
        for regla in ["R1", "R2", "R3"]: # Per cada nombre, el modificarem per les 3 regles.
            num_actual = num
            ha_abandonat = False
            exposicions = -1 # Abandona un cop l'exposes, comença a la 1a exposició.
            while not ha_abandonat:
                # L'únic que canvia amb cada regla és la probabilitat de mostrar contingut d'esq-dreta.
                if regla == "R1": p_esq = (1 - num_actual) ** 2 / ((1 + num_actual) ** 2 + (1 - num_actual) ** 2) # Regla de REFORÇAMENT
                elif regla == "R2": p_esq = (1 - num_actual) / 2 # Regla JUSTA
                else: p_esq = (1 + num_actual) / 2 # Regla OPOSADA
                assert 0 <= p_esq <= 1, "Probabilitat NO normalitzada entre [0, 1]"
                
                if exposa_esquerra(p_esq): 
                    if num_actual < 0: # Està alineat
                        p_aband = 0.05
                        if abandona(p_aband): ha_abandonat = True
                    else: # No està alineat
                        p_aband = 0.25
                        if abandona(p_aband): ha_abandonat = True
                    num_actual = num_actual - (1 + num_actual) / 4 # Després canviem la seva posició
                else: # Exposa la dreta
                    if num_actual > 0: # Està alineat
                        p_aband = 0.05
                        if abandona(p_aband): ha_abandonat = True
                    else: # No està alineat
                        p_aband = 0.25
                        if abandona(p_aband): ha_abandonat = True
                    num_actual = num_actual + (1 - num_actual) / 4 
                exposicions += 1
            if regla == "R1":
                if exposicions in abandonats_R1:
                    abandonats_R1[exposicions] += 1
                else: abandonats_R1[exposicions] = 1
            
            elif regla == "R2":
                if exposicions in abandonats_R2:
                    abandonats_R2[exposicions] += 1
                else: abandonats_R2[exposicions] = 1
            else:
                if exposicions in abandonats_R3:
                    abandonats_R3[exposicions] += 1
                else: abandonats_R3[exposicions] = 1
    barres_dicc(abandonats_R1)
    barres_dicc(abandonats_R2)
    barres_dicc(abandonats_R3)
if __name__ == "__main__":
    main()


