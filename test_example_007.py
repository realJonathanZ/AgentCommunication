import os
import time
from huggingface_hub import InferenceClient


class TestingDataSection:
    def __init__(self, name, address, rating):
        # This constructor is not finalized, more fields may be given. 
        # Field attribute count is uncertain.
        self.name = name
        self.address = address
        self.rating = rating

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nRating: {self.rating}"

# testing instances
data_sections = [
    TestingDataSection("Anytime Fitness", "120 Tweed Ln, Saskatoon, SK S7V 0K1, Canada", 4.4),
    TestingDataSection("Snap Fitness Saskatoon", "420 Duchess St #4, Saskatoon, SK S7K 0R1, Canada", 4.9),
    TestingDataSection("Planet Fitness", "2325 Preston Ave S, Saskatoon, SK S7J 2G2, Canada", 4.1),
    TestingDataSection("Planet Fitness", "810 Circle Dr E, Saskatoon, SK S7K 3T8, Canada", 4.3),
    TestingDataSection("THRIVE ACTIVE SASKATOON", "431 Nelson Rd, Saskatoon, SK S7S 1P2, Canada", 4.9),
    TestingDataSection("Snap Fitness", "210 Slimmon Rd #80, Saskatoon, SK S7V 0A7, Canada", 4.9),
    TestingDataSection("Motion Fitness Lawson Heights", "134 Primrose Dr, Saskatoon, SK S7K 5S6, Canada", 4.5),
    TestingDataSection("Rise Strength Lab", "2630 Jasper Ave S, Saskatoon, SK S7J 2K2, Canada", 5.0)
]

# define the constraint and category key
constraint = "the model must accept all information in a single data section and return True/False \
            based on whether the category-key matches the data section. \
            Only one word should be returned, either 'True' or 'False'."
category_key = "gym"

# client..
client = InferenceClient()

# For each section, combine constraint + catagory key + str(DataSection) into prompt
# Then, diliver the info via api call
# Then, receive response
for section in data_sections:
    prompt = f"{constraint}\n\nCategory-Key: {category_key}\n\nData Section:\n{section}"

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[
            {"role": "system", "content": "You are an assistant that follows user-defined constraints strictly."},
            {"role": "user", "content": prompt}
        ]
    )

    print(f"Data Section:\n{section}\n") # For this data section
    print(f"Response: {completion.choices[0].message.content}\n") # The response content is...



    ##############################
    ##############################

    # nah some wrong results..
    # about asking it one by one to see where is wrong? prompt? constraint? unable to search through web?