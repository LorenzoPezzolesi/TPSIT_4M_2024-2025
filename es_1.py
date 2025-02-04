import threading

# Variabili globali 
resultato_1 = 0
risultato_2 = 0


def calcola_somma():
    global result1
    result1 = 5 + 3 
    print(f"Risultato della somma (5 + 3): {result1}")


def calcola_sottrazzione():
    global risultato_2
    risultato_2 = 4 - 2
    print(f"Risultato della sottrazione (4 - 2): {risultato_2}")


if __name__ == "__main__":
    
    thread_1 = threading.Thread(target=calculate_multiplication)
    thread_2 = threading.Thread(target=calculate_subtraction)

    
    thread_1.start()
    thread_2.start()

    
    thread_1.join()
    thread_2.join()

    # Calcolo finale
    risultato_finale = resultato_1 * risultato_2
    print(f"Risultato finale (5 + 3)  * (4 - 2): {risultato_finale}")


