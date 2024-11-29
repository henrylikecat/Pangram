a=input("Enter the input: ")
vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
}
"""for i in a:
    if i in vowels:
        vowels[i]+=1
print(vowels)"""
#count the occurrence of each alphabet
alphabet={
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0,
}
for i in a:
    if i in alphabet:
        alphabet[i]+=1
print(alphabet)
#Find if the number is entered by the user is a panagram or not.
number=input("Enter a number: ")
numbers={
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
}
for i in number:
    if i in numbers:
        numbers[i]+=1
print(numbers)
pangram=True
for i in numbers.values():
    if i==0:
        pangram=False
if pangram:
    print("Enter number is a pangram")
else:
    print("Enter number is not a pangram")
