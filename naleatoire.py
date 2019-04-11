#Nombre aleatoire entre 0 et 9

from random import *

r = randint(0,9)

n = input ("veuillez entrez un nombre entre 0 et 9 : ")

if r == n:
   print ("bravo,vous avez gagné")
else:
   print ("perdu! retry!")


