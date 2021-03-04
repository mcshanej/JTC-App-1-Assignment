# Requesting information from the user about the cost of food, number of people, and tip percentage
# First I ask the user to input some information
cost = input("How much does the food in your meal cost? ")

#Found the try/except code recommendation here in the last comment: https://stackoverflow.com/questions/55885862/convert-input-str-to-int-in-python


#this checks to make sure the 'cost' input can be converted to an float. If the input can't be converted to an float or integer (as appropriate for the question), this asks them to enter a number and repeats the question. This is required because mathematical operations can only be performed on int and float.
try:
    cost = float(cost)
except:
    print('Please enter a number')
    cost = input("How much does the food in your meal cost? ")

#Converts cost input into an float
cost = float(cost)

#as above, checks to make sure that the input is an integer
people = input("How many people will be splitting the check? ")
try:
    people = int(people)
except:
    print('Please enter a whole number')
    people = input("How many people will be splitting the check? ")

#converts people input into an integer (can't have partial people)
people = int(people)

#as above, checks to make sure that the input is a float (people MAY want to leave part of a percentage, though 15.75% seems a bit strange....)
tip = input("How much of a tip would you like to leave? ")
try:
    tip = float(tip)
except:
    print('Please enter a percentage in number form')
    tip = input("How much of a tip would you like to leave? ")

#converts tip input into a float
tip = float(tip)

#Creating a variable to calculate the total cost of the meal by adding the cost of the food, the amount of the tip, and the sales tax
total = (cost) + (cost *(tip/100)) + (cost/10)

#Calculating the amoun each person owes
per_person = total / people

#Telling the user the total cost and each person's share after the tip and sales tax.
print(f"The total cost of the meal, including the tip, is ${total}. Because there are {people} people in your party, each person's share is ${per_person}.")