#Kirjutage programm, mis käib läbi iga tähe sõnes ja prindib selle välja.

# text = "python"

""" for letter in text:
    print(letter)
 """ 
#Kirjutage programm, mis prindib sõne tagurpidi (viimasest tähemärgist esimese juurde), nii et iga täht kuvatakse eraldi reale.


text = "hello"

for i in range(len(text) -1, -1, -1):
    print(text[i])


