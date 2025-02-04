import threading

# Variabili globali per memorizzare i risultati
result1 = 0
result2 = 0

# Funzione per calcolare 5 + 3
def calculate_multiplication():
    global result1
    result1 = 5 + 3 
    print(f"Risultato della moltiplicazione (3 * 4): {result1}")

# Funzione per calcolare 4 - 2
def calculate_subtraction():
    global result2
    result2 = 4 - 2
    print(f"Risultato della sottrazione (5 - 2): {result2}")

# Funzione principale
if __name__ == "__main__":
    # Creazione dei thread
    thread1 = threading.Thread(target=calculate_multiplication)
    thread2 = threading.Thread(target=calculate_subtraction)

    # Avvio dei thread
    thread1.start()
    thread2.start()

    # Attesa del completamento dei thread
    thread1.join()
    thread2.join()

    # Calcolo finale
    final_result = result1 * result2
    print(f"Risultato finale (5 + 3)  * (4 - 2): {final_result}")