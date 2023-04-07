# String concatenation (aka HOw to put strings togeter)
# # suppose we want to create a string that says "Subscribe to ____"
# Youtuber = "Kylie Ying " # Some string varible

# A few ways to do this 
# Print ("Subscribe to " + Youtuber) 
# print ("subscribe to {}". format(youtuber))
# print (f"subscriber to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ") 
verb2 = input("Verb: ")
famous_person = input("Famous person ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \ I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

