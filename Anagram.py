
print("Anagramm Test für Bürgerwerke eG")
print("geschriben von Mehrdad Farokhy")
print('Gebe bitte dein zwei worter ein')

word1 = input()

word2 = input()

print('Hello, ' + word1 +word2)

print("Sind Sie bereit, Anagramme mit meinem Python-Programm zu finden? Los geht's!")
print("")
print("")



result1 = list()
result2 = list()
for item in word1:
  result1.append(item)
for item in word2:
  result2.append(item)
result1.sort()
result2.sort()
  



if (result1==result2) and (len(word1)==len(word2)) :
	print (word1+" und "+word2+" sind Anagramme")
else :
	print ("Keinen Anagramm Gefunden")
	print ("Hier sind die buchstaben auf gelistet")
	print (result1)
	print (result2)
	if (result1==result2):
			print("waren die listen gleich dennoch kein Anagramm! die lange waren verschiden.")
			print (len(word1))
			print (len(word2))
	
