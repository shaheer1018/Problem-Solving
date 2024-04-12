#=====================================================
#                  PROBLEM 1
#=====================================================
def classify_age(age):
    
    if (age < 13):
        print('Child')
    elif (13 <= age <= 19):
        print('Teenager')
    elif (20 <= age <= 59):
        print('Adult')
    else:
        print('Senior')

#=====================================================
#                  PROBLEM 2
#=====================================================
def movie_ticket_price(age, day):

    if age >= 18:
        price = 12
    else:
        price = 8

    if day.lower() == 'Wednesday':
        price = price - 2
    else:
        pass
    
    print(price)


#=====================================================
#                  PROBLEM 3
#=====================================================
def letter_grade(score):

    if 90 <= score <= 100:
        print('Grade: A')
    elif 80 <= score <= 89:
        print('Grade: B')
    elif 70 <= score <= 79:
        print('Grade: C')
    elif 60 <= score <= 69:
        print('Grade: D')
    elif score < 60:
        print('Grade: F')
    else:
        print('Enter score in the range of 0 to 100.')

#=====================================================
#                  PROBLEM 4
#=====================================================
def fruit_ripeness_checker(fruit, color):

    if fruit.lower() == 'banana':
        if color.lower() == 'green':
            print('Unripe')
        elif color.lower() == 'yellow':
            print('Ripe')
        elif color.lower() == 'brown':
            print('Overripe')
        else:
            print('Enter color "Green", "Yellow" or "Brown"')
    else:
        print('Enter fruit "Banana". ')

#=====================================================
#                  PROBLEM 5
#=====================================================
def weather_activity_suggestion(weather):

    if weather.lower() == 'sunny':
        print('Go for a walk.')
    elif weather.lower() == 'rainy':
        print('Read a book.')
    elif weather.lower() == 'snowy':
        print('Build a snowman . ')
    else:
        print('Enter "Sunny", "Rainy" or "Snowy" weather.')

#=====================================================
#                  PROBLEM 6
#=====================================================
def transportation_mode_selection(distance):
    
    if (distance < 3) and (distance > 0):
        print('Walk')
    elif (3 <= distance <= 15):
        print('Bike')
    elif (distance >= 15):
        print('Car')
    else:
        print('Enter a valid positive integer value.')
#=====================================================
#                  PROBLEM 7
#=====================================================
def coffe_customization(order_size, extra_shot):

    # order_size -> 'small', 'medium', 'large'
    # extra_shot -> True or False

    if extra_shot == True:
        print(f'{order_size} Coffee with an extra shot.')
    else:
        print(f'{order_size} Coffee with no extra shot.')
#=====================================================
#                  PROBLEM 8
#=====================================================
def password_strength_checker(password):

    if len(password) < 6:
        print('Weak password')
    elif 6 <= len(password) <= 10:
        print('Medium password')
    else:
        print('Strong password')

#=====================================================
#                  PROBLEM 9
#=====================================================
def leap_year_checker(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year} is leap year.')
    else:
        print(f'{year} is not a leap year.')

#=====================================================
#                  PROBLEM 10
#=====================================================
def pet_food_recommendation(specie, age):
    
    if specie.lower() == 'dog' and age < 2:
        print('Recommended food: Puppy food')
    elif specie.lower() == 'cat' and age > 5:
        print('Recommended food: Senior cat food')
    else:
        print('Enter specie "dog" and age a positive number less than 2. \
               Or "cat" and age a number greater than 5. ')




def main():
    # Problem 1
    print('Problem 1')
    age = 25
    classify_age(age)
    print('')

    # Problem 2
    print('Problem 2')
    age = 25
    day = 'Wednesday'
    movie_ticket_price(age, day)
    print('')

    # Problem 3
    print('Problem 3')
    score = 91
    letter_grade(score)
    print('')

    # Problem 4
    print('Problem 4')
    fruit = 'Banana'
    color = 'Yellow'
    fruit_ripeness_checker(fruit, color)
    print('')

    # Problem 5
    print('Problem 5')
    weather = 'Sunny'
    weather_activity_suggestion(weather)

    # Problem 6
    print('Problem6')
    distance = 4
    transportation_mode_selection(distance)

    # Problem 7
    print('Problem 7')
    order_size = "Small"
    extra_shot = True
    coffe_customization(order_size, extra_shot)

    # Problem 8
    print('Problem 8')
    password = 'my-secure-password'
    password_strength_checker(password)
    print('')

    # Problem 9
    print('Problem 9')
    year = 2023
    leap_year_checker(year)
    print('')

    # Problem 10
    print('Problem 10')
    specie = 'dog'
    age = 1
    pet_food_recommendation(specie, age)


if __name__ == '__main__':
    main()