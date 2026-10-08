#----------------------------------------------------------- Felles -----------------------------------------------------------------------------import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filnavn = "CSV_fil_Vær_2014_2024/sinnes_2014_2025.csv"



årstall = input("Skriv inn et årstall: ").strip()




#----------------------------------------------------------- Fredrik ---------------------------------------------------------------------------
liste_placeholder = []
liste_snødybde = []
liste_nedbør = []
liste_temperatur = []
liste_vind = []

liste_dato_datetime = []





første_scan = True



try:
    with open(filnavn, "r", encoding="UTF-8") as csv_fil:
        for linje in csv_fil:
            if første_scan:   #Ikke les første linje, her er det kun forklaringstekst
                første_scan = False
                continue

            linje_stripped = linje.strip()
            liste_placeholder = (linje_stripped.split(";"))

            if årstall in liste_placeholder[2]:

                date_format = '%d.%m.%Y'
                date_obj = datetime.strptime(liste_placeholder[2], date_format)
                liste_dato_datetime.append(date_obj)


                liste_temperatur.append(float(liste_placeholder[3].replace(",", "." , ).replace("-", "0")))
                liste_nedbør.append(float(liste_placeholder[4].replace(",", "." , ).replace("-", "0")))
                liste_vind.append(float(liste_placeholder[5].replace(",", "." , ).replace("-", "0")))
                liste_snødybde.append(float(liste_placeholder[6].replace(",", "." , ).replace("-", "0")))


        
        
        liste_dato_temp = list(range(0, len(liste_temperatur)))
        liste_dato_nedbør = list(range(0, len(liste_nedbør)))
        liste_dato_vind = list(range(0, len(liste_vind)))
        liste_dato_snø = list(range(0, len(liste_snødybde)))

        #print(liste_dato_datetime)
        #print(liste_temperatur)

    
        
     

except FileNotFoundError:
    print("Fil finnes ikke: ")





# Lager en figur med to plott under hverandre
#fig, (plot1) = plt.subplots(1, 1, figsize=(15, 7)) #(plot1, plot2) = plt.subplots(2, 1, figsize=(15, 7))
#fig, (plot3, plot4) = plt.subplots(2, 1, figsize=(15, 7))

#--------------------------------- Temperatur ------------------------------------
#plot1.plot(liste_dato_datetime, liste_temperatur, marker="", color="tab:red")
#plot1.set_title("Temperatur")
#plot1.set_ylabel("Antall grader")
#plot1.xaxis.set_major_locator(mdates.MonthLocator())
#plot1.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
#plot1.grid(True)

#---------------------------------- Nedbør ---------------------------------------
# plot2.plot(liste_dato_nedbør, liste_nedbør, marker="", color="tab:blue")
# plot2.set_title("Nedbør")
# plot2.set_xlabel(årstall)
# plot2.set_ylabel("Antall grader")
# plot2.set_xticks(range(0, 366, 30))
# plot2.grid(True)

#--------------------------------- Vind ----------------------------------------
# plot3.plot(liste_dato_vind, liste_vind, marker="", color="tab:green")
# plot3.set_title("Vind")
# plot3.set_ylabel("Antall grader")
# plot3.set_xticks(range(0, 366, 30))
# plot3.grid(True)

#----------------------------------- Snø ---------------------------------------
# plot4.plot(liste_dato_snø, liste_snødybde, marker="", color="tab:blue")
# plot4.set_title("Snø")
# plot4.set_xlabel(årstall)
# plot4.set_ylabel("Antall grader")
# plot4.set_xticks(range(0, 366, 30))
# plot4.grid(True)

# #-------------------------------------------------------------------------------



#fig.suptitle(f"Vær")
#plt.tight_layout()
#plt.show()


#Oppgave d)

# Konverter datoene fra strenger til datetime objekter for å få en finere visning av datoene


#----------------------------------------------------------------------------------------------------------------------------------------------




def skifore(filnavn, årstall):
    årstall = int(årstall)

    start = datetime(årstall - 1, 11, 1)
    slutt = datetime(årstall, 5, 31)
    antall = 0

    with open(filnavn, "r", encoding="utf-8-sig") as csv_fil:
        next(csv_fil)  # Hopper over første linja



        for linje in csv_fil:
            deler = linje.strip().split(";")

            # Hopper over linjer med feil. quwgdi
            if len(deler) < 7 or not deler[2].strip():
                continue

            dato = datetime.strptime(deler[2], "%d.%m.%Y")

            if start <= dato <= slutt:
                snøtekst = deler[6].strip()

                # Hopper over manglande snømålinga
                if snøtekst in ("", "-"):
                    continue

                snødybde = float(snøtekst.replace(",", "."))

                if snødybde >= 20:
                    antall += 1

    return antall
print("hello")

antall = skifore(filnavn, årstall)

print(f"Skisesongen {årstall}: {antall} registrerte dager med skiføre.")
