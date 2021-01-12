# ©2021 -- Jean-Hugues Roy -- GNU GPL v3.
# coding : utf-8

from parler import Parler
import json, csv

mst = "à remplir en consultant vos cookies de connexion à Parler"
jst = "à remplir en consultant vos cookies de connexion à Parler"

client = Parler(mst, jst)

fOUT = "suiveuxParler.csv"

utilisateur = "RadioQuebec"

profil = client.profile(utilisateur)
print(profil)
user = profil["_id"]

### POUR TROUVER SES FOLLOWERS

print("#"*20)
print("D'abord les FOLLOWERS de {}".format(utilisateur))
print("#"*20)

lien = "suivi par"
dernier = False
start = False
n = 0

while dernier == False:
	resultats = client.getFollowersOfUserId(user,startKey=start)
	for suiveux in resultats["followers"]:
		n += 1
		numero = suiveux["id"]
		bio = suiveux["bio"]
		nom = suiveux["name"]
		pseudo = suiveux["username"]
		score = suiveux["score"]
		joined = suiveux["joined"]
		infos = [utilisateur,lien,n,nom,pseudo,score,numero,bio,joined]
		print(infos)
		matze = open(fOUT, "a")
		mercer = csv.writer(matze)
		mercer.writerow(infos)
		print("$"*10)
	start = resultats["next"]
	dernier = resultats["last"]
	print("start = {}".format(start))
	print("dernier = {}".format(dernier))
	print("*"*20)
	print("*"*20)

### POUR TROUVER LES COMPTES QU'IL SUIT

print("#"*20)
print("Ensuite, les personnes que {} suit".format(utilisateur))
print("#"*20)

lien = "suit"
dernier = False
start = False
n = 0

while dernier == False:
	resultats = client.getFollowingOfUserId(user,startKey=start)
	for suiveux in resultats["followees"]:
		n += 1
		numero = suiveux["id"]
		bio = suiveux["bio"]
		nom = suiveux["name"]
		pseudo = suiveux["username"]
		score = suiveux["score"]
		joined = suiveux["joined"]
		infos = [utilisateur,lien,n,nom,pseudo,score,numero,bio,joined]
		print(infos)
		matze = open(fOUT, "a")
		mercer = csv.writer(matze)
		mercer.writerow(infos)
		print("$"*10)
	start = resultats["next"]
	dernier = resultats["last"]
	print("start = {}".format(start)) 
	print("dernier = {}".format(dernier)) # Infos utiles en cas de plantage
	print("*"*20)
	print("*"*20)