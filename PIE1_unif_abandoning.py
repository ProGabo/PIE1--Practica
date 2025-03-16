from random import uniform
import matplotlib.pyplot as plt

def exposa_esquerra(prob: float) -> bool:
    '''Retorna la decisió aleatòria de si exposa contingut de l'esquerra donada la seva probabilitat, sinó exposa contingut de la dreta. Prec: 0 <= prob <= 1.'''
    posicio_aleatori = uniform(0, 1)
    if posicio_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, l'exposa a l'esquerra
        return True
    return False

def abandona(prob: float) -> bool:
    '''Decideix si abandona o no un usuari depenent de la prob. d'abandonar.'''
    assert 0 <= prob <= 1
    posicio_aleatori = uniform(0, 1)
    if posicio_aleatori < prob: # Si la probabilitat (límit superior de [0, 1]) conté el nombre aleatori entre 0 i 1, l'exposa a l'esquerra
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
    opinions_unif: list[float] = [uniform(-1, 1) for _ in range(10000)] # Genera 10000 opinions_unif aleatòries entre 0 i 1.   
    abandonats_R1: dict[int, int] = {}
    abandonats_R2: dict[int, int] = {}
    abandonats_R3: dict[int, int] = {}
    
    for posicio in opinions_unif: 
        for regla in ["R1", "R2", "R3"]: # Per cada nombre, el modificarem per les 3 regles.
            posicio_actual = posicio
            ha_abandonat = False
            exposicions = 0 # Abandona un cop l'exposes, comença a la 1a exposició.
            while not ha_abandonat:
                # L'únic que canvia amb cada regla és la probabilitat de mostrar contingut d'esq-dreta.
                if regla == "R1": p_esq = (1 - posicio_actual) ** 2 / ((1 + posicio_actual) ** 2 + (1 - posicio_actual) ** 2) # Regla de REFORÇAMENT
                elif regla == "R2": p_esq = (1 - posicio_actual) / 2 # Regla JUSTA
                else: p_esq = (1 + posicio_actual) / 2 # Regla OPOSADA
                assert 0 <= p_esq <= 1, "Probabilitat NO normalitzada entre [0, 1]"
                
                if exposa_esquerra(p_esq): 
                    if posicio_actual < 0 and abandona(0.05): ha_abandonat = True # Està alineat amb esquerra. P_abandonar = 0.5
                    elif posicio_actual > 0 and abandona(0.25): ha_abandonat = True # No està alineat. P_abandonar = 0.25
                    posicio_actual = posicio_actual - (1 + posicio_actual) / 4 # Canvi a esquerra
                else: 
                    if posicio_actual < 0 and abandona(0.25): ha_abandonat = True # No alineat
                    elif posicio_actual > 0 and abandona(0.05): ha_abandonat = True # Alineat
                    posicio_actual = posicio_actual + (1 - posicio_actual) / 4 # Canvi a dreta
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
    barres_dicc(abandonats_R1, "R1", "uniforme")
    barres_dicc(abandonats_R2, "R2", "uniforme")
    barres_dicc(abandonats_R3, "R3", "uniforme")
if __name__ == "__main__":
    main()


