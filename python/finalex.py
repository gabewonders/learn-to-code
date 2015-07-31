stock_info = {}

def add_stock_info(day, stock_price):
    """adds a day and stock price to the dictionary"""
    global stock_info
    // your code here


def print_stock_info():
    """prints all stock prices in the dictionary"""
    for key, value in stock_info.iteritems():
      // your code here


def get_greatest_stock_price():
    """Returns the greatest stock price from your dictionary"""
    greatest_stock_price = 0
    // your code here
		

def main ():
    """Runs the program"""
    number_of_stocks = int(raw_input("How many stocks do you want to enter: "))
    
    // your code here
    // tip: convert the stock price to a float like this
    // stock_price = float(raw_input("Please enter a stock price: "))
    
    print_stock_info()
    print "The highest stock price is $%s." % (get_greatest_stock_price())


#Runs main method
main()