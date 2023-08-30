#three arguments versus one
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
print()
print("The itsy bitsy spider climbed up the waterspout.")
#positional argument
print("My name is", "Python.")
print("Monty Python.")
#keyword argument
print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My name is ", end="")
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")
#Both keyword arguments may be mixed in one invocation, just like here in the editor window.

#The example doesn't make much sense, but it visibly presents the interactions between end and sep.
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

