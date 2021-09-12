import sys, os
sys.path.append("..")
from ordine import *
from classifier import *
from search import *
from regression import *

import warnings
warnings.filterwarnings("ignore")

peso = 0
routes = []
storico_des = []

veicolo = seleziona_mezzo()
wind = simula_cond_atmosferiche()
orario = simula_orario()
dist_parziale = 0
dist_totale = 0

# tiene traccia della scelta effettuata dall'utente
scelta = 0

# tiene traccia del numero di esecuzioni effettuate
esecuzioni = 0
partenza = ''

print('----------------------------- Warehouse Manager ----------------------------- ')
while(scelta != 2):
    print('Ordine Gestito n°',esecuzioni+1, '\n')

    if(esecuzioni == 0 or scelta == 1):
        # viene utilizzata per evitare di generare le stesse destinazioni
        flag = False

        while(flag == False):
            des = genera_destinazione()
            if des not in storico_des:
                storico_des.append(des)
                print("L'ordine deve essere consegnato a:", des, '\n')
                flag = True

        # genera l'ordine
        prod = genera_ordine(des)
        mostra_ordine(prod)

        # calcola il peso degli ordini
        peso += getPeso(prod)
        print("Il peso complessivo dell'ordine è pari a: ", peso, 'kg\n')

        # mostra le categorie
        categorie = getCategorie(prod)

        # classifica l'ordine ricevuto
        print("Indicazioni per l'imballaggio:")
        bayes_laplace(categorie)
        
        #imposta il punto di partenza
        if(esecuzioni == 0):
            partenza = 'magazzino'

        # trasforma la mappa in un grafo
        G = get_grafo()
        
        # prende le coordinate del nodo di partenza e arrivo
        c_start = get_coordinate(partenza)
        c_des = get_coordinate(des)

        # prende il nodo di partenza
        n_start = get_nodo(G, c_start['y'], c_start['x'])
        
        # prende il nodo obiettivo
        n_des = get_nodo(G, c_des['y'], c_des['x'])

        if(esecuzioni == 0):
            # calcola il percorso con l'algoritmo a*
            route = percorso_astar(G, n_start, n_des)
            # mostra il percorso sulla mappa
            plot_percorso(G, route, esecuzioni)
            # inserisce il percorso nella lista di tutte le tappe
            routes.append(route)
            # calcola la distanza da percorrere
            dist_parziale = lunghezza_percorso(G, n_start, n_des)
            print('La distanza stimata da percorrere è:', round(dist_parziale,1), 'm')
            dist_totale = dist_parziale
            
        if(esecuzioni > 0):
            # calcola il percorso con l'algoritmo a*
            route = percorso_astar(G, n_start, n_des)
            # aggiunge il percorso alla lista di tutte le tappe
            routes.append(route)
            # mostra i percorsi sulla mappa    
            plot_percorso(G, routes, esecuzioni)
            # calcola la distanza da percorrere
            dist_parziale = lunghezza_percorso(G, n_start, n_des)
            print("La distanza stimata dell'ultimo tratto da percorrere è:", round(dist_parziale),'m')
            # tiene traccia della distanza totale
            dist_totale += dist_parziale

        # stampa le indicazioni relative alla mappa
        print('Le indicazioni per andare da', partenza, 'a', des, 'sono: ')
        stampa_indicazioni(G, route)

        pred = predizione(veicolo['id'], peso, wind, orario)

        if(wind==0):
            vento = 'assente/trascurabile'
        else:
            vento = 'presente'

        print("In base alle condizioni:\n",'Veicolo:',veicolo['modello'],'\n','Peso:',peso,'kg',
                'Vento:', vento,'Orario:',orario )
        print("\nIl consumo di carburante stimato in base alle condizioni è di:",pred,'l/100km')
        print("Il costo del carburante per la consegna ammonta a: €", round(costo_consegna(dist_totale, pred),2),'\n')

        esecuzioni += 1
        partenza = des

        if(esecuzioni == 5):
            print('Non ci sono ulteriori ordini da gestire!')
            break
        else:
            print('Scegliere 1 per inserire un altro ordine')
            print('Scegliere 2 per terminare il programma')
            scelta = int(input('Scelta: '))
            print('-----------------------------------------------------------------------------')
        



        

