#dynamically generate some text wiht variables.
firstname = 'jon'
lastname = 'bone'
#jon [bones] is a coder
message = firstname + ' [' + lastname + '] is a coder'
print(message)
# f represents formatted sting
msg = f'[{firstname}] {[lastname]} is a coder'
#difference between square brackets inside the curly braces and outside the curly braces.
print(msg)

