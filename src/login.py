def login():
    korisnicko = input('Korisnicko ime? ')
    sifra = input('Sifra? ')
    while(proveraKorisnika(korisnicko, sifra)) == False:
        print('Niste uneli validno korisnicko ime ili sifru')
        korisnicko = input('Unesite korisnicko ime?')
        sifra = input('Unesite sifru?')   
    print ('Korisnik je uspesno prijavljen')
    print ('Prijavljeni korisnik je', korisnicko)


def proveraKorisnika(korisnicko, sifra):
    postoji = False
    fajl = open("../data/korisnici.txt","r")
    linije = fajl.readlines()
    fajl.close()
    for k in linije:
        korisnik = k.split('|')
        if korisnicko == korisnik[0] and sifra == korisnik[1]:
            postoji = True
    return postoji

def unosProdavca(korisnicko, sifra, imePrezime):
    uspesanUnos = True
    fajl_out = open("../data/korisnici.txt","a")
    fajl_out.write(korisnicko + '|' + sifra + '|' + imePrezime + '|' + 'Prodavac' + '|\n')
    fajl_out.close()
    return uspesanUnos
