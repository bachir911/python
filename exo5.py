#ecrire un programme qui permet a un emeteur d'envoyer une somme a un recepteur.
#l'emeteur, le recepteur ansi que la somme doivent etre saisi au clavier
#les frais d'envoi son estimés a 1000
#si le montant a envoyé est superieur aux frais le recepteur recoit la difference
#sinon un message est affiché a l'utilisateur lui indiquant que "ce montant est insuffisant"


recepteur = input("veuiller entrer le nom du recepteur")

emetteur = input("veuiller entrer le nom de l'emetteur")

frais = 1000

somme = int(input("veuillez entrer le montant à envoyer"))

difference = somme - frais

if somme > frais:


   print("la difference est", difference)

else:

   print("le montant est insuffisant")
