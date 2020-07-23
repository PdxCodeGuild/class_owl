import random

answers= ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.",
"You may rely on it.","As I see it yes.","Most likely","Outlook good.","Yes.","Signs point to yes",
"Reply hazy, try again.","Ask again later","Better not tell you now.","Cannot predict now.",
"Concentrate and ask again.","Don't count on it.","My reply is no","My sources say no.","Outlook not so good",
"Very doubtful."]

chosen_saying = random.choice(answers)

print ("Welcome to the Magic 8 Ball!")

question = input("What is your question?: ")

print (question)

print (f'''"Searching my magic globe..."
{chosen_saying}.''')

second_questions = input("Do you want to ask another question: ").lower()

chosen_saying = random.choice(answers)

if second_questions == 'yes':
    input ("What is your question: ")
    print (chosen_saying)
elif second_questions == 'no':
    print ("Thank you for playing")
