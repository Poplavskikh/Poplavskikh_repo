# List creation
things = ["mozzarella", "cinderella", "salmonella"]
# Writing an element with a capital litter
things[1] = "Cinderella"
print(things)
# Element conversion to upper case
X = things[0].upper()
things[0] = X
print(things)
# Remove item from list
del things[2]
print(things)

# Dictionary making
live = {"animals": 1, "plants": 2, "other": 3}
print(live)
# Adding a second dictionary
live["animals"] = {"cats": 1, "octopi": 2, "emus": 3}
# Add list
live["animals"]["cats"] = ["Henri", "Grumpy", "Lucy"]
# Add tuple
live["animals"]["octopi"] = ("Doctor Octopus", "The Kraken", "Squidward")
print(live)
print(live["animals"])
print(live["animals"]["cats"])
print(live["animals"]["octopi"])
