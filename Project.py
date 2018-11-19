#Psuedocode
#age = input "How old are you?"
#weight = input "What is your weight in killograms?"
#height = input "What is your height in meters?"
#
#
#def calculate_calories (age, weight):
#    if age <= 9
#        calorie_intake = (22.7 * weight) + 495
#
#    elif age >=10 and age <=17
#        calorie_intake = (17.5 * weight) + 651
#
#    elif age >=18 and age <=29
#        calorie_intake = (15.3 * weight) + 679
#
#    elif age >=30 and age <=60
#        calorie_intake = (11.6 * weight) + 879
#
#    else
#        calorie_intake = (13.5 * weight) + 487
#    calorie_intake = str(calorie_intake)
#
#    return calorie_intake
#
#def calculate_BMI (weight, height):
#    BMI = weight/height^2
#    return BMI
#
#def weight_comparison (bmi):
#    weight_status = ""
#    if bmi < 18.5:
#        weight_status = "underweight"
#
#    if bmi >= 18.5 and bmi <= 24.9
#        weight_status = "normal weight"
#
#    if bmi >= 25 and bmi <=29.9
#        weight_status = "overweight"
#
#    if bmi >= 30 and bmi <=34.9
#        weight_status = "obese"
#
#    if bmi >= 35
#        weight_status = "extremely obese"
#
#    return weight_status
#
#BMI = calculate_BMI(weight,height)
#


import math

#Get user input for their age, weight and height
age = input ("How old are you?")
age = int(age)
weight = input ("What is your weight in killograms?")
weight = int(weight)
height = input ("What is your height in meters?")
height = float(height)

#function that calculates the calorie intake
def calculate_calories (age, weight):
    calorie_intake = 0
    #these equations are based off of the Worl Health Organization calorie intake equations
    #check the users age, and calculate their desired calorie intake accordingly
    if age <= 9:
        calorie_intake = (22.7 * weight) + 495
    elif age >=10 and age <=17:
        calorie_intake = (17.5 * weight) + 651
    elif age >=18 and age <=29:
        calorie_intake = (15.3 * weight) + 679
    elif age >=30 and age <=60:
        calorie_intake = (11.6 * weight) + 879
    else:
        calorie_intake = (13.5 * weight) + 487
    calorie_intake = str(calorie_intake)
    #retrun desired calorie intake
    return calorie_intake

#Calculate the users BMI from their weight and height
def calculate_BMI (weight, height):
    BMI = weight/math.pow(height,2)
    #return users bmi
    return BMI

#Figure out if the user is underwiehgt, normal weight, overweight, obese, or extremely obese
def weight_comparison (bmi):
    weight_status = ""
    #Check the bmi and see what catagory it falls under (as defined by WHO)
    if bmi < 18.5:
        weight_status = "underweight"
    if bmi >= 18.5 and bmi <= 24.9:
        weight_status = "normal weight"
    if bmi >= 25 and bmi <=29.9:
        weight_status = "overweight"
    if bmi >= 30 and bmi <=34.9:
        weight_status = "obese"
    if bmi >= 35:
        weight_status = "extremely obese"
    #return the users weight statur
    return weight_status

#Call the BMI function
BMI = calculate_BMI(weight,height)
#Calls the calculate_calories function and prints the results
print ("You should be eating " + calculate_calories(age, weight) + " calories every day")
#Calls the calculate_BMI function and prints the results
print ("Your BMI is " + str(BMI))
#Calls the weight_comparison function and prints the results
print ("Based, on your BMI you are " + weight_comparison(BMI))
