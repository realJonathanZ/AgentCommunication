import os
from huggingface_hub import InferenceClient

client = InferenceClient()

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": "How many 'G's in 'huggingface'?"
        }
    ],
)

#print the object type
print("Object type:", type(completion.choices[0].message))
print("\n")

# print the object
# Object type
print(completion.choices[0].message)
print("\n")
# Object content
print(completion.choices[0].message.content)