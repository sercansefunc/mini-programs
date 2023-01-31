import random

game=['rock','paper','scissors']

score1,score2=0,0

rounds = input ("How many rounds you want to play?")

for i in range (0,int(rounds)):
  choice_1 = random.choice(game)
  choice_2 = random.choice(game)
  print(choice_1,choice_2)
  if(choice_1==choice_2):
    score1,score2=score1,score2
  elif((choice_1=="rock" or choice_2 == "rock") and (choice_1=="scissors" or choice_2 == "scissors")):
    if(choice_1=="rock"):
      score1+=1
    else:
      score2+=1
  elif((choice_1=="rock" or choice_2 == "rock") and (choice_1=="paper" or choice_2 == "paper")):
    if(choice_1=="rock"):
      score2+=1
    else:
      score1+=1
  elif((choice_1=="paper" or choice_2 == "paper") and (choice_1=="scissors" or choice_2 == "scissors")):
    if(choice_1=="paper"):
      score2+=1
    else:
      score1+=1

print(score1,",",score2)
if (score1>score2):
  print("Player 1 wins!")
elif(score2>score1):
  print("Player 2 wins!")
else:
  print("Tie!")
