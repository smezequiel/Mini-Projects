print("Welcome to my quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("That's correct!")
    score += 1  # score = score + 1
else:
    print("Wrong answer")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("That's correct!")
    score += 1
else:
    print("Wrong answer")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("That's correct!")
    score += 1
else:
    print("Wrong answer")


print("You got " + str(score) + " questions correct")
