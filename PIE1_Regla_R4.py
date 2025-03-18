from random import uniform, normalvariate
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

def exposa_esquerra(prob: float) -> bool:
    '''Retorna la decisió aleatòria de si exposa contingut de l'esquerra donada la seva probabilitat.
    Sinó exposa contingut de la dreta. Prec: 0 <= prob <= 1.'''
    assert 0 <= prob <= 1, "Probabilitat NO normalitzada entre [0, 1]"
    num_aleatori = uniform(0, 1)
    if num_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, l'exposa a l'esquerra
        return True
    return False

def abandona(prob: float) -> bool:
    '''Retorna la decisió aleatòria de si exposa contingut de l'esquerra donada la seva probabilitat.
    Sinó exposa contingut de la dreta. Prec: 0 <= prob <= 1.'''
    assert 0 <= prob <= 1, "Probabilitat NO normalitzada entre [0, 1]"
    num_aleatori = uniform(0, 1)
    if num_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, l'exposa a l'esquerra
        return True
    return False

def mostra_histograma(dades: list[float], regla: str, distribucio: str) -> None:
    '''Mostra histograma d'un conjunt de dades que indica la quantitat de posicions polítiques entre esquerra-dreta. 
    Si s'ha utilitzat una regla d'exposició, la mostrem per pantalla.'''

    sns.set_style("whitegrid") # Recrea la graella del gràfic    
    sns.histplot(dades, bins=20, kde=True, color="#007acc", edgecolor="black") 
    
    plt.xlabel("Posicionament polític esquerra-dreta")
    plt.ylabel("Freqüència")
    plt.title(f"Histograma de la {distribucio} després d'utilitzar {regla}.") 

    plt.show()

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


def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    opinions_unif = [uniform(-1, 1) for _ in range(10000)] # Genera 10000 opinions_unif aleatòries entre -1 i 1.
    opinions_normal: list[float] = []
    for i in range(10000):
        posicio = normalvariate(0, sqrt(1 / 13))
        if posicio > 1: posicio = 1
        elif posicio < -1: posicio = -1
        opinions_normal.append(posicio)
    uniform_R4: list[float] = []
    norm_R4: list[float] = []
    
    for posicio in opinions_unif: 
            for i in range(15):
                if exposa_esquerra(0.5): posicio = posicio - (1 + posicio) / 4
                else: posicio = posicio + (1 - posicio) / 4 
            uniform_R4.append(posicio)

    for posicio in opinions_normal: 
            for i in range(15):
                if exposa_esquerra(0.5): posicio = posicio - (1 + posicio) / 4
                else: posicio = posicio + (1 - posicio) / 4 
            norm_R4.append(posicio)

    mostra_histograma(uniform_R4, "R4", "uniforme")
    mostra_histograma(norm_R4, "R4", "normal")
    
if __name__ == "__main__":
    main()


