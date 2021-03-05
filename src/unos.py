def idSlobodan(idVrednost):
    fajl = open("../data/projekcije.txt","r")
    linije = fajl.readlines()
    fajl.close()
    for i in linije:
	    film = i.split('|')
	    if idVrednost == film[0]:
		    return False
	
    return True
	
def unosProjekcije(id, ime, zanr, sala, datum, vreme, trajanje):
    uspesanUnos = False
    if (idSlobodan(id)):
        fajl_out = open("../data/projekcije.txt","a")
        fajl_out.write(id + '|' +ime + '|' + zanr + '|' + sala + '|' + 'False|' + datum + '|' +vreme+ '|' + trajanje + '|\n')
        uspesanUnos = True
        fajl_out.close()
    return uspesanUnos


def prikaziZanrove():
    print ('Izbor zanra:')
    dict = {'1': 'Akcija', '2': 'Komedija', '3' : 'Triler', '4' : 'Drama', '5': 'SciFi'}
    print ('1) - Akcija')
    print ('2) - Komedija ')
    print ('3) - Triler')
    print ('4) - Drama')
    print ('5) - SciFi')
    izbor = input('Izaberite: ')
    
    while int(izbor) < 1 or int(izbor) > 5:
        print('Pogresna vrednost, moguci izbor je od 1 do 5.')
        izbor = input('Izaberite: ')

    return dict[izbor]
