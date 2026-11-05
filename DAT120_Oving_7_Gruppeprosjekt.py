#----------------------------------------------------------- Felles -----------------------------------------------------------------------------import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filnavn_øving_7 = "CSV_fil_Vær_2014_2024/sinnes_2014_2025.csv"

filnavn_oslo = "Værstasjon_Oving_10/oslo_blindern_1954_2025_med_makstemperatur (2).csv"
filnavn_røros = "Værstasjon_Oving_10/roeros_1954_2025_med_makstemperatur (2).csv"
filnavn_tromsø = "Værstasjon_Oving_10/tromsoe_1954_2025_med_makstemperatur (2).csv"
filnavn_værnes = "Værstasjon_Oving_10/vaernes_1954_2025_med_makstemperatur (2).csv"
filnavn_venabu = "Værstasjon_Oving_10/venabu_1954_2025_med_makstemperatur (2).csv"



#------------------------------------------------ ----------- Fredrik ---------------------------------------------------------------------------
liste_placeholder = []
placeholder_temp_max = []
placeholder_temp_min = []
placeholder_nedbør_total = []
placeholder_vind_max = []
placeholder_snø_max = []

liste_snødybde = []
liste_total_nedbør = []
liste_temp_max = []
liste_temp_min = []
liste_vind = []

liste_dato_datetime = []
liste_dato_nedbør_datetime = []
liste_dato_vind_datetime = []
liste_dato_snø_datetime = []



første_scan = True
første_lesing = True

månedliste = []
måned = 1
forrige_scan_måned = 1
ugyldig_lesing = 0





try:
    with open(filnavn_oslo, "r", encoding="UTF-8") as csv_fil:
        for linje in csv_fil:

            if første_scan:   #Ikke les første linje, her er det kun forklaringstekst
                første_scan = False
                continue

            linje_stripped = linje.strip()
            liste_placeholder = (linje_stripped.split(";"))

            if len(liste_placeholder) == 1:
                continue

            månedliste = liste_placeholder[2].split(".")

            try:
                måned = månedliste[1]
            except IndexError:
                continue


            if not liste_placeholder[4] == "-" and not liste_placeholder[4] == '':    #Max og min temp
                placeholder_temp_max.append(float(liste_placeholder[4].replace(",", ".")))
                placeholder_temp_min.append(float(liste_placeholder[4].replace(",", ".")))



            if liste_placeholder[5] == "-":
                ugyldig_lesing += 1
                placeholder_nedbør_total.append(0.0)



            elif not liste_placeholder[5] == "-" and not liste_placeholder[5] == '':    #Total Nedbør
                placeholder_nedbør_total.append(float(liste_placeholder[5].replace(",", ".")))


            if not liste_placeholder[6] == "-" and not liste_placeholder[6] == '':    #Max vind
                placeholder_vind_max.append(float(liste_placeholder[6].replace(",", ".")))

            if not liste_placeholder[7] == "-" and not liste_placeholder[7] == '':    #Max snødybde
                placeholder_snø_max.append(float(liste_placeholder[7].replace(",", ".")))
            elif liste_placeholder[7] == "-" or liste_placeholder[7] == '':
                placeholder_snø_max.append(0.0)
            

          

            if måned != forrige_scan_måned and not første_lesing: 
                if len(placeholder_temp_max) == 0:
                    liste_temp_max.append(0)
                else:
                    liste_temp_max.append(max(placeholder_temp_max))
                

                if len(placeholder_temp_min) == 0:
                    liste_temp_min.append(0)
                else:
                    liste_temp_min.append(max(placeholder_temp_min))




                if ugyldig_lesing > 20:
                    liste_total_nedbør.append(0)
                else:
                    liste_total_nedbør.append(sum(placeholder_nedbør_total))




                if len(placeholder_vind_max) == 0:
                    liste_vind.append(0)
                else:
                    liste_vind.append(max(placeholder_vind_max))



                if len(placeholder_snø_max) == 0:
                    liste_snødybde.append(0)
                else:
                    liste_snødybde.append(max(placeholder_snø_max))

                ugyldig_lesing = 0

                placeholder_temp_max = []
                placeholder_temp_min = []
                placeholder_nedbør_total = []
                placeholder_vind_max = []
                placeholder_snø_max = []




                liste_dato_datetime.append(forrige_dato.replace(day=1))

            



            første_lesing = False
            forrige_scan_måned = måned
            forrige_dato = datetime.strptime(liste_placeholder[2], '%d.%m.%Y')


    if len(placeholder_temp_max) == 0:
        liste_temp_max.append(0)
    else:
        liste_temp_max.append(max(placeholder_temp_max))
                    
    
    if len(placeholder_temp_min) == 0:
        liste_temp_min.append(0)
    else:
        liste_temp_min.append(max(placeholder_temp_min))
                        
    
    if ugyldig_lesing > 20:
        liste_total_nedbør.append(0)
    else:
        liste_total_nedbør.append(sum(placeholder_nedbør_total))


    if len(placeholder_vind_max) == 0:
        liste_vind.append(0)
    else:
        liste_vind.append(max(placeholder_vind_max))

    liste_snødybde.append(max(placeholder_snø_max))
    liste_dato_datetime.append(forrige_dato.replace(day=1))
            

            

except FileNotFoundError:
    print("Fil finnes ikke: ")



#--------------------------- AI hjelp for sortering --------------------------------
sortert = sorted(zip(liste_dato_datetime))
liste_dato_datetime = [rad[0] for rad in sortert]
#-----------------------------------------------------------------------------------

fig, (plot1, plot2) = plt.subplots(2, 1, figsize=(15, 10))
fig, (plot3, plot4) = plt.subplots(2, 1, figsize=(15, 10))
fig, (plot5) = plt.subplots(1, 1, figsize=(15, 10))

#--------------------------------- Temperatur ------------------------------------
plot1.plot(liste_dato_datetime, liste_temp_max, marker="", color="tab:red")
plot1.set_title("Maks Temperatur")
plot1.set_ylabel("Antall grader")
plot1.xaxis.set_major_locator(mdates.YearLocator())
plot1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plot1.grid(True)

plot2.plot(liste_dato_datetime, liste_temp_min, marker="", color="tab:blue")
plot2.set_title("Min Temperatur")
plot2.set_ylabel("Antall grader")
plot2.xaxis.set_major_locator(mdates.YearLocator())
plot2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plot2.grid(True)

plot3.plot(liste_dato_datetime, liste_total_nedbør, marker="", color="tab:blue")
plot3.set_title("Total Nedbør")
plot3.set_ylabel("mm")
plot3.xaxis.set_major_locator(mdates.YearLocator())
plot3.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plot3.grid(True)

plot4.plot(liste_dato_datetime, liste_vind, marker="", color="tab:green")
plot4.set_title("Maks Vind")
plot4.set_ylabel("m/s")
plot4.xaxis.set_major_locator(mdates.YearLocator())
plot4.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plot4.grid(True)

plot5.plot(liste_dato_datetime, liste_snødybde, marker="", color="tab:blue")
plot5.set_title("Maks snødybde")
plot5.set_ylabel("mm")
plot5.xaxis.set_major_locator(mdates.YearLocator())
plot5.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plot5.grid(True)



plt.tight_layout()
plt.show()








#---------------------------------------- Sommerdager -------------------------------------------------
sommerdager = 0
høysommerdager = 0
tropedager = 0

for element in liste_temperatur:
    if element >= 20.0 and not element >= 25.0:
        sommerdager += 1
    if element >= 25.0 and not element >= 30.0:
        høysommerdager += 1
    if element >= 30.0:
        tropedagerdager += 1

print(f"""
Antall Sommerdager er: {sommerdager} stk
Antall Høysommerdager er: {høysommerdager} stk
Antall Tropedager er: {tropedager} stk""")

#-----------------------------------------------------------------------------------------------------------------------------------
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

antall = skifore(filnavn, årstall)

print(f"Skisesongen {årstall}: {antall} registrerte dager med skiføre.")
#---------------------------------------- Plantevekst -------------------------------------------------
plantevekst = 0

for temperatur in liste_temperatur:
    if temperatur >= 5:
        plantevekst += temperatur - 5

print(f"Total plantevekst i {årstall}: {plantevekst:.2f}")





#---------------- Oppgave G: Lengste periode uten nedbør ----------------

from datetime import timedelta

def lengste_periode_uten_nedbor(filnavn, årstall):
    lengste = 0
    antall = 0
    startdato = None
    beste_start = None
    beste_slutt = None
    forrige_dato = None

    nedbor_data = []

    with open(filnavn, "r", encoding="utf-8-sig") as csv_fil:
        next(csv_fil)

        for linje in csv_fil:
            deler = linje.strip().split(";")

            if len(deler) < 5:
                continue

            try:
                dato = datetime.strptime(deler[2].strip(), "%d.%m.%Y")
            except ValueError:
                continue

            if dato.year != int(årstall):
                continue

            nedbor_tekst = deler[4].strip()

            if nedbor_tekst in ("", "-"):
                nedbor = None
            else:
                try:
                    nedbor = float(nedbor_tekst.replace(",", "."))
                except ValueError:
                    nedbor = None

            nedbor_data.append((dato, nedbor))

    # Sorterer målingene etter dato
    nedbor_data.sort()

    # Finner lengste sammenhengende periode uten nedbør
    for dato, nedbor in nedbor_data:

        if nedbor == 0:
            if antall == 0 or forrige_dato is None or dato - forrige_dato != timedelta(days=1):
                antall = 1
                startdato = dato
            else:
                antall += 1

            if antall > lengste:
                lengste = antall
                beste_start = startdato
                beste_slutt = dato

        else:
            antall = 0

        forrige_dato = dato

    # Skriver ut resultatet
    print("\n--- Oppgave G: Lengste periode uten nedbør ---")

    if lengste > 0:
        print(f"Lengste periode: {lengste} dager")
        print(f"Startdato: {beste_start.strftime('%d.%m.%Y')}")
        print(f"Sluttdato: {beste_slutt.strftime('%d.%m.%Y')}")
    else:
        print("Ingen registrerte dager uten nedbør.")

# Kjører funksjonen
lengste_periode_uten_nedbor(filnavn, årstall)
#----------------------------------------------