# From test example 003 I have seen (very possibly) the batch limit is 20.
# To make sure it's not/less relavant to context length,
# I will test it with some complicated questions.

import os
import time
from huggingface_hub import InferenceClient

client = InferenceClient()

# I have five requests
user_requests = [
    "Explain the origin of the term Doge",
    "What is a 'Crescendo' in terms of piano?",
    "What is first principle theory?",
    "Briefly introduce mathematical expectation and its usage",
    "What era was it when it was 200AD?",
    "Explain what do people do most with Python Django frame",
    "What is a event-driven architecture that many programmer use?",
    "What is the nutrition difference between beef bone and chicken bone?",
    "What are the procedures to make a body pillow?",
    "What is a Tremolo in terms of piano?",
    "Give me some recommandations for my next meal please",
    "What is INFP personality?",
    "Briefly introduce the history of Roman Empire",
    "What does Topology study?",
    "Can you calculate the intercept of functions 3x+2y+3z=3 and -y+3z-x=1",
    "Prove a transpose of the transpose of a matrix is the matrix itself",
    "What is an amide? Explain its Louis structure.",
    "Explain what does Context Length mean in terms of modern LLM models",
    "What do u think of the model gpt-4o?",
    "What is the sum of 20+20",
    "What is the origin of the term 'BRUH'"
]


# the messages, an array of several elements
# each element is a dictionary with "role" and "content"
messages = [
    {"role": "user", "content": request} for request in user_requests
]

start_time = time.time()

# Make a single API call with the batch of messages
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=messages
)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")

# examine the object type of each choice
# print the type of each choice in completion.choices
for i, choice in enumerate(completion.choices):
    print(f"the type of choice {i} (i starts at 0) : {type(choice)}")



# print the responses for each user request
for i, choice in enumerate(completion.choices):
    print(f"Response to request {i+1}: {choice.message.content}\n")

# My guess is the 128K context length is not abundant enough for the model to 
# generate 20 results for complicated questions.

###################################
###################################
# C:\bruh\bruhh\bruhhh\AgentCommunication> python test_example_004.py
# Execution time: 8.492140293121338 seconds
# the type of choice 0 (i starts at 0) : <class 'huggingface_hub.inference._generated.types.chat_completion.ChatCompletionOutputComplete'>
# Response to request 1: The term **"Doge"** (pronounced *dohj*) originated as an internet meme in the early 2010s, featuring a Shiba Inu dog with broken, comic-style captions in **multicolored Comic Sans font** (e.g., "such wow," "very amaze"). Here’s a breakdown of its evolution:

# 1. **Pre-Meme Origins (2005–2010)**
#    - The word "doge" was an accidental misspelling of "dog" in a 2005 episode of *Homestar Runner*, but this wasn’t the direct source.
#    - The iconic Shiba Inu, named **Kabosu**, belonged to a Japanese teacher. Her photo was posted on her owner’s blog in 2010, showing Kabosu with raised eyebrows and a side-eye glance.

# 2. **Meme Explosion (2013–2014)**
#    - The image went viral on **Tumblr**, **Reddit**, and **4chan**, paired with **"Doge Speak"**—a parody of pidgin English (e.g., "so scare," "much happy").
#    - The absurd humor and the dog’s expressive face made it a staple of internet culture.

# 3. **Cryptocurrency Tie-In (2013–Present)**
#    - In 2013, the meme inspired **Dogecoin (DOGE)**, a satirical cryptocurrency that later gained real-world value and a cult following (boosted by Elon Musk’s tweets).

# 4. **Legacy**
#    - Doge became a symbol of internet absurdity and wholesome humor. Kabosu’s image remains one of the most recognizable memes in history.

# **Fun Fact:** In 2024, Kabosu’s owner announced the dog’s (likely) final photo due to her age, reigniting nostalgia for the meme.

# Would you like details on specific aspects (e.g., linguistic quirks, Dogecoin’s impact)?