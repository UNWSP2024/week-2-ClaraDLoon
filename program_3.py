#Clara Riley
#09/11/24
#Reciept after Purchase

def calculate_total_purchase():


    input('What is your first item? ')
    price_1 = float(input('What is the price of your first item? '))
    input('What is your second item? ')
    price_2 = float(input('What is the price of your second item? '))
    input('What is your third item? ')
    price_3 = float(input('What is the price of your third item? '))
    input('What is your fourth item? ')
    price_4 = float(input('What is the price of your fourth item? '))
    input('What is your fifth item? ')
    price_5 = float(input('What is the price of your fifth item? '))

    subtotal = (price_1 + price_2 + price_3 + price_4 + price_5)

    tax = (subtotal * 0.07)

    total = (subtotal + tax)

    print('Your subtotal is: $',subtotal)
    print('Your tax is: $', tax)
    print('Your total is: $', total)


calculate_total_purchase()
