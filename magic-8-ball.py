import random
##Make the list of possible answers
answers=("Yes-definitely", "It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "Better not tell you now", "My sources say no", "Outlook not so good", "Very doubtful", "No", "No", "No", "No")

# Different way to do answers. 
#if random_number == 1:
  #answer = "Yes - definitely"
#elif random_number == 2:
  #answer = "It is decidedly so"
#elif random_number == 3:
  #answer = "Without a doubt"
#elif random_number == 4:
 # answer = "Reply hazy, try again"
#elif random_number == 5:
  #answer = "Ask again later"
#elif random_number == 6:
  #answer = "Better not tell you now"
#elif random_number == 7:
  #answer = "My sources say no"
#elif random_number == 8:
  #answer = "Outlook not so good"
#elif random_number == 9:
  #answer = "Very doubtful"
#else:
  #answer = "Error"
  



# Allow user inputs for name and question
#name = input("What is your name? ")
#question = input("What is your question? ")

# Set a name and question
name = "Spongebob"
question = "Magic Conch, will I ever get married?"

# Print the question and a random answer
#print(f"{name} asks: {question}")
#print(f"Magic 8-Ball's answer: {answer}") 
#print(f"Magic 8-Ball's answer: {random.choice(answers)}")
if name == "":
  print(f"Question: {question}")
else: 
  print(f"{name} asks: {question}")

if question == "":
  print("Please ask a question first.")
else:
  print(f"Magic 8-Ball's answer: {random.choice(answers)}")


