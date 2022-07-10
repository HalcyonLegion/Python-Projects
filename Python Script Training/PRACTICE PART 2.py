from math import*

#I can't think of an application for this, but it's a program which calculates how many slices of pizza you ate and therefore how
#much you should pay...?

name_1=input("What is your name?")
name_2=input("What is your name?")
name_3=input("What is your name?")

slices_in_the_pizza=input("How many slices are in the Pizza? ")
price_of_the_pizza=input("What is the price of the Pizza? ")

percentage_ate_by_person_1=input(name_1+ " What percentage of the Pizza did you eat? ")
percentage_ate_by_person_2=input(name_2+ " What percentage of the Pizza did you eat? ")
percentage_ate_by_person_3=input(name_3+ " What percentage of the Pizza did you eat? ")

number_of_slices_ate_person_1=float(percentage_ate_by_person_1)*float(slices_in_the_pizza)
number_of_slices_ate_person_2=float(percentage_ate_by_person_2)*float(slices_in_the_pizza)
number_of_slices_ate_person_3=float(percentage_ate_by_person_3)*float(slices_in_the_pizza)

price_paid_by_name_1=float(percentage_ate_by_person_1)*float(price_of_the_pizza)
price_paid_by_name_2=float(percentage_ate_by_person_2)*float(price_of_the_pizza)
price_paid_by_name_3=float(percentage_ate_by_person_3)*float(price_of_the_pizza)

print(name_1+" has eaten "+str(number_of_slices_ate_person_1)+" slices and has paid "+str(price_paid_by_name_1)+"£ for his meal ")
print(name_2+" has eaten "+str(number_of_slices_ate_person_2)+" slices and has paid "+str(price_paid_by_name_2)+"£ for his meal ")
print(name_3+" has eaten "+str(number_of_slices_ate_person_3)+" slices and has paid "+str(price_paid_by_name_3)+"£ for his meal ")