from random import uniform, randint
import matplotlib.pyplot as plt
# Generem 10000 números aleatoris de la uniforme

def exposa_esquerra(prob: float) -> bool:
    '''Retorna la decisió aleatòria de si exposa contingut de l'esquerra donada la seva probabilitat, sinó exposa contingut de la dreta. Prec: 0 <= prob <= 1.'''
    num_aleatori = uniform(0, 1)
    if num_aleatori < prob: # Si la probabilitat conté el nombre generat aleatòriament, l'exposa a l'esquerra
        return True
    return False
    ### NO CONTEMPLEM EL CAS QUE SIGUI IGUAL (NO EXISTEIX TEÒRICAMENT)

def mostra_histograma(dades: list[float]) -> None:
    '''Mostra histograma d'un conjunt de dades.'''
    plt.hist(dades, bins=10, color="royalblue", edgecolor="black")
    
    plt.xlabel("Posicionament polític esquerra-dreta")
    plt.ylabel("Frequencia")
    plt.title("Histograma segons R1, seguint la uniforme")

    plt.show()

def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    nombres: list[float] = [uniform(-1, 1) for _ in range(10000)]
    mostra_histograma(nombres)
    uniform_R1: list[float] = []

    # R1: REINFORCEMENT RULE
    for num in nombres:
        for i in range(15):
            p_esq = (1 - num) ** 2 / ((1 + num) ** 2 + (1 - num) ** 2)
            assert 0 <= p_esq <= 1, "Probabilitat NO normalitzada."
            if exposa_esquerra(p_esq):
                num = num - (1 + num) / 4
            
            else:
                num = num + (1 - num) / 4 
        uniform_R1.append(num) # Un cop acabades les 15, afegim el número a la nova distribució.
    mostra_histograma(uniform_R1)
if __name__ == "__main__":
    main()


