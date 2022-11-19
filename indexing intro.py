course = 'python course for beginners'
#Here the index is from square brackets to get on charecter
print(course[0])
#0 is the first charecter -1 is the last charecter.in the string
print(course[-1])
#we can also print a certain length of charecters bu using the folowing

print(course[0:3])
#this will print char '012' and excludes the last one specified.

print(course[6:])
#if end charecter is not specified all the charecters in the string will be selected

print(course[:12])
#if first char is left empty python interpreter assumes it as 0
#if the end charecter is empty Python interpreter assumes it as till the end of the string

#[:] can be used as a copy
another = course[:]
print(another)

#we can re use this multiple times.
print(another[1:-1])