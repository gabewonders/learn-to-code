stock_info = {}


def add_stock_info(day, stock_price):
	"""adds a day and stock price to the dictionary"""
	global stock_info
	stock_info[day] = stock_price


def print_stock_info():
	"""prints all stock prices in the dictionary"""
	for key, value in stock_info.iteritems():
		print "The stock price on %s was $%s." % (key, value)


def get_greatest_stock_price():
	"""Returns the greatest stock price from your dictionary"""
	greatest_stock_price = 0
	for key, value in stock_info.iteritems():
		if greatest_stock_price < value:
			greatest_stock_price = value

	return greatest_stock_price
		

def main ():
	"""Runs the program"""
	number_of_stocks = int(raw_input("How many stocks do you want to enter: "))
	count = 0
	while (count < number_of_stocks):
		day = raw_input("Please enter a date in the following format YYYY-MM-DD: ")
		stock_price = float(raw_input("Please enter a stock price: "))
		add_stock_info(day, stock_price)
		count += 1
	
	print_stock_info()
	print "The highest stock price is $%s." % (get_greatest_stock_price())


#Runs main method
main()
