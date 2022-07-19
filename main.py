print("Welcome to the Trivia Quiz!")

playing = input("Do you want to play the game? ")


if playing == "no":
    print("Maybe next time!")

if playing.lower() != "yes":
    quit()

print("Ok! Let's move on to the Trivia. ")
score = 0

answer = input("What is the Capital of Ohio? ")
if answer.lower() == "columbus":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("Which President had two non-consecutive terms? ")
if answer.lower() == "grover cleveland":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What company did Mark Zuckerberg found in 2004? ")
if answer.lower() == "facebook":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What was YouTube's iconic slogan for many years?  ")
if answer.lower() == "broadcast yourself":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("In 2010, Kanye West released ____  ")
if answer.lower() == "my beautiful dark twisted fantasy":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What year did the first iPhone release?  ")
if answer.lower() == "2007":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What does IT stand for?  ")
if answer.lower() == "information technology":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What is the Capital of Washington?  ")
if answer.lower() == "olympia":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What is Google's parent company?  ")
if answer.lower() == "alphabet":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("During 2020 and the early COVID era, what hit online multiplayer game took the world by storm?  ")
if answer.lower() == "among us":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("Who won TIME Magazine's Person of the Year Award in 2006?  ")
if answer.lower() == "you":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What does CD stand for? ")
if answer.lower() == "compact disc":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What year was believed to be the end of the world? ")
if answer.lower() == "2012":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What is the end of a shoelace called? ")
if answer.lower() == "aglet":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What is the Capital of Texas? ")
if answer.lower() == "austin":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("When did Gangnam Style release? ")
if answer.lower() == "2012":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What is the Capital of California? ")
if answer.lower() == "sacramento":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("In the hit TV series Breaking Bad, what is Walter White's criminal alias? ")
if answer.lower() == "heisenberg":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

answer = input("What does NASA stand for? ")
if answer.lower() == "national aeronautics and space administration":
    print('Correct Answer, you may move on.')
    score += 1
else:
    print('Incorrect answer or format.')

print("You got " + str(score) + " questions correct")
print("You got " + str((score/20) * 100) + "%!")