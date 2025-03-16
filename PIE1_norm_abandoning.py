from random import uniform, normalvariate
import matplotlib.pyplot as plt
from math import sqrt

def exposa_esquerra(prob: float) -> bool:
    '''Retorna la decisió aleatòria de si exposa contingut de l'esquerra donada la seva probabilitat
    Sinó exposa contingut de la dreta. Prec: 0 <= prob <= 1.'''
    assert 0 <= prob <= 1
    num_aleatori = uniform(0, 1)
    if num_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, l'exposa a l'esquerra
        return True
    return False

def abandona(prob: float) -> bool:
    '''Decideix si abandona o no un usuari depenent de la prob. d'abandonar.'''
    assert 0 <= prob <= 1
    num_aleatori = uniform(0, 1)
    if num_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, abandona.
        return True
    return False

def barres_dicc(data: dict[int, int], regla: str, distribucio: str) -> None:
    '''Dibuixa línea de barres d'un diccionari que emmagetzama els continguts fins a abandonar.
    Al gràfic dibuixat s'especifica la regla utilitzada'''
        
    dades_filtrades = {k: v for k, v in data.items() if k <= 80} # No més de 80 consumicions (molt escàs).
    diccionari_ordenat = sorted(dades_filtrades.items())
    claus, valors = zip(*diccionari_ordenat)

    plt.figure(figsize=(12, 5))
    plt.bar(claus, valors, color='skyblue')

    plt.xlabel(f"Cops que ha consumit l'usuari fins a abandonar")
    plt.ylabel("Freqüència")
    plt.title(f"Continguts consumits a la {distribucio} fins a abandonar segons {regla}.")

    plt.show()

def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    opinions_normal: list[float] = []
    for i in range(10000):
        posicio = normalvariate(0, sqrt(1 / 13))
        if posicio > 1: posicio = 1
        elif posicio < -1: posicio = -1
        opinions_normal.append(posicio)
    
    abandonats_unif_R1: dict[int, int] = {} # Clau: nombre d'exposicions fins a sortir, valor: freqüència de cops que passa la clau.
    abandonats_unif_R2: dict[int, int] = {}
    abandonats_unif_R3: dict[int, int] = {}
    for posicio in opinions_normal: 
        for regla in ["R1", "R2", "R3"]: # Per cada nombre, el modificarem per les 3 regles.
            posicio_actual = posicio
            ha_abandonat = False
            exposicions = 0 # Comptador de les exposicions fins a abandonar. Comença sense cap exposició
            
            while not ha_abandonat:
                if regla == "R1": p_esq = (1 - posicio_actual) ** 2 / ((1 + posicio_actual) ** 2 + (1 - posicio_actual) ** 2) # R1: REFORÇ
                elif regla == "R2": p_esq = (1 - posicio_actual) / 2 # R2: JUSTA
                else: p_esq = (1 + posicio_actual) / 2 # R3: OPOSADA
                
                if exposa_esquerra(p_esq): 
                    if posicio_actual < 0 and abandona(0.05): ha_abandonat = True # Està alineat amb esquerra. P_abandonar = 0.5
                    elif posicio_actual > 0 and abandona(0.25): ha_abandonat = True # No està alineat. P_abandonar = 0.25
                    posicio_actual = posicio_actual - (1 + posicio_actual) / 4 # Canvi a esquerra
                else: 
                    if posicio_actual < 0 and abandona(0.25): ha_abandonat = True # No alineat
                    elif posicio_actual > 0 and abandona(0.05): ha_abandonat = True # Alineat
                    posicio_actual = posicio_actual + (1 - posicio_actual) / 4 # Canvi a dreta
                exposicions += 1

            if regla == "R1" and exposicions in abandonats_unif_R1: abandonats_unif_R1[exposicions] += 1
            elif regla == "R1": abandonats_unif_R1[exposicions] = 1
            elif regla == "R2" and exposicions in abandonats_unif_R2: abandonats_unif_R2[exposicions] += 1
            elif regla == "R2": abandonats_unif_R2[exposicions] = 1
            elif regla == "R3" and exposicions in abandonats_unif_R3: abandonats_unif_R3[exposicions] += 1
            else: abandonats_unif_R3[exposicions] = 1

    barres_dicc(abandonats_unif_R1, "R1", "normal")
    barres_dicc(abandonats_unif_R2, "R2", "normal")
    barres_dicc(abandonats_unif_R3, "R3", "normal")
if __name__ == "__main__":
    main()


