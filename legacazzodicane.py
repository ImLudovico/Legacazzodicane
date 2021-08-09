from time import sleep
import sys
import os


from functions import *
from classes import *

os.system("clear")

print("""                 _                _
 /  _  _  _  _  / `_ _ _  _   _/./ `_  _  _
/_,/_'/_//_|/_|/_,/_|/_/_/_//_///_,/_|/ //_'
      _/                                    """)

print("ver: 0.1")

# -------------------------------------------------------------

print("Benvenuti, le squadre iscritte sono ",len(Teams), ".")
sleep(0.0)
print("Viene riportata la lista: ")

for i in range(len(Teams)):
    sleep(0.0)
    print("- ", Teams[i])

print("\n")
input("Premere invio per procedere all'estrazione dell'ordine di pick.")
NewTeamList = Teams.copy()
orderpick(NewTeamList)
R_NewTeamList = NewTeamList.copy()
R_NewTeamList.reverse()

print("L'ordine casuale di pick è stato processato:")

NewCompetition = Competition()

# Populate competition
for i in range(len(NewTeamList)):
    sleep(0.0)
    NewCompetition.addTeam(Team(NewTeamList[i]))

# Print competition
NewCompetition.printCompetition()

print("\n")


# -------------------------------------------------------------

print("--- ESTRAZIONE DATI ---")
print("Estraggo i dati dal file di Fantacalcio.it")
goalkeepers, defenders, midfielders, forwards = get_players_list('Quotazioni_Fantacalcio.xlsx')
print("Estrazione completata.")
print("\n")

print("Premere invio per continuare")

# -------------------------------------------------------------

print(""" _______  _______  ______    _______  ___   _______  ______    ___
|       ||       ||    _ |  |       ||   | |       ||    _ |  |   |
|    _  ||   _   ||   | ||  |_     _||   | |    ___||   | ||  |   |
|   |_| ||  | |  ||   |_||_   |   |  |   | |   |___ |   |_||_ |   |
|    ___||  |_|  ||    __  |  |   |  |   | |    ___||    __  ||   |
|   |    |       ||   |  | |  |   |  |   | |   |___ |   |  | ||   |
|___|    |_______||___|  |_|  |___|  |___| |_______||___|  |_||___| """)


input("Si procede all'estrazione dei portieri. Premere invio per continuare.")

for i in range(len(NewTeamList)):
    NewCompetition.competition_team_list[i], goalkeepers = get_and_remove_elite_gk(NewCompetition.competition_team_list[i], goalkeepers)
    print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_goalkeepers[0].name, ", ", NewCompetition.competition_team_list[i].team_goalkeepers[1].name)


input("Si procede all'estrazione dei secondo giro di portieri (pick inverso)")

for i in reversed(range(len(NewTeamList))):
    NewCompetition.competition_team_list[i], goalkeepers = get_and_remove_elite_gk(NewCompetition.competition_team_list[i], goalkeepers)
    print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_goalkeepers[2].name, ", ", NewCompetition.competition_team_list[i].team_goalkeepers[3].name)

print(""" _______  _______  ______    _______  ___   _______  ______    ___
|       ||       ||    _ |  |       ||   | |       ||    _ |  |   |
|    _  ||   _   ||   | ||  |_     _||   | |    ___||   | ||  |   |
|   |_| ||  | |  ||   |_||_   |   |  |   | |   |___ |   |_||_ |   |
|    ___||  |_|  ||    __  |  |   |  |   | |    ___||    __  ||   |
|   |    |       ||   |  | |  |   |  |   | |   |___ |   |  | ||   |
|___|    |_______||___|  |_|  |___|  |___| |_______||___|  |_||___| """)

print("Ricapitolando, ecco i portieri di ogni squadra: ")

for i in range(len(NewTeamList)):
    print("[",i+1,"]", NewTeamList[i], ":  \t", NewCompetition.competition_team_list[i].team_goalkeepers[0].name, ",\t ",
    NewCompetition.competition_team_list[i].team_goalkeepers[1].name, ",\t ",
    NewCompetition.competition_team_list[i].team_goalkeepers[2].name, ",\t ",
    NewCompetition.competition_team_list[i].team_goalkeepers[3].name,
    ".\t Valore fantagazzetta della rosa dei portieri:\t", NewCompetition.competition_team_list[i].get_value_gk())

input("Premere invio per passare alla fase successiva.")

print("""  ______   ___   _______  _______  __    _  _______  _______  ______    ___
|      | |   | |       ||       ||  |  | ||       ||       ||    _ |  |   |
|  _    ||   | |    ___||    ___||   |_| ||  _____||   _   ||   | ||  |   |
| | |   ||   | |   |___ |   |___ |       || |_____ |  | |  ||   |_||_ |   |
| |_|   ||   | |    ___||    ___||  _    ||_____  ||  |_|  ||    __  ||   |
|       ||   | |   |    |   |___ | | |   | _____| ||       ||   |  | ||   |
|______| |___| |___|    |_______||_|  |__||_______||_______||___|  |_||___| """)

input("Premere invio per avviare la fase di selezione dei difensori. Le prime 6 estrazioni avverranno in maniera esplicita. Le estrazioni vengono eseguite per pick order alternati.")

for q in range(6):
    print("Estrazione numero ", q+1)
    if q%2 == 0:
        for i in range(len(NewTeamList)):
            NewCompetition.competition_team_list[i], defenders = get_and_remove_elite_def(NewCompetition.competition_team_list[i], defenders)
            print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_defenders[q].name)
    else:
        for i in reversed(range(len(NewTeamList))):
            NewCompetition.competition_team_list[i], defenders = get_and_remove_elite_def(NewCompetition.competition_team_list[i], defenders)
            print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_defenders[q].name)
    print("Difensori rimasti: ", len(defenders))
    input("Premere invio")

input("Premere invio per procedere al resto delle estrazioni (4)")

for q in range(4):
    print("Estrazione addizionale numero ", q+1)
    if q%2 == 0:
        for i in range(len(NewTeamList)):
            NewCompetition.competition_team_list[i], defenders = get_and_remove_elite_def(NewCompetition.competition_team_list[i], defenders)
    else:
        for i in reversed(range(len(NewTeamList))):
            NewCompetition.competition_team_list[i], defenders = get_and_remove_elite_def(NewCompetition.competition_team_list[i], defenders)
    print("Difensori rimasti: ", len(defenders))


input("Premere invio per procedere.")

print("""  ______   ___   _______  _______  __    _  _______  _______  ______    ___
|      | |   | |       ||       ||  |  | ||       ||       ||    _ |  |   |
|  _    ||   | |    ___||    ___||   |_| ||  _____||   _   ||   | ||  |   |
| | |   ||   | |   |___ |   |___ |       || |_____ |  | |  ||   |_||_ |   |
| |_|   ||   | |    ___||    ___||  _    ||_____  ||  |_|  ||    __  ||   |
|       ||   | |   |    |   |___ | | |   | _____| ||       ||   |  | ||   |
|______| |___| |___|    |_______||_|  |__||_______||_______||___|  |_||___| """)

print("Ecco un riepilogo di chi difenderà le vostre porte: ")

for i in range(len(NewTeamList)):
    print("[",i+1,"]", NewTeamList[i], ":  \n",
    NewCompetition.competition_team_list[i].team_defenders[0].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[1].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[2].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[3].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[4].name, ",\n ",
    NewCompetition.competition_team_list[i].team_defenders[5].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[6].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[7].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[8].name, ",\t ",
    NewCompetition.competition_team_list[i].team_defenders[9].name, ",\n "
    )


for i in range(len(NewTeamList)):
    print("[",i+1,"]", NewTeamList[i], " - ", "\t Valore Fantacalcio della rosa dei difensori :\t", NewCompetition.competition_team_list[i].get_value_def())

print("Premere invio per procedere.")

print("""  _______  _______  __    _  _______  ______    _______  _______  _______  __   __  _______  ___   _______  _______  ___
|       ||       ||  |  | ||       ||    _ |  |       ||       ||   _   ||  |_|  ||       ||   | |       ||       ||   |
|       ||    ___||   |_| ||_     _||   | ||  |   _   ||       ||  |_|  ||       ||    _  ||   | |  _____||_     _||   |
|       ||   |___ |       |  |   |  |   |_||_ |  | |  ||       ||       ||       ||   |_| ||   | | |_____   |   |  |   |
|      _||    ___||  _    |  |   |  |    __  ||  |_|  ||      _||       ||       ||    ___||   | |_____  |  |   |  |   |
|     |_ |   |___ | | |   |  |   |  |   |  | ||       ||     |_ |   _   || ||_|| ||   |    |   |  _____| |  |   |  |   |
|_______||_______||_|  |__|  |___|  |___|  |_||_______||_______||__| |__||_|   |_||___|    |___| |_______|  |___|  |___| """)

input("Premere invio per avviare la fase di selezione dei centrocampisti. Le prime 6 estrazioni avverranno in maniera esplicita. Le estrazioni vengono eseguite per pick order alternati.")

for q in range(6):
    print("Estrazione numero ", q+1)
    if q%2 == 0:
        for i in range(len(NewTeamList)):
            NewCompetition.competition_team_list[i], midfielders = get_and_remove_elite_mid(NewCompetition.competition_team_list[i], midfielders)
            print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_midfielders[q].name)
    else:
        for i in reversed(range(len(NewTeamList))):
            NewCompetition.competition_team_list[i], midfielders = get_and_remove_elite_mid(NewCompetition.competition_team_list[i], midfielders)
            print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_midfielders[q].name)
    print("Centrocampisti rimasti: ", len(defenders))
    input("Premere invio")

input("Premere invio per procedere al resto delle estrazioni (4)")

for q in range(4):
    print("Estrazione addizionale numero ", q+1)
    if q%2 == 0:
        for i in range(len(NewTeamList)):
            NewCompetition.competition_team_list[i], midfielders = get_and_remove_elite_mid(NewCompetition.competition_team_list[i], midfielders)
    else:
        for i in reversed(range(len(NewTeamList))):
            NewCompetition.competition_team_list[i], midfielders = get_and_remove_elite_mid(NewCompetition.competition_team_list[i], midfielders)
    print("Centrocampisti rimasti: ", len(midfielders))

print("""  _______  _______  __    _  _______  ______    _______  _______  _______  __   __  _______  ___   _______  _______  ___
|       ||       ||  |  | ||       ||    _ |  |       ||       ||   _   ||  |_|  ||       ||   | |       ||       ||   |
|       ||    ___||   |_| ||_     _||   | ||  |   _   ||       ||  |_|  ||       ||    _  ||   | |  _____||_     _||   |
|       ||   |___ |       |  |   |  |   |_||_ |  | |  ||       ||       ||       ||   |_| ||   | | |_____   |   |  |   |
|      _||    ___||  _    |  |   |  |    __  ||  |_|  ||      _||       ||       ||    ___||   | |_____  |  |   |  |   |
|     |_ |   |___ | | |   |  |   |  |   |  | ||       ||     |_ |   _   || ||_|| ||   |    |   |  _____| |  |   |  |   |
|_______||_______||_|  |__|  |___|  |___|  |_||_______||_______||__| |__||_|   |_||___|    |___| |_______|  |___|  |___| """)

print("Ecco un riepilogo di chi presiederà il centrocampo: ")

for i in range(len(NewTeamList)):
    print("[",i+1,"]", NewTeamList[i], ":  \n",
    NewCompetition.competition_team_list[i].team_midfielders[0].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[1].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[2].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[3].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[4].name, ",\n ",
    NewCompetition.competition_team_list[i].team_midfielders[5].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[6].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[7].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[8].name, ",\t ",
    NewCompetition.competition_team_list[i].team_midfielders[9].name, ",\t "
    )


for i in range(len(NewTeamList)):
    print("[",i+1,"]", NewTeamList[i], " - ", "\t Valore Fantacalcio della rosa dei centrocampisti :\t", NewCompetition.competition_team_list[i].get_value_mid())

print("Premere invio per procedere.")

print(""" _______  _______  _______  _______  _______  _______  _______  __    _  _______  ___
|   _   ||       ||       ||   _   ||       ||       ||   _   ||  |  | ||       ||   |
|  |_|  ||_     _||_     _||  |_|  ||       ||       ||  |_|  ||   |_| ||_     _||   |
|       |  |   |    |   |  |       ||       ||       ||       ||       |  |   |  |   |
|       |  |   |    |   |  |       ||      _||      _||       ||  _    |  |   |  |   |
|   _   |  |   |    |   |  |   _   ||     |_ |     |_ |   _   || | |   |  |   |  |   |
|__| |__|  |___|    |___|  |__| |__||_______||_______||__| |__||_|  |__|  |___|  |___| """)

input("Premere invio per avviare la fase di selezione degli attaccanti. Le prime 6 estrazioni avverranno in maniera esplicita. Le estrazioni vengono eseguite per pick order alternati.")

for q in range(6):
    print("Estrazione numero ", q+1)
    if q%2 == 0:
        for i in range(len(NewTeamList)):
            NewCompetition.competition_team_list[i], forwards = get_and_remove_elite_fw(NewCompetition.competition_team_list[i], forwards)
            print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_forwards[q].name)
    else:
        for i in reversed(range(len(NewTeamList))):
            NewCompetition.competition_team_list[i], forwards = get_and_remove_elite_fw(NewCompetition.competition_team_list[i], forwards)
            print("Tocca a ", NewTeamList[i], "\tche ha ricevuto: \t", NewCompetition.competition_team_list[i].team_forwards[q].name)
    print("Attaccanti rimasti: ", len(defenders))
    input("Premere invio")

input("Premere invio per procedere al resto delle estrazioni (4)")

for q in range(4):
    print("Estrazione addizionale numero ", q+1)
    if q%2 == 0:
        for i in range(len(NewTeamList)):
            NewCompetition.competition_team_list[i], forwards = get_and_remove_elite_fw(NewCompetition.competition_team_list[i], forwards)
    else:
        for i in reversed(range(len(NewTeamList))):
            NewCompetition.competition_team_list[i], forwards = get_and_remove_elite_fw(NewCompetition.competition_team_list[i], forwards)
    print("Attaccanti rimasti: ", len(forwards))

print(""" _______  _______  _______  _______  _______  _______  _______  __    _  _______  ___
|   _   ||       ||       ||   _   ||       ||       ||   _   ||  |  | ||       ||   |
|  |_|  ||_     _||_     _||  |_|  ||       ||       ||  |_|  ||   |_| ||_     _||   |
|       |  |   |    |   |  |       ||       ||       ||       ||       |  |   |  |   |
|       |  |   |    |   |  |       ||      _||      _||       ||  _    |  |   |  |   |
|   _   |  |   |    |   |  |   _   ||     |_ |     |_ |   _   || | |   |  |   |  |   |
|__| |__|  |___|    |___|  |__| |__||_______||_______||__| |__||_|  |__|  |___|  |___| """)

print("Premere invio per procedere.")

print("Ecco un riepilogo degli attaccanti: ")

for i in range(len(NewTeamList)):
    print("[",i+1,"]", NewTeamList[i], ":  \n",
    NewCompetition.competition_team_list[i].team_forwards[0].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[1].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[2].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[3].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[4].name, ",\n ",
    NewCompetition.competition_team_list[i].team_forwards[5].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[6].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[7].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[8].name, ",\t ",
    NewCompetition.competition_team_list[i].team_forwards[9].name, ",\t "
    )


for i in range(len(NewTeamList)):
    print("[",i+1,"]", NewTeamList[i], " - ", "\t Valore Fantacalcio della rosa degli attaccanti :\t", NewCompetition.competition_team_list[i].get_value_fw())

print("Premere invio per procedere.")

print(""" ______    ___   _______  _______  _______  _______  ___   _______  ___      _______  __    _  ______   _______
|    _ |  |   | |       ||   _   ||       ||       ||   | |       ||   |    |   _   ||  |  | ||      | |       |
|   | ||  |   | |       ||  |_|  ||    _  ||_     _||   | |   _   ||   |    |  |_|  ||   |_| ||  _    ||   _   |
|   |_||_ |   | |       ||       ||   |_| |  |   |  |   | |  | |  ||   |    |       ||       || | |   ||  | |  |
|    __  ||   | |      _||       ||    ___|  |   |  |   | |  |_|  ||   |___ |       ||  _    || |_|   ||  |_|  |
|   |  | ||   | |     |_ |   _   ||   |      |   |  |   | |       ||       ||   _   || | |   ||       ||       |
|___|  |_||___| |_______||__| |__||___|      |___|  |___| |_______||_______||__| |__||_|  |__||______| |_______|""")

input("Tutte le estrazioni sono state eseguite. Premere un tasto per procedere.")

for i in range(len(NewTeamList)):
    print(NewTeamList[i], " presenta una rosa dal valore pari a ------------------------------->", NewCompetition.competition_team_list[i].get_value())
    print("Portieri: ",
    NewCompetition.competition_team_list[i].team_goalkeepers[0].name, " ",
    NewCompetition.competition_team_list[i].team_goalkeepers[1].name, " ",
    NewCompetition.competition_team_list[i].team_goalkeepers[2].name, " ",
    NewCompetition.competition_team_list[i].team_goalkeepers[3].name)
    print("Difensori: ",
    NewCompetition.competition_team_list[i].team_defenders[0].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[1].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[2].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[3].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[4].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[5].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[6].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[7].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[8].name, " ",
    NewCompetition.competition_team_list[i].team_defenders[9].name, " ",)
    print("Centrocampisti: ",
    NewCompetition.competition_team_list[i].team_midfielders[0].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[1].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[2].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[3].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[4].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[5].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[6].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[7].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[8].name, " ",
    NewCompetition.competition_team_list[i].team_midfielders[9].name, " ")
    print("Attaccanti:",
    NewCompetition.competition_team_list[i].team_forwards[0].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[1].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[2].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[3].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[4].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[5].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[6].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[7].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[8].name, " ",
    NewCompetition.competition_team_list[i].team_forwards[9].name, " ")
    print("\n")
