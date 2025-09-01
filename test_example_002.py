import os
import time
from huggingface_hub import InferenceClient

client = InferenceClient()

# I have five requests
user_requests = [
    "What is the sum of 9+9",
    "What is the sum of 99+99",
    "What is the sum of 999+999",
    "What is the sum of 9999+9999",
    "What is the sum of 99999+99999"
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

# The reason I see only 1+1 print statement instead of 5 + 5
# Although I got 5 elements in messages array
# The model can process all these elements in a single api call
# And the post-condition when I got the array of (var-customized) completion.choices
# There is only one element in it
# Therefore I got 1 + 1 print response

# It takes 6.37 seconds in total
# The terminal output I'm gonna include it as following:

################################
################################

# C:\bruh\bruhh\bruhhh\AgentCommunication> python test_example_002.python
# Execution time: 6.370581388473511 seconds
# the type of choice 0 (i starts at 0) : <class 'huggingface_hub.inference._generated.types.chat_completion.ChatCompletionOutputComplete'>
# Response to request 1: Let's calculate each sum step by step:

# 1. **9 + 9**
#    \( 9 + 9 = 18 \)

# 2. **99 + 99**
#    \( 99 + 99 = 198 \)

# 3. **999 + 999**
#    \( 999 + 999 = 1998 \)

# 4. **9999 + 9999**
#    \( 9999 + 9999 = 19998 \)

# 5. **99999 + 99999**
#    \( 99999 + 99999 = 199998 \)

# ### Final Answers:
# - \( 9 + 9 = \boxed{18} \)
# - \( 99 + 99 = \boxed{198} \)
# - \( 999 + 999 = \boxed{1998} \)
# - \( 9999 + 9999 = \boxed{19998} \)
# - \( 99999 + 99999 = \boxed{199998} \)

