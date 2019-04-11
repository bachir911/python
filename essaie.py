#Condition alternative en boucle

from random import randint

random_gamer = randint(0,9)

gamer_answer = 3

while gamer_answer > 0:

   gamer = int(input("veuillez entrez un numero compris entre 0 et 9: "))

   if gamer == random_gamer:

      print ("Bravo, tu as gagne")

      break

   elif gamer != random_gamer:

      print ("oups! essai encore")

   gamer_answer -= 1

else:

      print ("Desole, echoué 3 fois!")
