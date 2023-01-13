# Age Calculator
current_year = 2022
user_birth_year = int(input("What Is Your Birth Year\n\n"))
age = (current_year-user_birth_year)
print(age)

if age <12 :
    print("You are a child!")

if age == 12 :
    print("You are a pre-teenager!")

if age == 13 :
    print("You are a teenager!")

if age >13 :
    print("You are a pre-adult!")

if age == 18 :
    print("You are an adult!")

if age >18 :
    print("You are an adult!")