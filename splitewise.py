
class Spesa:
    """classe con variabile di classe. ogni spesa ha un attributo titolo, pagatore e importo. ha inoltre un attributo propria_quota
che calcola quant'è la quota di quella spesa che rappresnta la quota personale
e si calcola semplicemente dividendo per il numero di persone. il metodo aggiungi
aggiunga la spesa alla lista di classe"""

    lista_spese = []

    def __init__(self,titolo, pagatore, importo):
        self.titolo = titolo
        self.pagatore = pagatore
        self.importo = importo
        self.propria_quota = round(self.importo/Persona.partecipanti,2)

    def __str__(self):
        return f"{self.importo:.2f} € per {self.titolo} pagato da {self.pagatore}"
    
    def aggiungi_spesa(self):
        Spesa.lista_spese.append([self.pagatore,self.importo,self.propria_quota])
    
class Persona:
    """Classe persona con tre variabili di classe, partecipanti per contare le persone,
    totale spese è la somma di tutte le spese effettuate, totale quote singole calcola
    per ogni istanza la somma delle quote delle singole spese di quella persona.
    somma rappresenta il totale speso da una persona tolte le proprie quote, e cioè
    quello che deve ricevere dagli altri"""

    partecipanti = 0
    totale_spese = 0
    totale_quote_singole = 0

    def __init__(self, nome):
        self.nome = nome
        self.somma=0
        self.quota_spesa = 0
        self.tot_dare = 0
        Persona.partecipanti +=1
        

    def __repr__(self):
        return f"{self.nome}"

    def aggiungi(self,spesa,quota):
        """metodo per incrementare i vari totali"""
        self.somma += round(spesa - quota,2) #aggiungo a somma il valore della spesa- la quota personale
        Persona.totale_spese += spesa #aggiungo la spesa al totale
        Persona.totale_quote_singole += quota #aggiungo la quota al tot quote
        self.quota_spesa += quota #aggiungo la quota al tot quote di ogni persona
        
    def dare(self):
        """metodo che calcola quanto ognuno deve dare agli altri. togliendo le quote
        personali dalle quote totali"""
        self.tot_dare = round(Persona.totale_quote_singole - self.quota_spesa,2)
        
def aggiungi_partecipante():
    """funzione per creare istanze persone con dati inseriti dall'utente"""
    gruppo = []
    contatore = 0
    #ciclo che mi permette di poter inserire n utenti a piacimento
    while True: 
        if len(gruppo)==0:
            nome = input("inserisci il nome del partecipante:\n-->").lower()
        else:
            aggiungi = input("vuoi aggiungere un altro partecipante?s/n\n-->").lower()
            if aggiungi == "s":
                # qui si potrebbe implementare un controllo errori
                nome = input("inserisci il nome del partecipante:\n-->").lower()
            else:
                break
        contatore +=1
        p = "p"+str(contatore) #attribuisco un nome univoco a ogni elemento
        p=Persona(nome) #creo istanza di classe
        gruppo.append(p)
        # print(p)
    return gruppo    

def inserisci_spesa():
    """funzione per inserire le spese effettuate partendo dai dati inseriti dall'utente"""
    tutti = aggiungi_partecipante()
    print(tutti)
    contatore = 0
    sp = "sp"+str(contatore) #attribuisco nome univoco
    #ciclo che mi permette di poter inserire n spese a piacimento
    while True:
        nuova_spesa = input("vuoi aggiungere una spesa?s/n\n-->").lower()
        if nuova_spesa == "s":
            # qui si potrebbe implementare un controllo errori
            spesa = input("che spesa è stata fatta?\n-->")
            ammontare = float(input("a quanto ammonta la spesa?\n-->"))
            pagante = input("chi ha pagato?\n-->").lower()
            #ciclo for per aggiungere il nome pagante come argomento per creare istanza passato a sua volta come istanza
            for nome in tutti:
                if nome.nome == pagante:
                    contatore += 1
                    sp = Spesa(spesa,nome,ammontare) #creo istanza di classe
                    sp.aggiungi_spesa() #lancio metodo di classe 
                    # print(Spesa.lista_spese)      
        else:
            break     
    return tutti

def spesa_partecipante():
    """funzione che lancia il metodo aggiungi della classe persona
    per ogni persona contenuta nelle varie liste che compongo la lista delle spese"""
    for spesa in Spesa.lista_spese:
        spesa[0].aggiungi(spesa[1],spesa[2])

def calcolo_finale():
    """funzione cha calcola quanto ognuo deve dare  e/o ricevere e abbina i pagamenti
    in modo che siano il minor numero possibile"""
    gruppo = inserisci_spesa() #attribuisco il return alla variabile gruppo
    spesa_partecipante() #lancio il metodo
    creditori = {}
    debitori = {}
    for persona in gruppo: #per ogni persona lancio il metodo dare
        persona.dare()
        creditori[persona] = persona.somma #creo dict con chiave nome, e valore quanto deve ricevere
        debitori[persona] = persona.tot_dare #creo dict con chiave nome, e valore quanto deve dare

    set_creditori = set(creditori) #trasformo i dict in set per operare con gli insiemi
    set_debitori  = set(debitori)
    entrambi = set_creditori & set_debitori #trovo l'intersezione tra i due set

        # se la persona è presente nell'intersezione vuol dire che deve sia dare che ricevere,
        # quindi trovato il minimo tra credito e debito lo sottraggo al valore più grande
        # in modo da azzerare quello più piccolo,poi elimino l'elemento con valore zero
    for membro in entrambi: 
        credito = creditori[membro]
        debito = debitori[membro]
        if credito > debito:
            creditori[membro] = credito - debito
            debitori.pop(membro)
        else:
            debitori[membro]= debito - credito
            creditori.pop(membro)
    # print("creditori",creditori)
    # print("debitori", debitori)

    # ciclo in cui trovo il max valore tra i creditori, il max fra i debitori e sottraggo
    # il valore minimo fra i due sia al valore del creditore che del debitore e assegno
    # i nuovi valori alle chiave corrispondenti. lo faccio per x volte finche tutti hanno
    # pagato il loro debito
    fine = False
    while fine == False: 
        maxc = max(creditori.values())
        maxd = max(debitori.values())
        cre = [c for c,v in creditori.items() if v == maxc] #trovo la chiave corrispondente al max
        deb = [c for c,v in debitori.items() if v == maxd] #trovo la chiave corrispondente al max
        minimo = min(maxc,maxd)
        if minimo == 0:
            fine = True
        else:
            print(f"{deb} deve dare {minimo:.2f} € a {cre}") 
            for c,v in debitori.items(): #aggiorno i valori sottraendo il valore minimo
                if v == maxd:
                    debitori[c] = v-minimo   
            for c,v in creditori.items():
                if v == maxc:
                    creditori[c] = v- minimo
    # print("creditori",creditori)
    # print("debitori", debitori)

if __name__ == "__main__":
    calcolo_finale()
    
