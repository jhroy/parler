# ©2021 -- Jean-Hugues Roy -- GNU GPL v3.
# coding : utf-8

from parler import Parler
import json, csv

mst = "à remplir en consultant vos cookies de connexion à Parler"
jst = "à remplir en consultant vos cookies de connexion à Parler"

client = Parler(mst, jst)

fIN = "tousElus.csv"
fOUT = "elusParler.csv"

f1 = open(fIN)
elus = csv.reader(f1)
next(elus)

for elu in elus:
	
	# Pour suivre le travail de notre script, on écrit dans le terminal le nom de l'élu qu'on va chercher dans Parler
	
	print(elu[3].replace("Honourable","").strip())

	# Étape 1 -- On écrit, dans notre CSV final, quelques données sur l'élu qu'on va chercher dans Parler
	
	matze = open(fOUT, "a")
	mercer = csv.writer(matze)
	mercer.writerow([elu[3].replace("Honourable","").strip(),elu[0],elu[1],elu[7]])

	# Étape 2 -- On cherche l'élu...

	resultats = client.userSearch(username=elu[3].replace("Honourable","").strip())
	users = resultats["users"]

	# ... et s'il y a des résultats, on consigne le nom de chaque abonné Parler et son pseudonyme dans une ligne de notre CSV final

	for u in users:
		print(u["name"],u["username"])
		matze = open(fOUT, "a")
		mercer = csv.writer(matze)
		mercer.writerow([u["name"],u["username"]])

	# Petit séparateur pour délimiter chaque élu recherché

	print("*"*10)