# from test 004 it is verified that
# 128K context length is not abundant enough for 20 complex questions.(via batch processing)
# In this example I got 5 requests containing some mid-complex questions.

import os
import time
from huggingface_hub import InferenceClient

client = InferenceClient()

user_requests = [
    "Explain the origin of the term Doge",
    "What is a 'Crescendo' in terms of piano?",
    "What is first principle theory?",
    "Briefly introduce mathematical expectation and its usage",
    "What era was it when it was 200AD?"
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


###############
###############
# C:\bruh\bruhh\bruhhh\AgentCommunication> python test_example_005.py
# Execution time: 23.87771987915039 seconds
# the type of choice 0 (i starts at 0) : <class 'huggingface_hub.inference._generated.types.chat_completion.ChatCompletionOutputComplete'>
# Response to request 1: Here are concise answers to your questions:

# 1. **Origin of "Doge"**:
#    The term *Doge* (pronounced *dohj*) originated in Venice, Italy, deriving from the Latin *dux* ("leader"). It referred to the elected chief magistrate of Venice (697–1797) or Genoa (1339–1797). The title symbolized the ruler’s authority in these maritime republics.

#    *Modern usage*: The word gained internet fame in 2013 as "Doge" (shiba inu dog memes with broken English captions like "such wow"), likely from a 2005 misspelling of "dog" on a Japanese website.

# 2. **Crescendo (Piano)**:
#    A *crescendo* in piano (and music generally) is a gradual increase in volume, indicated by the symbol **<** or the term *cresc.* It instructs the player to play louder over a passage. The opposite is *decrescendo* (decreasing volume).

# 3. **First-Principles Thinking**:
#    A problem-solving method where complex issues are broken down into their most basic, self-evident truths (axioms), then rebuilt from the ground up. Example: Elon Musk used it to reduce rocket costs by questioning assumptions about materials and manufacturing.

# 4. **Mathematical Expectation**:
#    The expected value (mean) of a random variable, representing the average outcome if an experiment is repeated many times. Calculated as:
#    - **Discrete**: *E(X) = Σ [x_i · P(x_i)]*
#    - **Continuous**: *E(X) = ∫ x · f(x) dx*
#    **Usage**: Risk assessment (e.g., insurance, gambling), statistics, and decision theory.

# 5. **200 AD Era**:
#    The year 200 AD fell in:
#    - **Roman Empire**: Pax Romana (relative peace under emperors like Septimius Severus).
#    - **Han Dynasty**: Late Eastern Han period in China (before the Three Kingdoms).
#    - **Global Context**: Classical antiquity, with major civilizations (Maya, Gupta India) flourishing. 


# Let me know if you'd like deeper dives on any topic!

### seems 5 requests in a batch is good to go!

