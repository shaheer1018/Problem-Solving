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





def main():
    # Problem 1
    print('Problem 1')
    age = 25
    classify_age(age)

    # Problem 2
    print('Problem 2')
    age = 25
    day = 'Wednesday'
    movie_ticket_price(age, day)

    # Problem 3
    print('Problem 3')
    score = 91
    letter_grade(score)

    

if __name__ == '__main__':
    main()