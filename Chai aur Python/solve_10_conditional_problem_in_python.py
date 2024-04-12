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







def main():
    # Problem 1
    age = 25
    classify_age(age)


if __name__ == '__main__':
    main()