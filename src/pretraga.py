def pretraga(tip, vrednost):
    postoji = False
    fajl = open("../data/projekcije.txt","r")
    linije = fajl.readlines()
    fajl.close()
    lista=[]
	
    for i in linije:
        film = i.split('|')
        if tip == 'id' and vrednost == film[0] and film[4]== 'False':
            lista.append(i)
        elif tip == 'ime' and film[1].lower().find(vrednost.lower())>=0 and film[4]== 'False':
            lista.append(i)
        elif tip == 'zanr' and film[2].lower().find(vrednost.lower())>=0 and film[4]== 'False':
            lista.append(i)
        elif tip == 'sala' and film[3].lower().find(vrednost.lower())>=0 and film[4]== 'False':
            lista.append(i)
    return lista
