#Clara Riley
#09/11/24
#Average Ages

def average_age():

    # Get User Input
    age_1 = int(input('Friend 1: '))
    age_2 = int(input('Friend 2: '))
    age_3 = int(input('Friend 3: '))
    age_4 = int(input('Friend 4: '))
    age_5 = int(input('Friend 5: '))

    # Sum ages
    age_sum = (age_1 + age_2 + age_3 + age_4 + age_5)

    # Average the ages
    age_average = (age_sum / 5)
    # Print the results
    print('The average age of your friends is ', age_average)

# Line which calls the above function.
average_age()
