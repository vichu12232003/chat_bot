import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me ChatBot."]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you.", "I'm doing well."]
    ],
    [
        r"quit|bye|Bye",
        ["Bye! Take care."]
        
    ],
    [
        r"how old are you?",
        ["I am a computer program, so I don't have an age."]
    ],
    [
        r"what can you do?",
        ["I can assist you with various tasks, answer questions, or have a casual conversation."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"how's the weather today\?",
        ["I'm sorry, but I don't have access to real-time data. You can check a weather website or app for that!"]
    ],
    [
        r"(.*) (love|like) you (.*)",
        ["Aww, that's sweet!", "Thanks! I'm just a program, but I'm glad you like me."]
    ],
    [
        r"(.*) (hungry|thirsty|tired)",
        ["I'm just a computer program, so I don't experience physical sensations."]
    ],
]

def chatbot():
    print("Hello! I'm ChatBot. How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.chat.util.reflections = reflections
    chatbot()

