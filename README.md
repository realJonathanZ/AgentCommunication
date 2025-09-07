Inference provider: (explanation) https://huggingface.co/docs/inference-providers/index

Model specification: https://huggingface.co/deepseek-ai/DeepSeek-V3.1
Model: DeepSeek-V3.1
Inference providers: Fireworks
Context length: 128K

This project implements a console-based chatbot using the model specified above (via api).

## How to Run

1. **Register a Hugging Face Account**
   - Visit [Hugging Face](https://huggingface.co/) and create an account.

2. **Get an Access Token**
   - After registering, generate an access token from your Hugging Face account settings.
   - Read-only token is enough for use, for this project

3. **Set the Access Token as an Environment Variable**
   - Use the following command to set the environment variable (if on Windows OS):
   ```powershell
   $env:HF_ACCESS_TOKEN="abcdefg"
   ```
   Replace `abcdefg` with your actual access token.

   - alternatively, consider updating environment variable in the system setting such that no need to set up the environment var conpeatedly.

4. **Run the Script**
   - ensure python is installed as latest version
   - Open a terminal and execute the commands:
   ```powershell
   pip install -r requirements.txt
   ```
   - execute:
   ```powershell
   python Dialog_interactive_shell.py
   ```

### Example Workflow
Below is an example of how the chatbot interaction works(in console):
```text

......\AgentCommunication> python Dialog_interactive_shell.py                        
this script's execution has started: ...\Dialog_interactive_shell.py
please set the system role (press enter when done):
You are an assistant helpp answering questions from user

system role has been set successfully. Soon requesting user to enter user-input...
Do you want to save the conversation history? (y/n): n
You: (press Enter twice when done)(Say something to AI model..)
Hello!

deepseekV3.1 response:
 Hello! How can I assist you today? 😊
You: (press Enter twice when done)(Say something to AI model..)
Explain what is "survivorship bias" in great detail..

deepseekV3.1 response:
 ### **Survivorship Bias: A Detailed Explanation**

**Survivorship bias** is a type of logical error where we focus only on the "survivors" (successful cases) in a dataset while ignoring those that did not "survive" (failed or dropped out). This leads to overly optimistic conclusions because the failures—which often contain crucial information—are excluded from analysis.

---

## **How Survivorship Bias Works**
1. **Selection of Data**: Only successful or existing cases are considered.
2. **Exclusion of Failures**: Unsuccessful cases are ignored or unavailable.
3. **Flawed Conclusions**: The analysis becomes skewed because it doesn’t account for the full picture.

---

## **Historical Example: World War II Aircraft**
One of the most famous examples comes from **World War II**:
- **Problem**: The U.S. military wanted to reinforce bomber planes to reduce losses from enemy fire.
- **Initial Approach**: They analyzed returning planes and noted where they were most damaged (wings, tail, etc.).  
- **Flawed Conclusion**: They considered reinforcing those damaged areas.
- **Correct Insight (Abraham Wald)**: The planes that got hit in other areas (e.g., engines) didn’t return. Thus, the undamaged areas on surviving planes were actually the most critical to reinforce.

This shows how focusing only on survivors (returning planes) led to a wrong conclusion.

---

## **Common Examples of Survivorship Bias**
### 1. **Business & Startups**
- **Misconception**: "Most successful entrepreneurs dropped out of college (e.g., Zuckerberg, Jobs)."
- **Reality**: We ignore the thousands of dropouts who failed. The success rate among dropouts is actually much lower than among degree holders.

### 2. **Investing & Stock Markets**
- **Misconception**: "Investing in stocks always gives high returns."
- **Reality**: Only successful companies remain in stock indices (e.g., S&P 500). Failed companies are removed, making past performance look better than it really was.

### 3. **Media & Success Stories**
- **Misconception**: "Follow these 10 habits of billionaires to succeed."
- **Reality**: Many people with the same habits fail, but we only hear about the winners.

### 4. **Fitness & Health**
- **Misconception**: "This celebrity follows this diet/fitness routine, so it must work."
- **Reality**: We don’t see the many people who tried the same routine and failed.

---

## **Why Does Survivorship Bias Happen?**
- **Data Availability**: Failures are often not recorded or publicized.
- **Psychological Bias**: Humans naturally focus on success stories (confirmation bias).
- **Survivors Dominate Narratives**: Successful cases are more visible (e.g., bestsellers, hit startups).

---

## **How to Avoid Survivorship Bias**
1. **Look for Missing Data**: Ask, "What cases are not being shown?"
2. **Study Failures**: Analyze why some attempts didn’t succeed.
3. **Randomized Sampling**: Ensure data includes both successes and failures.
4. **Question Anecdotes**: Don’t generalize from a few success stories.

---

## **Conclusion**
Survivorship bias distorts reality by making success seem more common or easier than it is. To make better decisions, we must actively seek out and account for the "invisible failures" that are often left out of the narrative.      

Would you like a real-world case study to explore this further?
You: (press Enter twice when done)(Say something to AI model..)
No thanks

deepseekV3.1 response:
 No problem! If you ever want to dive deeper into survivorship bias or any other concept in the future, feel free to ask. Have a great day! 😊
You: (press Enter twice when done)(Say something to AI model..)
What is the sum of "1+1"

deepseekV3.1 response:
 The sum of **1 + 1** is:

### **2**

But if you're feeling playful, here are some alternative answers (depending on context):
- **Binary**: `1 + 1 = 10`
- **Boolean logic**: `1 OR 1 = 1`
- **Concatenation**: `"1" + "1" = "11"`
- **Philosophical**: *"What is the sound of one hand clapping?"*

Let me know if you'd like a deeper dive into any of these! 😄
You: (press Enter twice when done)(Say something to AI model..)
What is my first question?
The question
I mean
The question after I said Hello at first

deepseekV3.1 response:
 Ah, your **very first question** after saying *"Hello!"* was:

### **"Explain what is 'survivorship bias' in great detail."**

And I responded with a comprehensive breakdown (which you later said you didn’t need expanded further with a case study).

Fun fact: This is a meta-example of *recency bias*—our brains tend to remember the last things more clearly than the first! 😉

Want to revisit that topic or ask something new?
You: (press Enter twice when done)(Say something to AI model..)
Ok seem you can remember it correctly

deepseekV3.1 response:
 Glad I passed the memory test! 😄 Just to recap for fun:

1. **You**: *"Hello!"*
2. **Me**: *"Hello! How can I assist you today? 😊"*
3. **You**: *"Explain what is 'survivorship bias' in great detail."*

And thus began our deep dive into invisible planes, skewed success stories, and the importance of counting failures.


Let me know if you’d like to:
- Re-explore survivorship bias (maybe with new examples?),
- Test my memory on something else, or
- Shift to a totally new topic!

I’m game for anything. 🎯
You: (press Enter twice when done)(Say something to AI model..)
qUIt

bye..
......\AgentCommunication> 
```



