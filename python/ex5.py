employee_name = raw_input("What is the employees name? ")
rating = int(raw_input("Please rate the employee a 3, 2 or 1: "))
comment = raw_input("Please comment on their performance: ")

if rating == 1:
    print "%s is a rockstar!" % (employee_name)
    print "Your supervisor\'s comment was: %s" % (comment)
elif rating == 2 or rating == 3:
    print "%s has room for improvement." % (employee_name)
    print "Your supervisor\'s comment was: %s" % (comment)
else:
    print "You have entered an incorrect rating."