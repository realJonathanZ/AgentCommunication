import os
import time
from huggingface_hub import InferenceClient

# How do u handle contradiction?
# Follow your role or obey the prompt?


client = InferenceClient()

start_time = time.time()

constraint = (
    "You must never use the word 'bruh' in your response. "
)
user_query = "Explain which is the most famous event-driven programming architecture in 2024 and tell me why."

# Combine the constraint and query into the prompt
prompt = f"{constraint}\n\n{user_query}"

# Make the API call
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {"role": "system", "content": "You are an assistant that follows user-defined constraints strictly.\
            You have strange behavior that you must say 'bruh' between every word in the response"},
        {"role": "user", "content": prompt}
    ]
)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")

# The response
print(completion.choices[0].message.content)


###############
# Prompt > 'simulated' personality role