from random import randint

def genera_destinazione():
    # genera casulamente un numero che corrisponde ad un destinatario dell'ordine
    des = randint(0, len(destinazioni)-1)
    return destinazioni[des]

def genera_codice(categoria):
    codice = 0

    if(categoria == 'abbigliamento'):
        codice = randint(10000,19999)
    elif (categoria == 'auto e moto'):
        codice = randint(20000, 29999)
    elif (categoria == 'bellezza'):
        codice = randint(30000, 39999)
    elif (categoria == 'cancelleria e ufficio'):
        codice = randint(40000, 49999)
    elif (categoria == 'elettronica'):
        codice = randint(50000, 59999)
    elif (categoria == 'illuminazione'):
        codice = randint(60000, 69999)
    elif (categoria == 'informatica'):
        codice = randint(70000, 79999)
    elif (categoria == 'libri'):
        codice = randint(80000, 89999)
    elif (categoria == 'prodotti per animali'):
        codice = randint(90000, 99999)
    elif (categoria == 'strumenti musicali'):
        codice = randint(100000, 109999)
    elif (categoria == 'videogiochi'):
        codice = randint(110000, 119999)
    elif (categoria == 'utensili'):
        codice = randint(120000, 129999)

    return codice

def genera_peso(categoria):
    peso = 0

    if(categoria == 'abbigliamento'):
        peso = randint(10,35)
    elif (categoria == 'auto e moto'):
        peso = randint(10, 60)
    elif (categoria == 'bellezza'):
        peso = randint(5, 12)
    elif (categoria == 'cancelleria e ufficio'):
        peso = randint(8, 30)
    elif (categoria == 'elettronica'):
        peso = randint(4, 35)
    elif (categoria == 'illuminazione'):
        peso = randint(4, 10)
    elif (categoria == 'informatica'):
        peso = randint(5, 20)
    elif (categoria == 'libri'):
        peso = randint(5, 25)
    elif (categoria == 'prodotti per animali'):
        peso = randint(5, 50)
    elif (categoria == 'strumenti musicali'):
        peso = randint(3, 15)
    elif (categoria == 'videogiochi'):
        peso = randint(2, 10)
    elif (categoria == 'utensili'):
        peso = randint(10, 35)

    return peso

def genera_ordine(destinazione):
    # lista di prodotti contenuti nell'ordine
    prodotti = []
    item = {}
    codice = 0

    # quantità di prodotti in un ordine
    quantita = randint(3,12)

    # generazione prodotti
    for i in range(0,quantita):
        if(destinazione == 'centro commerciale'):
            cat = randint(0, len(cat_centro_commerciale)-1)
            categoria = cat_centro_commerciale[cat]
            codice = genera_codice(categoria)
            peso = genera_peso(categoria)
            
            item['codice'] = codice
            item['categoria'] = categoria
            item['peso'] = peso

            item_copy = item.copy()
            prodotti.append(item_copy)
                    
        elif(destinazione == 'ferramenta'):
            cat = randint(0, len(cat_ferramenta)-1)
            categoria = cat_ferramenta[cat]
            codice = genera_codice(categoria)
            peso = genera_peso(categoria)
            
            item['codice'] = codice
            item['categoria'] = categoria
            item['peso'] = peso

            item_copy = item.copy()
            prodotti.append(item_copy)       

        elif(destinazione == 'negozio elettronica'):
            cat = randint(0, len(cat_negozio_elettronica)-1)
            categoria = cat_negozio_elettronica[cat]
            codice = genera_codice(categoria)
            peso = genera_peso(categoria)
            
            item['codice'] = codice
            item['categoria'] = categoria
            item['peso'] = peso

            item_copy = item.copy()
            prodotti.append(item_copy)

        elif(destinazione == 'autoricambi'):
            cat = randint(0, len(cat_autoricambi)-1)
            categoria = cat_autoricambi[cat]
            codice = genera_codice(categoria)
            peso = genera_peso(categoria)
            
            item['codice'] = codice
            item['categoria'] = categoria
            item['peso'] = peso

            item_copy = item.copy()
            prodotti.append(item_copy)

        elif(destinazione == 'libreria'):
            cat = randint(0, len(cat_libreria)-1)
            categoria = cat_libreria[cat]
            codice = genera_codice(categoria)
            peso = genera_peso(categoria)
            
            item['codice'] = codice
            item['categoria'] = categoria
            item['peso'] = peso

            item_copy = item.copy()
            prodotti.append(item_copy)
    
    return prodotti
        


def getPeso(prodotti):
    peso = 0

    for item in prodotti:
        peso += int(item['peso'])

    return peso

def getCategorie(prodotti):
    categorie = []

    for item in prodotti:
        if item['categoria'] not in categorie:
            categorie.append(item['categoria'])

    return categorie

def mostra_ordine(prodotti):
    for item in prodotti:
        print('Codice: ', item['codice'], '  Categoria: ', item['categoria'])
    
    
# destinazioni
destinazioni = ['centro commerciale', 'ferramenta', 'negozio elettronica', 'autoricambi', 'libreria']

# categorie per destinazione
cat_centro_commerciale = ['abbigliamento', 'bellezza', 'informatica', 
                            'elettronica', 'libri', 'prodotti per animali', 'cancelleria e ufficio', 'videogiochi']
cat_ferramenta = ['elettronica', 'illuminazione', 'utensili']
cat_negozio_elettronica = ['elettronica', 'informatica', 'videogiochi']
cat_autoricambi = ['auto e moto', 'utensili']
cat_libreria = ['libri', 'cancelleria e ufficio', 'strumenti musicali']