import random, csv


def scegli_parola():
    """funziona che sceglie una parola random da un file 
    contenente tutte le parole del dizionario italiano"""
    file = "azpulito1.csv"
    with open(file) as f:
        parole = [word for word in f]
    parola = random.choice(parole).strip()
    return parola

def scegli_livello():
    """funziona per selezionare la difficoltà del gioco"""
    risposte = ["facile","medio","difficile"]
    while True:
        scelta_livello = input("""che livello vuoi fare?
                           - facile
                           - medio
                           - difficile\n
                           --->""")
        livello = scelta_livello.lower()
        if livello in risposte:
            return livello
        else:
            print("scegli un livello fra quelli indicati")

def facile():
    """funzione che imposta la difficoltà su facile
    accettando solo parole di lunghezza da 4 a 6 lettere"""
    while True:
        vocabolo = scegli_parola()
        if 4 <= len(vocabolo) <= 6:
            gioca(vocabolo,10)
            break
            
def medio():
    """funzione che imposta la difficoltà su medio
    accettando solo parola di lunghezza da 7 a 10 lettere"""
    while True:
        vocabolo = scegli_parola()
        if 7 <= len(vocabolo) <= 10:
            gioca(vocabolo,10)
            break        

def difficile():
    """funzione che imposta la difficoltà su difficile
    accettando solo parola di lunghezza superiore a 10 lettere"""
    while True:
        vocabolo = scegli_parola()
        if len(vocabolo) >= 10:
            gioca(vocabolo,10)
            break
        
def gioca(parola,tentativi):
    """funzione che sviluppa il gioco stampando la parola e contando i tentativi"""
    print(f"hai a disposizione {tentativi} tentativi")
    gioco = True
    i = 0
    lettere_scelte = []
    print(parola[0], end="") #stampo la prima lettera
    for l in parola[1:-1]: #per ogni lettera tra la prima e l'ultima stampo un trattino
        print("_", end="")
        continue
    print(parola[-1]) #stampo l'ultima lettera
    while gioco:
        scelta = input("che lettera vuoi?\n>")
        if len(scelta) > 1: #se l'input è maggiore di una lettera verifico se la parola scritta è quella cercata
            if scelta == parola:
                print(f"complimenti hai trovato la soluzione esatta.'{parola}' era la parola da indovinare")
                break
            else:
                print(f" '{scelta}' non è la soluzione esatta")               
        elif scelta in lettere_scelte: #lettera già scelta
            print("lettera già scelta, occasione persa")
            i += 1
            print(f"hai ancora {tentativi-i} tentativi\n")
        else:
            lettere_scelte.append(scelta)
            print(parola[0], end="")
            for l in parola[1:-1]: #confronto la lettera scelta con le lettere della parola e se uguale le stampo
                if l in lettere_scelte:
                    print(l,end="")
                else:
                    print("_", end="")
            print(parola[-1])
            i += 1 #incremento il numero di tentativi fatti
            print(f"hai ancora {tentativi-i} tentativi\n")
            if i == tentativi:
                soluzione = input("devi dare la soluzione\n-->") #se il n di tenativi corrisponde con quello previsto chiede la soluzione
                if soluzione == parola:
                    print(f"complimenti hai trovato la soluzione esatta.'{parola}' era la parola da indovinare")
                else:
                    print("mi dispiace hai perso")
                    print(f"la parola da indovinare era {parola}")
                    gioco = False

def livello():
    """funzione finale dove in base al livello selezionato lancia il codice appropriato"""
    liv = scegli_livello()
    if liv == "facile":
        facile()
    elif liv == "medio":
        medio()
    else:
        difficile()



if __name__ == "__main__":
    
    livello()

