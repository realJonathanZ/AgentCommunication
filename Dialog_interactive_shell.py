import os
from huggingface_hub import InferenceClient

# Initialize the InferenceClient
client = InferenceClient()

def dialog_interactive_shell():
    print("this script's execution has started: " + __file__)

    # second option: setting system role (what fake / simulated personality you want it to be?)
    print("please set the system role (press enter when done):")
    system_role = ""
    while True:
        line = input()
        if line.strip() == "": # If user press 'enter' on empty line, the loop is finished
            break
        system_role += line + "\n"

    print("system role has been set successfully. Soon requesting user to enter user-input...")

    # the core array that keeps conversation history simultaneously
    messages = [{"role": "system", "content": system_role}]

    # third option: interactive loop
    while True:
        print("You: (press Enter twice when done)(Say something to AI model..)")
        user_input = ""
        while True:
            line = input().strip()
            if line == "":  # If user press 'enter' on an empty line, the input is finished
                break
            user_input += line + "\n"

        # exit condition: case-insensitive of "q" or "quit"
        if user_input.strip().lower() in ["q", "quit"]:
            print("bye..")
            break

        # append user input to the conversation history
        messages.append({"role": "user", "content": user_input})

        # api call here you go
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=messages
        )

        # fetch response content and display..
        response = completion.choices[0].message.content
        print(f"deepseekV3.1 response:\n {response}")

        # append agent response to the conversation history
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    dialog_interactive_shell()
