from random import uniform, randint, normalvariate
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

def exposa_esquerra_norm(prob: float) -> bool:
    '''Retorna la decisió aleatòria de si exposa contingut de l'esquerra donada la seva probabilitat, sinó exposa contingut de la dreta. Prec: La probabilitat ve d'una distribució normal.'''
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

def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    nombres: list[float] = [normalvariate(0, sqrt(1 / 13)) for _ in range(10000)]
    mostra_histograma(nombres, None)
    normal_R1: list[float] = []
    normal_R2: list[float] = []
    normal_R3: list[float] = []

    for num in nombres: 
        for regla in ["R1", "R2", "R3"]: # Per cada nombre, el modificarem per les 3 regles.
            num_actual = num
            for i in range(15):
                # L'únic que canvia amb cada regla és la probabilitat de mostrar contingut d'esq-dreta.
                if regla == "R1": p_esq = (1 - num_actual) ** 2 / ((1 + num_actual) ** 2 + (1 - num_actual) ** 2) # Regla de REFORÇAMENT
                elif regla == "R2": p_esq = (1 - num_actual) / 2 # Regla JUSTA
                else: p_esq = (1 + num_actual) / 2 # Regla OPOSADA
                ##### OJO LA NORMAL NO ESTÀ FITADA PER [0, 1], TOCA ESTABLIR UN CONVENI.
                ##### SI X > 1 (FULL DRETA), SUPOSEM NO HI HA PROBABILITAT D'ANAR MÉS CAP A LA DRETA, HAURÀ D'ANAR 100% A L'ESQUERRA
                ##### SI X < 1 (FULL ESQ), SUPOSEM NO HI HA PROBABILITAT D'ANAR MÉS CAP A L'ESQUERRA, HAURÀ D'ANAR 100% A LA DRETA.
                if exposa_esquerra_norm(p_esq): num_actual = num_actual - (1 + num_actual) / 4
                else: num_actual = num_actual + (1 - num_actual) / 4 
    
            if regla == "R1": normal_R1.append(num_actual)
            elif regla == "R2": normal_R2.append(num_actual)
            else: normal_R3.append(num_actual)
    mostra_histograma(normal_R1, "R1")
    mostra_histograma(normal_R2, "R2")
    mostra_histograma(normal_R3, "R3")

if __name__ == "__main__":
    main()


