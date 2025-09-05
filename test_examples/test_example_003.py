# similar to test_example_002.py
# but this time I got manyy questions


import os
import time
from huggingface_hub import InferenceClient

client = InferenceClient()

# I have five requests
user_requests = [
    "What is the sum of 1+1",
    "What is the sum of 2+2",
    "What is the sum of 3+3",
    "What is the sum of 4+4",
    "What is the sum of 5+5",
    "What is the sum of 6+6",
    "What is the sum of 7+7",
    "What is the sum of 8+8",
    "What is the sum of 9+9",
    "What is the sum of 10+10",
    "What is the sum of 11+11",
    "What is the sum of 12+12",
    "What is the sum of 13+13",
    "What is the sum of 14+14",
    "What is the sum of 15+15",
    "What is the sum of 16+16",
    "What is the sum of 17+17",
    "What is the sum of 18+18",
    "What is the sum of 19+19",
    "What is the sum of 20+20",
    #"What is the sum of 21+21", # Seems for this model there is a batch processing limit of 20
]
# If include 21st request, it will only process the request of "21+21"


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

##################The terminal output
# C:\bruh\bruhh\bruhhh\AgentCommunication> python test_example_002.py
# Execution time: 3.5655174255371094 seconds
# the type of choice 0 (i starts at 0) : <class 'huggingface_hub.inference._generated.types.chat_completion.ChatCompletionOutputComplete'>
# Response to request 1: Here are the sums for the numbers you've asked about:

# - 1 + 1 = 2
# - 2 + 2 = 4
# - 3 + 3 = 6
# - 4 + 4 = 8
# - 5 + 5 = 10
# - 6 + 6 = 12
# - 7 + 7 = 14
# - 8 + 8 = 16
# - 9 + 9 = 18
# - 10 + 10 = 20
# - 11 + 11 = 22
# - 12 + 12 = 24
# - 13 + 13 = 26
# - 14 + 14 = 28
# - 15 + 15 = 30
# - 16 + 16 = 32
# - 17 + 17 = 34
# - 18 + 18 = 36
# - 19 + 19 = 38
# - 20 + 20 = 40

# Let me know if you'd like to explore further (e.g., patterns, explanations, or larger numbers)!
