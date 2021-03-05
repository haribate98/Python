def brisanje(vrednost):
    obrisano = False
    fajl = open('../data/projekcije.txt',"r")
    linije = fajl.readlines()
    fajl.close()
    fajl_out = open('../data/projekcije.txt',"w")
    for i in linije:
        film = i.split('|')
        if vrednost == film[0]:
            film[4] = 'True'
            obrisano = True
        my_string = "|".join(film)
        fajl_out.write(my_string)
    fajl_out.close()
    return obrisano
