import os
import time
from huggingface_hub import InferenceClient

client = InferenceClient()

start_time = time.time()

# user query and constraint defined as str.
user_query = "Explain which is the most famous event-driven programming architecture in 2024 and tell me why."
constraint = "The output should contain the word 'bruh' between every 5 words."

# combine them
prompt = f"{constraint}\n\n{user_query}"

# make the call
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {"role": "system", "content": "You are an assistant that follows user-defined constraints strictly."},
        {"role": "user", "content": prompt}
    ]
)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")

# Print the response
print("Response:")
print(completion.choices[0].message.content)

################################################
# .........\AgentCommunication> python test_example_006.py
# Execution time: 3.9577250480651855 seconds
# Response: 

#() The original response is a very long sentence(as a whole)
#() For display use. It has been sliced in several lines.

# bruh The most famous event-driven programming bruh architecture in 2024 
# is the bruh "Serverless Architecture," particularly bruh models like AWS Lambda, bruh Azure Functions, 
# and Google bruh Cloud Functions. This bruh architecture is dominant because bruh it scales automatically, 
# reduces bruh operational overhead, and bruh aligns perfectly with modern bruh microservices and cloud-native bruh applications. 
# Event-driven bruh systems excel in bruh handling real-time 
# data bruh processing, IoT, and bruh asynchronous workflows, 
# making bruh them ideal for bruh scalable, cost-efficient solutions. bruh The rise of bruh edge computing and bruh
# AI-driven event processing bruh has further solidified bruh its popularity.
