#!/usr/bin/python3

#import random
#
questions = [
   "What is the capital of France?Paris,Yerevan,Berlin,Moscow",
   "What is the capital of Armenia?Yerevan,Paris,Berlin,Moscow",
   "What is the capital of Germany?Berlin,Yerevan,Paris,Moscow",
   "What is the capital of Spain?Madrid,Yerevan,Berlin,Moscow",
   "What is the capital of Portugal?Lisbon,Yerevan,Berlin,Moscow",
   "What is the capital of Georgia?Tbilisi,Yerevan,Berlin,Moscow",
   "What is the capital of Belarus?Minsk,Yerevan,Berlin,Moscow",
   "What is the capital of Ukrain?Kiev,Yerevan,Berlin,Moscow",
   "What is the capital of Norway?Oslo,Yerevan,Berlin,Moscow",
   "What is the capital of Australia?Canberra,Yerevan,Berlin,Moscow",
   "What is the capital of Japan?Tokio,Yerevan,Berlin,Moscow",
   "What is the capital of China?Beijing,Yerevan,Berlin,Moscow",
   "What is the capital of USA?Washington,Yerevan,Berlin,Moscow",
   "What is the capital of Canada?Ottawa,Yerevan,Berlin,Moscow"
]

game_questions = []

while len(game_questions) < 10:
   num = random.randint(0, len(questions)-1)
   if questions[num] not in game_questions:
       game_questions.append(questions[num])

gquestions = {}
for el in game_questions:
   q,a = el.split("?")
   gquestions[q] = a.split(",")

cnt = 0

variant = ["A", "B", "C", "D"]
cvariant = ""
for q,a in gquestions.items():
   print(q)
   correct = a[0]
   random.shuffle(a)
   for i in range(len(variant)):
       print(variant[i], a[i])
       if a[i] == correct:
           cvariant = variant[i]
   answer = input("Your variant: ")
   if answer.upper() == cvariant:
       cnt += 1
       print("Correct.")
   else:
       print("Not. Correct answer was: ", correct)

print("You got %d/10" %cnt)

coutries = {
        "Japan":"Tokio",

        }


"What is the capital J"
"YOur answer: " 

time

mistakes once
mistakes 3 times
10 second for each answer












