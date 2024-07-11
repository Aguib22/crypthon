from cryptage import *

# fonction de cryptage

def crypt(message,cle):
	cle = int(cle)

	messageCrypt =""

	#boucle de parcourir du message
	for lettre in message:

		for indice,lettre_alpha in alphabet.items():
			if lettre == lettre_alpha:

				indice +=cle

				while indice > len(alphabet) - 1:
					indice -= len(alphabet)
					
				messageCrypt += alphabet[indice]

	return messageCrypt

# fonction de decryptage

def decrypt(message,cle):

	cle = int(cle)
	message_decrypter = ""

	for lettre in message:

	 	for indice,lettre_alpha in alphabet.items():

	 		if lettre == lettre_alpha:
	 			indice -= cle

	 			while indice < 0:
	 				indice += len(alphabet)

	 			message_decrypter += alphabet[indice]

	return message_decrypter

