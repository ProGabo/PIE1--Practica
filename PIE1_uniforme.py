from random import uniform, randint
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
    ### NO CONTEMPLEM EL CAS QUE SIGUI IGUAL (NO EXISTEIX TEÒRICAMENT)

def mostra_histograma(dades: list[float], regla: str|None) -> None:
    '''Mostra histograma d'un conjunt de dades que indica la quantitat de posicions polítiques entre esquerra-dreta. 
    Si s'ha utilitzat una regla d'exposició, la mostrem per pantalla.'''

    sns.set_style("whitegrid") # Recrea la graella del gràfic    
    sns.histplot(dades, bins=20, kde=True, color="#007acc", edgecolor="black") 
    
    plt.xlabel("Posicionament polític esquerra-dreta")
    plt.ylabel("Freqüència")
    if regla: plt.title(f"Histograma de la uniforme després d'utilitzar {regla}.") 
    else: plt.title("Histograma de la uniforme inicial.")

    plt.show()

def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    opinions_unif: list[float]
    opinions_unif = [uniform(-1, 1) for _ in range(10000)] # Genera 10000 opinions_unif aleatòries entre -1 i 1.
    mostra_histograma(opinions_unif, None)
    p_esq: float
    posicio: float

    uniform_R1: list[float] = []
    uniform_R2: list[float] = []
    uniform_R3: list[float] = []
    
    for posicio in opinions_unif: 
        for regla in ["R1", "R2", "R3"]: # Per cada nombre, el modificarem per les 3 regles.
            posicio_actual = posicio
            for i in range(15):
                # Canviem la probabilitat de mostrar l'esquerra depenent de cada regla.
                if regla == "R1": 
                    p_esq = (1 - posicio_actual) ** 2 / ((1 + posicio_actual) ** 2 + (1 - posicio_actual) ** 2) # R1: REFORÇ
                elif regla == "R2": p_esq = (1 - posicio_actual) / 2 # R2: JUSTA
                else: p_esq = (1 + posicio_actual) / 2 # R3: OPOSADA
                
                if exposa_esquerra(p_esq): posicio_actual = posicio_actual - (1 + posicio_actual) / 4
                else: posicio_actual = posicio_actual + (1 - posicio_actual) / 4 
    
            if regla == "R1": uniform_R1.append(posicio_actual)
            elif regla == "R2": uniform_R2.append(posicio_actual)
            else: uniform_R3.append(posicio_actual)

    mostra_histograma(uniform_R1, "R1")
    mostra_histograma(uniform_R2, "R2")
    mostra_histograma(uniform_R3, "R3")
    
if __name__ == "__main__":
    main()


