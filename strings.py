import multiPrintFunction

course = 'Python Course For "Beginners"'
# Len is a general purpose function
# print(len(course))

# When the value of a property is a function, we call it a method

# here functions specific to strings
# we use " . " operator after the stings varuable.
# when a function belongs to something else, or is specific to some kind of object, we refer to that function as a method.
# print(course.upper())


# def printten(gg):
#     i = 1
#     while i <= 6:
#         print(gg)
#         i += 1
#
# printten(course)

multiPrintFunction.printTen('prazmotj')
multiPrintFunction.printFive(course)

#this creates a new string but this wont change the existing sting.

#find the index of a char it is case sensitive and wil return -1 if the charecter is not found.
#print(course.find('P'))

#also replace charecter or charecters ina string with methos replace
#print(course.replace('Beginners', 'Absolute Beginners'))
