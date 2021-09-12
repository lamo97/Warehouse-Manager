import pandas as pd
import os
from pathlib import Path

def classTermsFrequency(frequency_table):
    class_frequency = 0
    for item in frequency_table:
        class_frequency += frequency_table.get(item)
    return class_frequency


def bayes_laplace(order):
    # imprta il dataset e crea un dataframe
    dframe = pd.read_csv("dataset/storico_categorie.csv")

    # l'ordine viene inserito in una lista

    # ogni item viene a sua volta inserito in una lista
    dframe['Ordine'] = dframe['Ordine'].str.split(',')

    # restituisce una lista di item non ripetuti
    vocabulary = []

    for item in dframe['Ordine']:
        i = 0
        while i<len(item):
            word = item[i].split(',')
            if word[0] not in vocabulary:
                vocabulary.append(word[0])
            i += 1

    # cardinalità della lista di item non ripetuti
    vocabulary_size = len(vocabulary)

    # inserisce gli item fragili in un dataframe separato
    fragili = dframe[dframe['Categoria'] == 'Fragile']

    # crea una lista di item classificati come fragili
    lista_fragili = []
    for products in fragili['Ordine']:
        for item in products:
            lista_fragili.append(item)

    # numero di oggetti fragili
    numero_fragili = len(lista_fragili)

    # crea una tabella delle frequenze degli item calssificati come fragili
    freq_fragili = {}

    for item in lista_fragili:
        if item in freq_fragili:
            freq_fragili[item] += 1
        else:
            freq_fragili[item] = 1

    # inserisce gli elementi del dizionario non presenti nella classe, settando frequenza 0
    for item in vocabulary:
        if item not in freq_fragili:
           freq_fragili.update({item : 0})

    # inserisce gli item non fragili in un dataframe separato
    non_fragili = dframe[dframe['Categoria'] != 'Fragile']

    # crea una lista di item classificati come non fragili
    lista_non_fragili = []
    for dish in non_fragili['Ordine']:
        for item in dish:
            lista_non_fragili.append(item)

    # numero di oggetti non fragili
    numero_non_fragili = len(lista_non_fragili)

    # crea una tabella delle frequenze degli item calssificati come non fragili
    freq_non_fragili = {}

    for item in lista_non_fragili:
        if item in freq_non_fragili:
            freq_non_fragili[item] += 1
        else:
            freq_non_fragili[item] = 1

    # inserisce gli elementi del dizionario non presenti nella classe, settando frequenza 0
    for item in vocabulary:
        if item not in freq_non_fragili:
            freq_non_fragili.update({item : 0})

    # trova la probabilità degli elementi fragili e non fragili
    cat_percentages = dframe['Categoria'].value_counts(normalize=True)

    # probabilità delle classi
    p_fragili = cat_percentages['Fragile']
    p_non_fragili = cat_percentages['Non Fragile']

    # probabilità naive degli item fragili
    p_ordine_fragile = 1
    # p_ordine_fragile = p_fragili

    # calcola la frequenza totale dei termini che appaiono nella classe
    numero_fragili = classTermsFrequency(freq_fragili)

    for item in order:
        if item in freq_fragili:
            item_count = freq_fragili[item]
            prob_item = (item_count + 1) / (numero_fragili + (1 * vocabulary_size))
            p_ordine_fragile *= prob_item

    # probabilità naive degli item non fragili
    p_ordine_non_fragile = 1
    # p_ordine_non_fragile = p_non_fragili

    # calcola la frequenza totale dei termini che appaiono nella classe
    numero_non_fragili = classTermsFrequency(freq_non_fragili)

    for item in order:
        if item in freq_non_fragili:
            item_count = freq_non_fragili[item]
            prob_item = (item_count + 1) / (numero_non_fragili + (1 * vocabulary_size))
            p_ordine_non_fragile *= prob_item

    
    ordine_fragile = p_ordine_fragile * p_fragili
    ordine_non_fragile = p_ordine_non_fragile * p_non_fragili
    
    
    if ordine_fragile > ordine_non_fragile:
        print("L'ordine contiene oggetti fragili. Usare l'apposito materiale da imballaggio!\n")
    elif ordine_fragile < ordine_non_fragile:
        print("L'ordine non contiene oggetti fragili. E possibile utiizzare l'imballaggio standard.\n")
    else:
        print("Impossibile determinare la natura dell'ordine. Intervento del personale richiesto!\n")
