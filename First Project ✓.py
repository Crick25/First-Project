#ask if like basketball, if yes display nba heights the same, if no ask if like football,
#if yes display football heights the same, if no to that print you boring cunt
#height from 5ft8 to 6ft5

myString = 'User'
print ("Hello " + myString)

name = input("What is your name?:  ")
type(name)

print("Welcome, " + name + "!")
age = input("And how old are you, " + name + "?:  ")
type(age)

height = input("What is your height in CM, " + name + "?:  ")
type(height)
           
sport = input("Are you a fan of a sport? If so which sport? ")
type(sport)

infoM = input("Type 'info' to display your saved information ")
type(infoM)

info = 'info'
if infoM == info:
    print("Here is what you've told me: ")
    print ("Your name is " + name + ",")
    print ("you are " + age + " years old,")
    print (height + "cm tall")
    print ("and you enjoy watching " +sport + ".")
    
