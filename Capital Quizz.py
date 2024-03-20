print("Welcome to my quiz game")

playing = input("do you wanna play?(y/n) ")
if playing.lower()  != "y":
    print("Okay, have a nice day!")
    quit()
print("Okay let's play!")
score=0

answer = input("What is the capital of india:")

if answer.lower()  != "delhi":
    print("Wrong!, the answer is delhi")
else:
    print("Very good, your answer is correct")
    score += 1

answer = input("What is the capital of USA:")

if answer.lower()  != "washington dc":
    print("Wrong!, the answer is washington dc")

else:
    print("Very good, your answer is correct")
    score += 1

answer = input("What is the capital of UK:")

if answer.lower()  != "london":
    print("Wrong!, the answer is london")
else:
    print("Very good, your answer is correct")
    score += 1

answer = input("What is the capital of Russia:")

if answer.lower()  != "moscow":
    print("Wrong!, the answer is moscow")
else:
    print("Very good, your answer is correct")
    score += 1

if score == 1 :
    print("You got ", score, " answer right!")
    print("You got ", (score/4 *100), " of answers right!")

else :
    print("You got ", score, " answers right!")
    print("You got ", (score /4 * 100), " of answers right!")