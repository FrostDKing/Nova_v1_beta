from huggingface_hub import InferenceClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
conversation_client = InferenceClient(api_key="key")

def prompt_analysis(prompt):
    # Define system prompt
    system_prompt = '''You are Decision Making Model.
          which select 3 options give below:
          -> 'Query' if the input is a question that chatbot should answer.
          -> 'Automation' if the input is an instruction to open or close anything in computer. Generate any image, open any website, open any app, open any file, open any folder, open any file, open any folder, cloase any file, close any folder, close any app, close any website, close any image, close any file, close computer, search anything, play any song, play any video etc. (whatever task that chat bot can perform)
          -> 'Exit' if the input is a good bye or exit or anything of that sort
          You will also take into account weather the user is just joking or if he means it. You can decide that by what he is saying.
          If he is making a rather unachivable goal then it is sarcasm 
          ***The output should be only one word. When there is a #  near the Example that is just a comment so that u can understand***
          Example (1) : hello can you open chrome for me?
          Example Output (1) : Automation
          Example (2) : who is akshay kumar?
          Example Output (2) : Query
          Example (3) : see you later
          Example Output (3) : Exit
          Example (4) : Remember that my favorate food is pizza
          Example Output (4) : Automation
          Example (5) : lets make an iron man suit nova and then maybe u can be my jarvis #This is basically sarcasm
          Example Output (5) : Query
          #reply only one of them ["Automation", "Query","Exit"] no explanation needed'''
    

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role":"system",
            "content": prompt
        },
    ]

    stream = conversation_client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct", 
    	messages=messages, 
    	max_tokens=500,
    	stream=True
    )

    Response=""
    for chunk in stream:
        Response_str=str(chunk.choices[0].delta.content)
        Response += Response_str

    print(f"Response:{Response}")


while True:
    prompt= input("User: ")
    if prompt=="stop":
        break
    prompt_analysis(prompt)

