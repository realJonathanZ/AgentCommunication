import os
import time
from huggingface_hub import InferenceClient

client = InferenceClient()

start_time = time.time()

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": "What is the sum of 1 + 1?"
        }
    ],
)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")

# #print the object type
# print("Object type:", type(completion.choices[0].message))
# print("\n")

# print the object
print(completion.choices[0].message)
print("\n")
# print object content
print(completion.choices[0].message.content)