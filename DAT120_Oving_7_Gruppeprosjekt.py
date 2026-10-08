#----------------------------------------------------------- Felles -----------------------------------------------------------------------------import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filnavn = "CSV_fil_Vær_2014_2024/sinnes_2014_2025.csv"


input_godkjent = False
while input_godkjent == False:
    try: 
        årstall = input("Skriv inn et årstall mellom 2014 til 2025: ")
        årstall_int = int(årstall)

        if årstall_int >= 2014 and årstall_int <= 2025:
            input_godkjent = True 
        else:
            print("Magnler data på det årstallet. ")
            print("årstall mellom 2014 og 2025: ")
            continue

    except ValueError:
        print("Årstall er godkjent tall")
        continue
 


#------------------------------------------------ ----------- Fredrik ---------------------------------------------------------------------------
liste_placeholder = []
liste_snødybde = []
liste_nedbør = []
liste_temperatur = []
liste_vind = []

liste_dato_temp_datetime = []
liste_dato_nedbør_datetime = []
liste_dato_vind_datetime = []
liste_dato_snø_datetime = []



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

                if not liste_placeholder[3] == "-":
                    liste_temperatur.append(float(liste_placeholder[3].replace(",", "." , )))
                    date_obj = datetime.strptime(liste_placeholder[2], '%d.%m.%Y')
                    liste_dato_temp_datetime.append(date_obj)

                
                if not liste_placeholder[4] == "-":
                    liste_nedbør.append(float(liste_placeholder[4].replace(",", "." , )))  
                    date_obj = datetime.strptime(liste_placeholder[2], '%d.%m.%Y')
                    liste_dato_nedbør_datetime.append(date_obj)

                if not liste_placeholder[5] == "-":
                    liste_vind.append(float(liste_placeholder[5].replace(",", "." , )))
                    date_obj = datetime.strptime(liste_placeholder[2], '%d.%m.%Y')
                    liste_dato_vind_datetime.append(date_obj)

                if not liste_placeholder[6] == "-":
                    liste_snødybde.append(float(liste_placeholder[6].replace(",", "." , )))
                    date_obj = datetime.strptime(liste_placeholder[2], '%d.%m.%Y')
                    liste_dato_snø_datetime.append(date_obj)


            

except FileNotFoundError:
    print("Fil finnes ikke: ")


#--------------------------- AI hjelp for sortering --------------------------------
sortert = sorted(zip(liste_dato_temp_datetime))
liste_dato_temp_datetime = [rad[0] for rad in sortert]

sortert = sorted(zip(liste_dato_nedbør_datetime))
liste_dato_nedbør_datetime = [rad[0] for rad in sortert]

sortert = sorted(zip(liste_dato_vind_datetime))
liste_dato_vind_datetime = [rad[0] for rad in sortert]

sortert = sorted(zip(liste_dato_snø_datetime))
liste_dato_snø_datetime = [rad[0] for rad in sortert]


#-----------------------------------------------------------------------------------

fig, (plot1, plot2) = plt.subplots(2, 1, figsize=(15, 7))
fig, (plot3, plot4) = plt.subplots(2, 1, figsize=(15, 7))

#--------------------------------- Temperatur ------------------------------------
plot1.plot(liste_dato_temp_datetime, liste_temperatur, marker="", color="tab:red")
plot1.set_title("Temperatur")
plot1.set_ylabel("Antall grader")
plot1.xaxis.set_major_locator(mdates.MonthLocator())
plot1.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
plot1.grid(True)

#---------------------------------- Nedbør ---------------------------------------
plot2.plot(liste_dato_nedbør_datetime, liste_nedbør, marker="", color="tab:blue")
plot2.set_title("Nedbør")
plot2.set_ylabel("Antall grader")
plot2.xaxis.set_major_locator(mdates.MonthLocator())
plot2.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
plot2.grid(True)

#--------------------------------- Vind ----------------------------------------
plot3.plot(liste_dato_vind_datetime, liste_vind, marker="", color="tab:blue")
plot3.set_title("Vind")
plot3.set_ylabel("meter per sekund")
plot3.xaxis.set_major_locator(mdates.MonthLocator())
plot3.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
plot3.grid(True)
#----------------------------------- Snø ---------------------------------------
plot4.plot(liste_dato_snø_datetime, liste_snødybde, marker="", color="tab:blue")
plot4.set_title("Snø")
plot4.set_ylabel("mm Snø")
plot4.xaxis.set_major_locator(mdates.MonthLocator())
plot4.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
plot4.grid(True)

# #-------------------------------------------------------------------------------

fig.suptitle(f"Vær")
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
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
