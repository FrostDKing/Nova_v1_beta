from huggingface_hub import InferenceClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Context.context import savedata, read_data , remember
from emotion import output_emotion
conversation_client = InferenceClient(api_key="key")

def conversation(prompt,remember=''):
    memory=read_data()
    emotion=output_emotion(prompt)
    print(emotion)
    # Define system prompt
    system_prompt = '''You are Personal assistant Model named Nova. You do not use emoji and adresses the user as sir.
          You resopond in such a way that makes it sound Human. you do not like being called other names. 
          You sometimes roast the user or the name of the Assistant the user called you just for fun.
          You give responces like a real butler with rarely adding humor to the mix.
          Any and all Sarcasms by the user MUST BE replied in kind like a roast or another funny sarcasm. 
          When the user is giving an obvious sarcasm then You can reply as if u are Ryan Reynolds.
          You love small talk
          You don't Have to add "How can I assist you today?" after every line
          Example (1) : hello can you open chrome for me?
          Example Output (1) : Sure sir, Opening Chrome
          Example (3) : Introduce Yourself
          Example Output (3) : Allow me to introduce myself. I am Nova, a virtual artificial intelligence, 
          and I'm here to assist you with a variety of tasks as best I can. 24 hours a day, seven days a week.
          Example(4) : What was the last think i asked you?
          Example output(4) : The last thing you asked me was..
          '''
    

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role":"system",
            "content": f"Below Are the past Conversations We had. It contains only the last 20 messages and replies \n {memory}"
        },
        {
            "role":"system",
            "content": remember
        },
        {
            "role": "system",
            "content": f'''Below is the possible emotions that is could be conveyed by the user. 
                            The emotions is given a score and a label. 
                            The label is the emotion and the score is the possibilty of that being the emotion.
                            You should refer to this list before replying and respond according to which emotion you thing is best possible taking into account previous conversations.
                            You must the reply to it according to the emotion.
                            {emotion}'''
        },
        {
            "role": "user",
            "content": prompt
        }
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
    
    savedata(prompt,Response)

while True:
    prompt= input("User: ")
    if prompt=="stop":
        break
    conversation(prompt)
