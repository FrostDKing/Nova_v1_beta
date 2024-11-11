import requests

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": "Bearer key"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
def output_emotion(prompt):
    output = query({
    	"inputs": prompt,
    })
    sorted_output = sorted(output[0], key=lambda x: x['score'], reverse=True)[:3]

    # Print the top 3 emotions
    list_emotions=[]
    for emotion in sorted_output:
        list_emotions.append(f"Label: {emotion['label']}, Score: {emotion['score']}")
    
    return list_emotions