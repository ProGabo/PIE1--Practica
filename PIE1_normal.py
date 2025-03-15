from random import uniform, randint, normalvariate
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

def exposa_esquerra(prob: float) -> bool:
    '''Retorna la decisió aleatòria d'exposar contingut de l'esquerra 
    donada la seva probabilitat, sinó exposa contingut de la dreta.'''
    
    assert 0 <= prob <= 1, "Probabilitat fora dels límits [0, 1]"
    num_aleatori = uniform(0, 1) 
    if num_aleatori < prob: # El número aleatòri és contingut per la probabilitat
        return True
    return False


def mostra_histograma(dades: list[float], regla: str, distribucio: str) -> None:
    '''Mostra histograma d'un conjunt de dades que indica la quantitat de posicions polítiques entre esquerra-dreta. 
    Si s'ha utilitzat una regla d'exposició, la mostrem per pantalla.'''

    sns.set_style("whitegrid") # Recrea la graella del gràfic    
    sns.histplot(dades, bins=20, kde=True, color="#007acc", edgecolor="black") 
    
    plt.xlabel("Posicionament polític esquerra-dreta")
    plt.ylabel("Freqüència")
    plt.title(f"Histograma de la normal després d'utilitzar {regla}.") 

    plt.show()

def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    
    opinions_normal: list[float] = []
    for i in range(10000):
        posicio = normalvariate(0, sqrt(1 / 13))
        if posicio > 1: posicio = 1
        elif posicio < -1: posicio = -1
        opinions_normal.append(posicio)


    
    normal_R1: list[float] = []
    normal_R2: list[float] = []
    normal_R3: list[float] = []

    for posicio in opinions_normal: 
        for regla in ["R1", "R2", "R3"]: # Per cada nombre, el modificarem per les 3 regles.
            posicio_actual = posicio # Modifiquem una nova variable, sense tocar la posició original.
            for i in range(15):
                # L'únic que canvia amb cada regla és la probabilitat de mostrar contingut d'esq-dreta.
                if regla == "R1": 
                    p_esq = (1 - posicio_actual) ** 2 / ((1 + posicio_actual) ** 2 + (1 - posicio_actual) ** 2) # R1: REFORÇ
                elif regla == "R2": p_esq = (1 - posicio_actual) / 2 # R2: JUSTA
                else: p_esq = (1 + posicio_actual) / 2 # R3: OPOSADA

                if exposa_esquerra(p_esq): posicio_actual = posicio_actual - (1 + posicio_actual) / 4
                else: posicio_actual = posicio_actual + (1 - posicio_actual) / 4 
    
            if regla == "R1": normal_R1.append(posicio_actual)
            elif regla == "R2": normal_R2.append(posicio_actual)
            else: normal_R3.append(posicio_actual)
    
    
    mostra_histograma(normal_R1, "R1", "normal")
    mostra_histograma(normal_R2, "R2", "normal")
    mostra_histograma(normal_R3, "R3", "normal")

if __name__ == "__main__":
    main()


