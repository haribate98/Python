def proveriVreme(sala, pocetnoVremeUnos, krajnjeVremeUnos):
    konfliktPostoji = True
    fajl = open("projekcije.txt","r")
    linije = fajl.readlines()
    fajl.close()
	
    for i in linije:
        film = i.split('|')
        salaFilma = film[3]	
        if sala == int(salaFilma):
            datumFilma = film[5]
            vreme = film[6]
            trajanje = film[7]
		    
            arr = datumFilma.split('.')
            datumFile = datetime.date(int(arr[0]), int(arr[1]), int(arr[2]))
		    
            arr2 = vreme.split(':')
            vremeFile = datetime.time(int(arr2[0]), int(arr2[1]))
		    
            pocetnoVremeFile = datetime.datetime.combine(datumFile, vremeFile)
            krajnjeVremeFile = pocetnoVremeFile + datetime.timedelta(minutes=int(trajanje))
            # print('poc file', pocetnoVremeFile)
            # print('kr file', krajnjeVremeFile)
			
            if krajnjeVremeUnos < pocetnoVremeFile or pocetnoVremeUnos > krajnjeVremeFile:
                konfliktPostoji = False
            else:
                konfliktPostoji = True
            return konfliktPostoji
			
        return konfliktPostoji

proveriVreme(1, 12.00, 120)
