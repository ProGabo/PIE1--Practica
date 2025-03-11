from random import uniform, randint
import matplotlib.pyplot as plt

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

def main() -> None:
    '''Executa el programa PRINCIPAL.'''
    nombres: list[float] = [uniform(-1, 1) for _ in range(10000)] # Genera 10000 nombres aleatòries entre 0 i 1.
    mostra_histograma(nombres, None)
    
    uniform_R1: list[float] = []
    uniform_R2: list[float] = []
    uniform_R3: list[float] = []
    
    for num in nombres: 
        for regla in ["R1", "R2", "R3"]: # Per cada nombre, el modificarem per les 3 regles.
            num_actual = num
            for i in range(15):
                # L'únic que canvia amb cada regla és la probabilitat de mostrar contingut d'esq-dreta.
                if regla == "R1": p_esq = (1 - num_actual) ** 2 / ((1 + num_actual) ** 2 + (1 - num_actual) ** 2) # Regla de REFORÇAMENT
                elif regla == "R2": p_esq = (1 - num_actual) / 2 # Regla JUSTA
                else: p_esq = (1 + num_actual) / 2 # Regla OPOSADA
                assert 0 <= p_esq <= 1, "Probabilitat NO normalitzada entre [0, 1]"
                
                if exposa_esquerra(p_esq): num_actual = num_actual - (1 + num_actual) / 4
                else: num_actual = num_actual + (1 - num_actual) / 4 
    
            if regla == "R1": uniform_R1.append(num_actual)
            elif regla == "R2": uniform_R2.append(num_actual)
            else: uniform_R3.append(num_actual)
    mostra_histograma(uniform_R1, "R1")
    mostra_histograma(uniform_R2, "R2")
    mostra_histograma(uniform_R3, "R3")
    
if __name__ == "__main__":
    main()


