#Chiffrement syméreique

def crypt(word):
	word = word.lower()
	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
	totaletters = 26
	numletter = []
	numkey = []
	numcrypt = []
	key = "thisistherandomgeneratedshittykeybpaeqmjvf"
	crypted = []


	i=0
	j=0
	while i != len(word):
		while word[i] != letters[j]:
			j=j+1
		else :
			numletter.append(j)
			i=i+1
			j=0		
	print("\n",numletter)


	i=0
	j=0
	while i != len(key):
		while key[i] != letters[j]:
			j=j+1
		else :
			numkey.append(j)
			i=i+1
			j=0
	print(numkey)


	i=0
	while i != len(word):
		numcrypt.append(numkey[i]+numletter[i])
		i=i+1
	print(numcrypt)



	j=0
	for thing in numcrypt:
		if numcrypt[j] > totaletters:
			numcrypt[j] = (numcrypt[j] - totaletters)
			j=j+1
		else:
			j=j+1
	print(numcrypt)

	i=0
	j=0
	for thing in numcrypt:
		crypted.append(letters[numcrypt[i]])
		i=i+1
	print(crypted)
	print("\nResult:","".join(crypted))

mot = input("Text to crypt : ")
crypt(mot)

