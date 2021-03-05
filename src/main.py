from brisanje import *
from login import *
from meni import *
from pretraga import *
from unos import *
from izmena import *

print ("Dobrosli, molimo vas unesite vase korisnicko ime i sifru")
#login()

izb=izborMenija()
     
if int(izb) == 1:
     tip = input('unesite tip? ')
     vrednost = input('unesite vrednost? ')
     print (pretraga(tip, vrednost))
     
    
     
elif int(izb) == 2:
	idVrednost = input('Unesite id')
	ime = input('Unesite ime')
	zanr = prikaziZanrove()
	sala = input('Unesite salu')
	datum = input ('Unesite datum')
	vreme = input('Unesite vreme')
	trajanje = input('Unesite trajanje')
	rez = unosProjekcije(idVrednost, ime, zanr, sala, datum, vreme, trajanje)
	if (rez):
		print('Uspesno uneta projekcija')
	else:
		print('Projekcija nije uspesno uneta')
		
elif int(izb) == 3:
    vrednost = input('Unesite id')
    rezultat = brisanje(vrednost)
    if rezultat == True:
        print ('Uspesno obrisano')
    else:
        print ('Niste uneli dobar id')

elif int(izb) == 4:
    event_id = input('Unesite ID dogadjaja koji zelite da promenite - ')
    event = find_event(event_id)
    print('1. Ime 2. Zanr 3. Sala 4. Vreme 5. Datum')
    menu_option = input('Unesite sta zelite da promenite - ')
    if int(menu_option) == 1:
        events = read_events()
        new_name = input('Unesite novo ime - ')
        updated_event = event.split('|')
        updated_event[1] = new_name
        event = '|'.join([str(x) for x in updated_event])
        for e in range(0, len(events), 1):
            if events[e].split('|')[0] == event.split('|')[0]:
                events[e] = event
        with open('../data/projekcije.txt', 'w') as data:
            for i in events:
                print(i)
                data.write(i)
                
    elif int(menu_option) == 2:
        events = read_events()
        novi_zanr = input('Unesite novi zanr - ')
        updated_event = event.split('|')
        updated_event[2] = novi_zanr
        event = '|'.join([str(x) for x in updated_event])
        for e in range(0, len(events), 1):
            if events[e].split('|')[0] == event.split('|')[0]:
                events[e] = event
        with open('../data/projekcije.txt', 'w') as data:
            for i in events:
                print(i)
                data.write(i)
                
    elif int(menu_option) == 3:
        events = read_events()
        nova_sala = input('Unesite novu salu - ')
        updated_event = event.split('|')
        updated_event[3] = nova_sala
        event = '|'.join([str(x) for x in updated_event])
        for e in range(0, len(events), 1):
            if events[e].split('|')[0] == event.split('|')[0]:
                events[e] = event
        with open('../data/projekcije.txt', 'w') as data:
            for i in events:
                print(i)
                data.write(i)
                
    elif int(menu_option) == 4:
        events = read_events()
        novo_vreme = input('Unesite novo vreme - ')
        updated_event = event.split('|')
        updated_event[6] = novo_vreme
        event = '|'.join([str(x) for x in updated_event])
        for e in range(0, len(events), 1):
            if events[e].split('|')[0] == event.split('|')[0]:
                events[e] = event
        with open('../data/projekcije.txt', 'w') as data:
            for i in events:
                print(i)
                data.write(i)

    elif int(menu_option) == 5:
         events = read_events()
         novi_datum = input('Unesite novi datum - ')
         updated_event = event.split('|')
         updated_event[5] = novi_datum
         event = '|'.join([str(x) for x in updated_event])
         for e in range(0, len(events), 1):
              if events[e].split('|')[0] == event.split('|')[0]:
                   events[e] = event
         with open('../data/projekcije.txt', 'w') as data:
              for i in events:
                   print(i)
                   data.write(i)

elif int(izb) == 5:
    korisnicko = input('Unesite korisnicko ime: ')
    sifra = input('Unesite sifru: ')
    imePrezime = input('Unesite ime i prezime: ')
    prod = unosProdavca (korisnicko, sifra, imePrezime)
    print ('Uspnesno ste uneli prodavca')
    
                
elif int(izb) == 6:
     quit()
