from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import JsonFileStorageAdapter
# Create a new instance of a ChatBot
chatbot = ChatBot('SimpleChatBot', storage_adapter='chatterbot.storage.JsonFileStorageAdapter')

# Create a new Trainer for the ChatBot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the ChatBot based on the English corpus
trainer.train("chatterbot.corpus.english")

# Start a conversation with the bot
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")
