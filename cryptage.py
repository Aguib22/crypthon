import string

toute_lettre = list(string.ascii_letters + string.punctuation + string.digits +" ")
alphabet = {}
i = 0
while i!= len(toute_lettre):

	alphabet[i] = toute_lettre[i]
	i+=1
 
