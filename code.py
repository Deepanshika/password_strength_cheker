import string
import requests

password = input("Enter your password : ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password ])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])

characters = [upper_case, lower_case, digits, special]

length = len(password)
score = 0
url = 'https://raw.githubusercontent.com/Deepanshika/password_strength_cheker/main/common_passwords.txt'

response = request.get(url)
if response.status_code == 200 :
    common = response.text.splitlines()

if password in common :
    print("Password found in common list, please change")
    exit()

if length > 8 :
    score += 1
if length > 12 :
    score += 1
if length > 16 :
    score += 1
if length > 20 :
    score += 1


if sum(characters) > 1 :
    score += 1
if sum(characters) > 2 :
    score += 2
if sum(characters) > 3 :
    score += 1
if sum(characters) > 4 :
    score += 1
if sum(characters) > 5 :
    score += 1


if score < 4 :
    print("The password is weak")
elif score >= 4 and score < 6 :
    print("The password is good")
else :
    print("The password is strong")

print("REMEMBER TO UPDATE YOUR PASSWORDS REGULARLY TO KEEP YOUR ACCOUNT SECURE!")
