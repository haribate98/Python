def meniMenadzer():
    print ('1) - Pretraga projekcije')
    print ('2) - Unos nove projekcije ')
    print ('3) - Brisanje projekcije')
    print ('4) - Izmena projekcije')
    print ('5) - Unos prodavca')
    print ('6) - Izlazak iz aplikacije')
    izbor = input('Izaberite: ')
    return izbor


def izborMenija():
    izb = meniMenadzer()
    while (not izb.isdigit() or int(izb) <1 or int(izb) >6):
        print ('Unesite pravilno: ')
        izb = meniMenadzer()
    return izb
