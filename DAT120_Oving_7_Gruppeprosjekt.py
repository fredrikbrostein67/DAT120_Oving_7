#----------------------------------------------------------- Felles -----------------------------------------------------------------------------import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filnavn_øving_7 = "CSV_fil_Vær_2014_2024/sinnes_2014_2025_med_makstemperatur.csv"

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


#--------------------------- Oppgave B ----------------------------------

# Lister for årstall og antall dager
liste_aar = []
liste_sommerdager = []
liste_hoysommerdager = []
liste_tropedager = []

# Ordbok for å lagre antall dager per år
dager_per_aar = {}

try:
    with open(filnavn_oslo, "r", encoding="UTF-8") as csv_fil:

        # Hopper over første linje
        next(csv_fil)

        for linje in csv_fil:
            linje = linje.strip()
            data = linje.split(";")

            # Sjekker at linjen har nok kolonner
            if len(data) < 5:
                continue

            try:
                # Henter dato og årstall
                dato = datetime.strptime(data[2], "%d.%m.%Y")
                aar = dato.year

                # Henter maksimaltemperatur
                temperatur = float(data[4].replace(",", "."))

            except (ValueError, IndexError):
                continue

            # Lager plass til hvert år
            if aar not in dager_per_aar:
                dager_per_aar[aar] = [0, 0, 0]

            # Teller sommerdager over 20 grader
            if temperatur > 20:
                dager_per_aar[aar][0] += 1

            # Teller høysommerdager over 25 grader
            if temperatur > 25:
                dager_per_aar[aar][1] += 1

            # Teller tropedager over 30 grader
            if temperatur > 30:
                dager_per_aar[aar][2] += 1

    # Sorterer årstallene
    liste_aar = sorted(dager_per_aar.keys())

    # Legger resultatene i egne lister
    for aar in liste_aar:
        liste_sommerdager.append(dager_per_aar[aar][0])
        liste_hoysommerdager.append(dager_per_aar[aar][1])
        liste_tropedager.append(dager_per_aar[aar][2])

    # Lager plott
    plt.figure(figsize=(15, 8))

    plt.plot(liste_aar, liste_sommerdager,
             label="Sommerdager", color="tab:orange")

    plt.plot(liste_aar, liste_hoysommerdager,
             label="Høysommerdager", color="tab:red")

    plt.plot(liste_aar, liste_tropedager,
             label="Tropedager", color="tab:blue")

    plt.title("Sommerdager, høysommerdager og tropedager - Oslo Blindern")
    plt.xlabel("År")
    plt.ylabel("Antall dager")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Finner ikke CSV-filen for Oslo Blindern")

#--------------------------- Slutt oppgave B ----------------------------



# =====================================================================
# OPPGAVE C - TEMPERATURSAMMENLIKNING
# =====================================================================

import csv


# Bruker filnavnene som allerede er definert i fellesdelen
værstasjoner_temp = {
    "Oslo Blindern": filnavn_oslo,
    "Røros": filnavn_røros,
    "Tromsø": filnavn_tromsø,
    "Værnes": filnavn_værnes,
    "Venabu": filnavn_venabu,
    "Sinnes": filnavn_øving_7
}


# Leser én værfil og regner ut gjennomsnittstemperaturen for hvert år
def les_årsgjennomsnitt(filnavn):

    # Her lagres temperaturene sortert etter år
    temperaturer_per_år = {}

    with open(filnavn, "r", encoding="utf-8-sig") as csv_fil:

        # Leser fila ved hjelp av kolonnenavnene
        leser = csv.DictReader(csv_fil, delimiter=";")

        # Leser én dag om gangen
        for rad in leser:

            dato_tekst = rad["Tid(norsk normaltid)"].strip()
            temperatur_tekst = rad["Middeltemperatur (døgn)"].strip()

            # Hopper over manglende temperaturmålinger
            if temperatur_tekst == "" or temperatur_tekst == "-":
                continue

            try:
                # Gjør datoen om til datetime
                dato = datetime.strptime(
                    dato_tekst,
                    "%d.%m.%Y"
                )

                # Gjør temperaturen om til float
                temperatur = float(
                    temperatur_tekst.replace(",", ".")
                )

            # Hopper over feilformaterte linjer
            except ValueError:
                continue


            år = dato.year


            # Lager en ny liste hvis året ikke finnes fra før
            if år not in temperaturer_per_år:
                temperaturer_per_år[år] = []


            # Legger temperaturen inn på riktig år
            temperaturer_per_år[år].append(temperatur)


    # Lister som skal brukes i grafen
    liste_årstall = []
    liste_gjennomsnitt_temp = []


    # Går gjennom alle år i rekkefølge
    for år in sorted(temperaturer_per_år):

        temperaturer = temperaturer_per_år[år]


        # Oppgaven krever minst 300 gyldige dager
        if len(temperaturer) >= 300:

            gjennomsnitt_temp = (
                sum(temperaturer) / len(temperaturer)
            )

            liste_årstall.append(år)
            liste_gjennomsnitt_temp.append(
                gjennomsnitt_temp
            )


    return liste_årstall, liste_gjennomsnitt_temp



# =====================================================================
# PLOTTING
# =====================================================================

# Lager en egen figur bare for oppgave C
# Dermed påvirker den ikke plottene i de andre deloppgavene
fig_temp, akse_temp = plt.subplots(
    figsize=(12, 6)
)


# Går gjennom alle værstasjonene
for navn, filnavn_stasjon in værstasjoner_temp.items():

    try:

        # Regner ut årsgjennomsnittet for stasjonen
        årstall_temp, gjennomsnitt_temp = les_årsgjennomsnitt(
            filnavn_stasjon
        )


        # Lager én kurve for hver værstasjon
        akse_temp.plot(
            årstall_temp,
            gjennomsnitt_temp,
            label=navn
        )


    except FileNotFoundError:

        print(
            "Fant ikke filen:",
            filnavn_stasjon
        )


# Tekst på grafen
akse_temp.set_title(
    "Gjennomsnittstemperatur per år"
)

akse_temp.set_xlabel(
    "År"
)

akse_temp.set_ylabel(
    "Gjennomsnittstemperatur (°C)"
)


# Viser navn på værstasjonene
akse_temp.legend()


# Gjør grafen lettere å lese
akse_temp.grid(True)


# Tilpasser grafen
plt.tight_layout()



# =====================================================================
# OPPGAVE D - VINDSTATISTIKK
# =====================================================================

from statistics import median

# Lager en ordbok med en liste for hver måned
vind_per_maaned = {}

for maaned in range(1, 13):
    vind_per_maaned[maaned] = []

try:
    # Leser værdata fra Oslo Blindern
    with open(filnavn_oslo, "r", encoding="UTF-8") as csv_fil:

        # Hopper over første linje
        next(csv_fil)

        for linje in csv_fil:
            data = linje.strip().split(";")

            # Sjekker at linjen inneholder nok kolonner
            if len(data) < 7:
                continue

            try:
                # Leser dato og finner måneden
                dato = datetime.strptime(data[2], "%d.%m.%Y")
                maaned = dato.month

                # Leser vindstyrken
                vind = float(data[6].replace(",", "."))

            except (ValueError, IndexError):
                continue

            # Legger vindmålingen til riktig måned
            vind_per_maaned[maaned].append(vind)

    # Lister for resultatene
    maaneder = []
    minimum_vind = []
    median_vind = []
    maksimum_vind = []

    # Regner ut statistikk for hver måned
    for maaned in range(1, 13):

        vind_liste = vind_per_maaned[maaned]

        if len(vind_liste) > 0:
            maaneder.append(maaned)
            minimum_vind.append(min(vind_liste))
            median_vind.append(median(vind_liste))
            maksimum_vind.append(max(vind_liste))

    # Lager diagrammet
    plt.figure(figsize=(12, 6))

    plt.plot(maaneder, minimum_vind,
             marker="o", label="Minimum vind")

    plt.plot(maaneder, median_vind,
             marker="o", label="Median vind")

    plt.plot(maaneder, maksimum_vind,
             marker="o", label="Maksimum vind")

    plt.title("Vindstatistikk per måned - Oslo Blindern")
    plt.xlabel("Måned")
    plt.ylabel("Vindstyrke (m/s)")

    plt.xticks(range(1, 13), [
        "Jan", "Feb", "Mar", "Apr", "Mai", "Jun",
        "Jul", "Aug", "Sep", "Okt", "Nov", "Des"
    ])

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

except FileNotFoundError:
    print("Finner ikke CSV-filen for Oslo Blindern")

# Viser alle diagrammene
plt.show()

# =====================================================================
# SLUTT OPPGAVE D
# =====================================================================


# ---------------- Oppgave e: Skisesonger ----------------

def skisesonger(filnavn):
    sesonger = {}

    with open(filnavn, "r", encoding="utf-8-sig") as csv_fil:
        overskrift = next(csv_fil).strip().split(";")
        snøkolonne = overskrift.index("Snødybde")

        for linje in csv_fil:
            deler = linje.strip().split(";")

            if len(deler) <= snøkolonne:
                continue

            try:
                dato = datetime.strptime(deler[2].strip(), "%d.%m.%Y")
            except ValueError:
                continue  # Hopper over forklaringsteksten nederst i fila.

            # Sesongen får årstallet til året den slutter i.
            if dato.month >= 11:
                sesong = dato.year + 1
            elif dato.month <= 5:
                sesong = dato.year
            else:
                continue  # Juni til oktober er utenfor skisesongen.

            if sesong not in sesonger:
                sesonger[sesong] = {}

            snøtekst = deler[snøkolonne].strip()

            if snøtekst in ("", "-"):
                continue  # Manglende målinger teller ikke som gyldige dager.

            # Hver dato lagres bare én gang.
            sesonger[sesong][dato] = float(snøtekst.replace(",", "."))

    årstall = []
    skidager = []

    if not sesonger:
        return årstall, skidager

    for år in range(min(sesonger), max(sesonger) + 1):
        start = datetime(år - 1, 11, 1)
        slutt = datetime(år, 5, 31)

        # +1 gjør at både første og siste dag telles med.
        dager_i_sesongen = (slutt - start).days + 1
        målinger = sesonger.get(år, {})

        årstall.append(år)

        if len(målinger) >= dager_i_sesongen / 2:
            antall = 0

            for snødybde in målinger.values():
                if snødybde >= 20:
                    antall += 1

            skidager.append(antall)
        else:
            # Gir et hull i kurven når sesongen har for lite data.
            skidager.append(float("nan"))

    return årstall, skidager


værstasjoner = {
    "Oslo Blindern": filnavn_oslo,
    "Røros": filnavn_røros,
    "Tromsø": filnavn_tromsø,
    "Værnes": filnavn_værnes,
    "Venabu": filnavn_venabu,
    "Sinnes": filnavn_øving_7,
}

fig_ski, akse_ski = plt.subplots(figsize=(12, 6))

for navn, filnavn_stasjon in værstasjoner.items():
    sesongår, antall_skidager = skisesonger(filnavn_stasjon)

    akse_ski.plot(
        sesongår,
        antall_skidager,
        marker=".",
        label=navn
    )

akse_ski.set_title("Dager med skiføre per skisesong – minst 20 cm snø")
akse_ski.set_xlabel("Året sesongen slutter (november året før–mai)")
akse_ski.set_ylabel("Registrerte dager med skiføre")
akse_ski.set_ylim(bottom=0)
akse_ski.grid(True, alpha=0.3)
akse_ski.legend()



plt.tight_layout()
plt.show()








#---------------------------------------- Sommerdager -------------------------------------------------
# sommerdager = 0
# høysommerdager = 0
# tropedager = 0

# for element in liste_temperatur:
#     if element >= 20.0 and not element >= 25.0:
#         sommerdager += 1
#     if element >= 25.0 and not element >= 30.0:
#         høysommerdager += 1
#     if element >= 30.0:
#         tropedagerdager += 1

# print(f"""
# Antall Sommerdager er: {sommerdager} stk
# Antall Høysommerdager er: {høysommerdager} stk
# Antall Tropedager er: {tropedager} stk""")

# #-----------------------------------------------------------------------------------------------------------------------------------

# #---------------------------------------- Plantevekst -------------------------------------------------
# plantevekst = 0

# for temperatur in liste_temperatur:
#     if temperatur >= 5:
#         plantevekst += temperatur - 5

# print(f"Total plantevekst i {årstall}: {plantevekst:.2f}")





# #---------------- Oppgave G: Lengste periode uten nedbør ----------------

# from datetime import timedelta

# def lengste_periode_uten_nedbor(filnavn, årstall):
#     lengste = 0
#     antall = 0
#     startdato = None
#     beste_start = None
#     beste_slutt = None
#     forrige_dato = None

#     nedbor_data = []

#     with open(filnavn, "r", encoding="utf-8-sig") as csv_fil:
#         next(csv_fil)

#         for linje in csv_fil:
#             deler = linje.strip().split(";")

#             if len(deler) < 5:
#                 continue

#             try:
#                 dato = datetime.strptime(deler[2].strip(), "%d.%m.%Y")
#             except ValueError:
#                 continue

#             if dato.year != int(årstall):
#                 continue

#             nedbor_tekst = deler[4].strip()

#             if nedbor_tekst in ("", "-"):
#                 nedbor = None
#             else:
#                 try:
#                     nedbor = float(nedbor_tekst.replace(",", "."))
#                 except ValueError:
#                     nedbor = None

#             nedbor_data.append((dato, nedbor))

#     # Sorterer målingene etter dato
#     nedbor_data.sort()

#     # Finner lengste sammenhengende periode uten nedbør
#     for dato, nedbor in nedbor_data:

#         if nedbor == 0:
#             if antall == 0 or forrige_dato is None or dato - forrige_dato != timedelta(days=1):
#                 antall = 1
#                 startdato = dato
#             else:
#                 antall += 1

#             if antall > lengste:
#                 lengste = antall
#                 beste_start = startdato
#                 beste_slutt = dato

#         else:
#             antall = 0

#         forrige_dato = dato

#     # Skriver ut resultatet
#     print("\n--- Oppgave G: Lengste periode uten nedbør ---")

#     if lengste > 0:
#         print(f"Lengste periode: {lengste} dager")
#         print(f"Startdato: {beste_start.strftime('%d.%m.%Y')}")
#         print(f"Sluttdato: {beste_slutt.strftime('%d.%m.%Y')}")
#     else:
#         print("Ingen registrerte dager uten nedbør.")

# # Kjører funksjonen
# lengste_periode_uten_nedbor(filnavn, årstall)
# #----------------------------------------------