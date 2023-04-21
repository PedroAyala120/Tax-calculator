#The program will ask the user to enter the amount of purchase. The program then computes the predetermined state and county sales tax
#Pedro Ayala

STATE_TAX = .05     #state tax global
COUNTY_TAX = 2.5    #county tax global

def main():
    
    price = float(input('Enter the amount of the puchase:'))        #ask for user to input purchase amount

    print('The amount purchased was: $', price)     #print original price
    print('State sales tax: ', STATE_TAX, '%')      #print state tax
    print('County sales tax: ', COUNTY_TAX, '%')    #print county tax


    total_tax = calc_sales_tax()        #call function to calculate total sales tax
    print('Total sales tax: ', total_tax, '%')      #print total sales tax


    total = calc_sales_price(price)     #call function
    print('Total sale price with tax: $', total)    #print total sale price


#function to calculate total sales tax
def calc_sales_tax():
    
    total_tax = STATE_TAX + COUNTY_TAX
    return total_tax        #return total sales tax

    main()  #return to main


#function to calculate the total sale price
def calc_sales_price(price):
    
    total = ((price + STATE_TAX) + COUNTY_TAX)
    return total        #return total sale price

main()  #return to main
