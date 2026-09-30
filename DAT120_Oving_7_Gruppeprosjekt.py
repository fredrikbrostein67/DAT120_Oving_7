#----------------------------------------------------------- Felles -----------------------------------------------------------------------------
import csv
from datetime import date
import matplotlib.pyplot as plt

filnavn = "CSV_fil_Vær_2014_2024/sinnes_2014_2025.csv"




årstall = "2014"          #(input("Skriv inn et årstall: "))



#----------------------------------------------------------- Fredrik ---------------------------------------------------------------------------
liste_placeholder = []
liste_snødybde = []
liste_nedbør = []
liste_temperatur = []
liste_vind = []





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
    
                try:
                    liste_temperatur.append(float(liste_placeholder[3].replace(",", ".")))
                    liste_nedbør.append(float(liste_placeholder[4].replace(",", ".")))
                    liste_vind.append(float(liste_placeholder[5].replace(",", ".")))
                    liste_snødybde.append(float(liste_placeholder[6].replace(",", ".")))

                except ValueError:
                    continue

        


        
        liste_dato_temp = list(range(0, len(liste_temperatur)))
        liste_dato_nedbør = list(range(0, len(liste_nedbør)))
        liste_dato_vind = list(range(0, len(liste_vind)))
        liste_dato_snø = list(range(0, len(liste_snødybde)))
    
        


            

except FileNotFoundError:
    print("Fil finnes ikke: ")


# Lager en figur med to plott under hverandre
fig, (plot1) = plt.subplots(1, 1, figsize=(15, 7))  #(plot1, plot2) = plt.subplots(2, 1, figsize=(15, 7))
#fig, (plot3, plot4) = plt.subplots(2, 1, figsize=(15, 7))

#--------------------------------- Temperatur ------------------------------------
plot1.plot(liste_dato_temp, liste_temperatur, marker="", color="tab:red")
plot1.set_title("Temperatur")
plot1.set_ylabel("Antall grader")
plot1.set_xticks(range(0, 366))
plot1.grid(True)

#---------------------------------- Nedbør ---------------------------------------
# plot2.plot(liste_dato_nedbør, liste_nedbør, marker="", color="tab:blue")
# plot2.set_title("Nedbør")
# plot2.set_xlabel(årstall)
# plot2.set_ylabel("Antall grader")
# plot2.set_xticks(range(0, 366))
# plot2.grid(True)

# #--------------------------------- Vind ----------------------------------------
# plot3.plot(liste_dato_vind, liste_vind, marker="", color="tab:green")
# plot3.set_title("Vind")
# plot3.set_ylabel("Antall grader")
# plot3.set_xticks(range(0, 366))
# plot3.grid(True)

# #----------------------------------- Snø ---------------------------------------
# plot4.plot(liste_dato_snø, liste_snødybde, marker="", color="tab:blue")
# plot4.set_title("Snø")
# plot4.set_xlabel(årstall)
# plot4.set_ylabel("Antall grader")
# plot4.set_xticks(range(0, 366))
# plot4.grid(True)

# #-------------------------------------------------------------------------------



fig.suptitle(f"Vær")
plt.tight_layout()
plt.show()


#Oppgave d)
#Brukeerenn skrive inn årstall
#programmet skal plotte:
#-> Snødydbe
#-> Nedbør
#-> Middeltemperatur
#-> Høyeste middelvind hver dag for dette året
## Hint Konverter datoene fra strenger til daetime objekter for å få en finere visning av datoene


#----------------------------------------------------------------------------------------------------------------------------------------------












