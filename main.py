#28/06/22  Nikora Muriwai-Ihimaera Te Reo Quiz
#v.1.1

#importing the random libary
import random

#welcome to quiz
print ("Kia Ora, Ko Wai Tou Ingoa? / Hello, What Is Your Name")
name = input()
print ("Nau Mai Haere Mai / Welcome " + name)

#Chances
chances = 1
print("You Will Have", chances ,"Chance To Answer Correctly, Please Answer With The Following: A, B, or C")

#globals and questions lists
score = 0
english = ["Fight", "Right", "Hungry", "Love", "Left"]
right_answer = ["Whawhai", "None", "Hiakai", "Aroha", "Maui"]
option_1 = ["Maui", "Whānau", "Hakari", "Ngakau", "Moana"]
option_2 = ["Kaha", "Maui", "Hangi", "Tokorua", "Whero"]

#define a function to generate a question
def generate_question(english,right_answer, option_1, option_2):
  global score
  print("What is the correct word for", english, "in te reo")
  #generate a random number to determine the sequence of questions
  random_sequence = random.randint(0,4)
  #seperate print statements for readability
  if(random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
      print("ka pai / good job") 
    else:
      print("hē / incorrect.")
  if(random_sequence == 1):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
      print("ka pai / good job") 
    else:
      print("he / incorrect.")
  if(random_sequence == 2):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
      print("ka pai / good job") 
    else:
      print("he / incorrect.")
  if(random_sequence == 3):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
      print("ka pai / good job") 
    else:
      print("he / incorrect.")
  if(random_sequence == 4):
    print("A", option_2)
    print("B", option_1)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
      print("ka pai / good job") 
    else:
      print("he / incorrect.")

  #generate 5 questions pulling possible answers from lists.
for i in range (0,5):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])

  #print the score at the end of quiz
while score >= 5:
  print ("Tino Pai! Your Score Was", score)
  break

while score <=4:
  print ("Aroha Mai, Your Score Was", score ,"Better Luck Next Time")
  break

#Goodbye message
print("Nga Mihi " + name, "For Playing My Te Reo Quiz")
  
  