
import pandas as pd
import random

#~# User questions
user_question = {
    "greeting": [
        "hi", "hello", "hey", "hii", "heyy bro"
    ],

    "order_status": [
        "where is my order",
        "track my order",
        "order kaha hai"
    ],

    "refund": [
        "i want refund",
        "return product",
        "refund chahiye"
    ],

    "product_query": [
        "product details",
        "is it available",
        "price kya hai"
    ],

    "complaint": [
        "not working",
        "very bad service",
        "issue aa raha hai"
    ],

    "farewell": [
        "bye",
        "thanks",
        "ok bye",
        "see you"
    ]
}

#~# Bot responses
bot_reply = {
    "greeting": [
        "Hello! How can I help?",
        "Hi there!"
    ],

    "order_status": [
        "Please share order ID",
        "Tracking details bhej raha hu"
    ],

    "refund": [
        "Refund initiated",
        "Return process start kar raha hu"
    ],

    "product_query": [
        "Here are product details",
        "Available hai"
    ],

    "complaint": [
        "Sorry for inconvenience",
        "Issue resolve karte hain"
    ],

    "farewell": [
        "Goodbye!",
        "Thanks for contacting"
    ]
}

#~# Sentiment labels
sentiments = ["positive", "neutral", "negative"]

data = []

conversation_id = 1

#~# Generate 200 conversations
for _ in range(20):

    user_id = random.randint(3000, 4000)

    #~# Each conversation contains 3 to 8 turns
    turns = random.randint(3, 8)

    for turn in range(turns):

        intent = random.choice(list(user_question.keys()))

        user_msg = random.choice(user_question[intent])

        bot_msg = random.choice(bot_reply[intent])

        #~# Append conversation row
        data.append({
            "conversation_id": conversation_id,
            "user_id": user_id,
            "turn": turn + 1,
            "intent": intent,
            "user_message": user_msg,
            "bot_response": bot_msg,
            "sentiment": random.choice(sentiments)
        })

    conversation_id += 1

#~# Create DataFrame
df = pd.DataFrame(data)

#~# Save dataset into CSV file
df.to_csv("chatbot_dataset.csv", index=False)

print("Dataset created successfully")