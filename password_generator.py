letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random
pw1=""
pw2=""
pw3=""

for i in range(1,nr_letters+1):
    l=random.choice(letters)
    pw1=pw1+l
#print(pw1)
for k in range(1, nr_symbols+1):
    s=random.choice(symbols)
    pw2=pw2+s
#print(pw2)
for j in range(1,nr_numbers+1):
    n=random.choice(numbers)
    pw3=pw3+n
#print(pw3)

pw4=pw1+pw2+pw3
final_pw=""
for a in range(1, len(pw1)+len(pw2)+len(pw3)+1):
    final_pw=final_pw+random.choice(pw4)
print(f"Your password is: {final_pw}")
