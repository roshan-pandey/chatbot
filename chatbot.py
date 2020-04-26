from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
import time

# movie_lines = pd.read_csv('dataset/corpus/sample.txt', sep = '\n', encoding = 'unicode_escape')

# print(movie_lines.head())
chatbot1 = ChatBot("BotBot")
chatbot2 = ChatBot("TobTob")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "I live in Rajasthan",
    "I like to eat paneer. What about you?",
    "I like Pizza!",
    "What's your hobbies?",
    "What do you like to eat?",
    "Where do you live?",
    "What's you profession?",
    "I like photography and art work"

]

trainer1 = ListTrainer(chatbot1)
trainer2 = ListTrainer(chatbot2)

trainer1.train(conversation)
trainer2.train(conversation)

query = input()
while True:
    response1 = chatbot1.get_response(query)
    print("BotBot: ",response1)
    time.sleep(2)
    response2 = chatbot1.get_response(response1)
    print("TobTob: ",response2)
    if query == 'exit':
        break
